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

@File    :   start_kill_volume_auto.py
@Time    :   2021/02/02 10:11:15
@Author  :   lmk
@Version :   1.0
@Contact :   lmk@zettakit.com
@Purpose    :   None
'''


def launch_cinder_volume_auto(self, ctxt, backend, store_pool, is_reboot=False):
    """because the utils.execute() is call blocked, but we lauch a process
    without return,so the utils.execute() is not suitable.
    we use the subprocess.Popen() directly.

    step:
        1. makedir
        2. reset conf , change backend ,store_pool
    """
    pid_file_path = CONF.state_path
    pid_file = pid_file_path + "/" + backend + ".pid"
    LOG.info("is_reboot:[%s]:launch cinder-volume-auto begin,"
             "backend:[%s],store_pool:[%s], pid_file:[%s]"
             % (is_reboot, backend, store_pool, pid_file))
    cmd = (
        'mkdir '
        '/usr/bin/cinder-volume '
        '--config-file /usr/share/cinder/cinder-dist.conf  '
        # '--config-file /etc/cinder/cinder.conf '
        '--config-file {this_conf} '
        '--logfile /var/log/cinder/volume.log'
        '--backend  {backend} '
        '--store_pool {store_pool} '
    ).format({
        "this_conf":"xxx",
        "backend":"ccc",
        "store_pool":"ddd"
    })

    process_pid = -1
    try:
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                             cwd='/')
        LOG.info("launch cinder-volume-auto end, pid:[%s]" % (p.pid))
        process_pid = p.pid
    except Exception as ex:
        LOG.error("failed to launch cinder-volume-auto: %s" % (str(ex)))

    try:
        with open(pid_file, 'w') as fp:
            fp.write(str(process_pid))
    except IOError as ex:
        LOG.error("failed to write pid into file, file:[%s],err:[%s]"
                  % (pid_file, str(ex)))


def kill_cinder_volume_auto(self, ctxt, backend, store_pool):
    pid_file_path = CONF.state_path
    pid_file = pid_file_path + "/" + backend + ".pid"
    LOG.info("kill cinder-volume-auto begin, backend:[%s], store_pool:[%s],"
             "pid_file:[%s]"
             % (backend, store_pool, pid_file))

    try:
        with open(pid_file, 'r') as fp:
            pid = fp.readline()
    except IOError as ex:
        LOG.error("failed to read file:[%s], err:[%s]" % (pid_file, str(ex)))
    else:
        out = None
        err = None
        try:
            cmd = "pstree " + pid + " -p" + \
                "|awk -F'[()]' '{for(i=1;i<=NF;i++)if($i~/[0-9]+/) print $i}' " + \
                "|xargs kill -9"
            out, err = utils.execute(cmd, shell=True)
        except OSError as e:
            LOG.error("kill cinder-volume-auto:oserror:[%s], pid:[%s]"
                      % (str(e), pid))
        except processutils.ProcessExecutionError as e:
            LOG.error("kill cinder-volume-auto:ProcessExecutionError:[%s],"
                      " pid:[%s]" % (str(e), pid))
        except Exception as e:
            LOG.error("kill cinder-volume-auto:Expection:[%s], pid:[%s]"
                      % (str(e), pid))

        if out is not None:
            LOG.info("kill cinder-volume-auto end, "
                     "backend:[%s], store_pool:[%s], pid:[%s]"
                     % (backend, store_pool, pid))
        os.remove(pid_file)


if __name__ == "__main__":
    pass
