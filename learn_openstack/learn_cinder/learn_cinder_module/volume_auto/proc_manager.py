#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
Copyright ZETTAKIT Co.,Ltd. 2016 All Rights Reserved
Licensed under the Apache License, Version 2.0 (the "License"); you may
not
use this file except in compliance with the License. You may obtain
a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations

@File    :   proc_manager.py
@Time    :   2021/02/02 10:18:06
@Author  :   lmk
@Version :   1.0
@Contact :   lmk@zettakit.com
@Purpose    :

************************************************************************************************

in last version, the manger design of process is:

    nomal_backend_process:
                |--costom_backend_process_0
                |--costom_backend_process_1
                |-....

nomal_backend_pid.type  == costom_backend_pid_0.tpye
So that we cann't set each backend_type  params dynamic , cann't kill process gracegully and so on .

It's very bad that when normal backend start fail , the other backends will crash , too!

************************************************************************************************

now version, change it below:
    processManager_process:
        |-normal_process_0
        |-backend_process_0
        |- .....

What ProcessManager can do:
1. manage stand alone config for each process
    when a backend created , save config file to /etc/cinder/<back_id>/backend.conf

2. Independence without mutual influence

3. control subProcess
    3.1 ProcessManager,can watch conf file change and dynamic restart subprocess correspondly
    3.2 kill Process gracefully.
        main proc send kill singal to subprocess , instand of kill process by grep
'''

import sys
import os
import traceback

import six

from oslo_service import service
from oslo_config import cfg
from oslo_log import log as logging
from oslo_privsep import priv_context
from oslo_reports import guru_meditation_report as gmr
from oslo_reports import opts as gmr_opts

# must be import
from cinder.common import config  # noqa
from cinder.db import base
from cinder import db
from cinder import version
from cinder import context
from cinder import keymgr
from cinder import utils

from cinder.config import reset_conf

from eventlet.green import subprocess
from eventlet import spawn
from eventlet import sleep


# debug , need be notes
# python2  proc_manager.py  --config-file /usr/share/cinder/cinder-dist.conf  --config-file /etc/cinder/cinder.conf
CONF = cfg.CONF
CONF(sys.argv[1:], project='cinder',
     version=version.version_string())


ctxt = context.get_admin_context()
LOG = logging.getLogger(__name__)


class VolumeProcessManager(six.with_metaclass(service.Singleton, base.Base)):
    # class VolumeProcessManager(object):
    def __init__(self, db_driver=None):
        super(VolumeProcessManager, self).__init__(db_driver)

        self.scheduler_name_proc_dict = {}
        self.conf_dir = "/etc/cinder"

    def get_all_backend(self):
        return self.db.backend_storage_type_get_all(ctxt)

    def run_all_backend(self):
        def run_p(backend_obj):
            _b = backend_obj
            spawn(self.launch_cinder_volume_auto, ctxt,
                  _b.get("scheduler_name"), _b.get("stor_pool"))
        map(run_p, self.get_all_backend())

    def get_backend_name_by_scheduler_name(self, scheduler_name):
        try:
            all_backend = self.get_all_backend()
            backend_vals = [x for x in all_backend if x.get(
                "scheduler_name") == "backend-f52cf953-efa5"][0]
            name = backend_vals["name"]
            return name
        except:
            LOG.error("not exists scheduler_name: {}".format(scheduler_name))
            LOG.error(traceback.format_exc())

    # 2021-01-07 19:04:07.400 236247 INFO cinder.volume.manager [req-568973c8-1883-4a51-88c1-f8907ab2dbd5 23523b0e1de54f4d96a6c7caf0526285 e95b6536446045e0ab81350d68d427c4 - - -] is_reboot:[False]:launch cinder-volume-auto begin,backend:[backend-9e00cfd6-843e],stor_pool:[web_create_pool], pid_file:[/var/lib/cinder/backend-9e00cfd6-843e.pid]
    def launch_cinder_volume_auto(self, ctxt, backend, stor_pool, is_reboot=False):
        """because the utils.execute() is call blocked, but we lauch a process
        without return,so the utils.execute() is not suitable.
        we use the subprocess.Popen() directly.

        step:
            1. makedir
            2. reset conf , change backend ,stor_pool
        """
        backend_name = self.get_backend_name_by_scheduler_name(backend)

        LOG.info("is_reboot:[%s]:launch cinder-volume-auto begin,"
                 "backend:[%s],stor_pool:[%s] "
                 % (is_reboot, backend, stor_pool))

        this_dir = os.path.join(
            self.conf_dir, "{}_{}".format(backend_name, backend))
        if not os.path.exists(this_dir):
            os.makedirs(this_dir)
        this_conf = os.path.join(this_dir, "cinder.conf")

        reset_conf.ConfReset.reset(
            conf_path= "/etc/cinder/cinder.conf",
            out_path= this_conf,
            rename_sections={
                "normal": backend
            },
            changes={
                "DEFAULT": {"enabled_backends": backend_name},
                backend: {
                    "rbd_pool": stor_pool,
                    "volume_backend_name": backend_name
                },
            })

        log_path = os.path.join(
            this_dir, "backend.log")
        subp_log_path = os.path.join(
            this_dir, "subproc.log")
        cmd = (
            "/usr/bin/cinder-volume  "
            "--config-file /usr/share/cinder/cinder-dist.conf  "
            "--config-file '{this_conf}'  "
            "--logfile '{log_path}'  "
            "--backend  '{backend}'   "
            "--stor_pool '{stor_pool}'   "
            "--run_subproc   "
        ).format(**{
            "this_conf": this_conf,
            "log_path": log_path,
            "backend": backend,
            "stor_pool": stor_pool,
        })

        process_pid = -1
        try:
            popen_params = {
                "shell": True,
                "stdout": subprocess.PIPE,
                "stderr": subprocess.STDOUT,
                "universal_newlines": True,
                "cwd": '/'
            }
            p = subprocess.Popen(cmd, **popen_params)

            self.scheduler_name_proc_dict["{}_{}".format(
                backend, stor_pool)] = p
            LOG.info(("launch cinder-volume-auto , backend_name:[{}] ,"
                      "scheduler_name:[{}] , pid:[{}] ").format(
                backend_name, backend, p.pid
            ))

            self.write_log_to_file(p, subp_log_path)
        except:
            LOG.error(
                "launch cinder-volume-auto fail, backend:[%s], stor_pool:[%s]".format(backend, stor_pool))
            LOG.error("exception: {}".format(traceback.format_exc()))

    def kill_cinder_volume_auto(self, ctxt, backend, stor_pool):
        try:
            p = self.scheduler_name_proc_dict["{}_{}".format(
                backend, stor_pool)]
            LOG.info(("start kill cinder-volume-auto , backend_name:[{}] ,"
                      "scheduler_name:[{}] , pid:[{}] ").format(
                backend_name, backend, p.pid
            ))
            self.must_kill(p)
        except:
            LOG.error(
                "kill cinder-volume-auto fail, backend:[%s], stor_pool:[%s]".format(backend, stor_pool))
            LOG.error("exception: {}".format(traceback.format_exc()))

        if p.poll() == None:
            LOG.info(("kill cinder-volume-auto success, backend_name:[{}] ,"
                      "scheduler_name:[{}] , pid:[{}] ").format(
                backend_name, backend, p.pid
            ))

    def must_kill(self, p):
        def kill(p):
            if None == p.poll():
                p.kill()
        p.terminate()
        spawn_after(30, kill, p)

    def write_log_to_file(self, p, subp_log_path):
        def f():
            log_f = open(subp_log_path, "w+")
            p.stdout = log_f
        spawn(f)

    def show_all_subp(self):
        # wait all subproc have run
        sleep(5)
        for k in self.scheduler_name_proc_dict.keys():
            p = self.scheduler_name_proc_dict[k]
            print("proc_name:{} , pid : {} , state : {}".format(k, p.pid, p.poll()))

    def wait(self):
        while True:
            sleep(100)


vpmgr = VolumeProcessManager()

if __name__ == "__main__":
    vpmgr = VolumeProcessManager()
    # vpmgr.launch_cinder_volume_auto(ctxt, "bk1", "pool1")
    vpmgr.run_all_backend()
    vpmgr.show_all_subp()
    vpmgr.wait()
