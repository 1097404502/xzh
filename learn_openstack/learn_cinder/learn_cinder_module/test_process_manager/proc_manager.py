#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   process.py
@Time    :   2021/01/28 17:03:10
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
import subprocess as sp
import eventlet
eventlet.monkey_patch()
from eventlet import spawn,spawn_after,sleep
import eventlet.debug
eventlet.debug.hub_prevent_multiple_readers(False)

# RuntimeError: Second simultaneous read on fileno 6 detected.  Unless you really know what you're doing, make sure that only one greenthread can read any particular socket.  Consider using a pools.Pool. If you do know what you're doing and want to disable this error, call eventlet.debug.hub_prevent_multiple_readers(False) - MY THREAD=<built-in method switch of GreenThread object at 0x7fbd883d1050>; THAT THREAD=FdListener('read', 6, <built-in method switch of GreenThread object at 0x7fbd883b60f0>, <built-in method throw of GreenThread object at 0x7fbd883b60f0>)
_out = sys.stdout.write

eventlet.pools.Pool
class VolumeProcessManager(object):
    def __init__(self):
        self._proc_dict = {}
        self.run_subprocs()
        self.get_all_subp_out()
        self.wait_all()
        # self.x = input()

    def get_backends_conf(self):
        return range(3)

    def run_subprocs(self):
        list(map(self.run_subproc, self.get_backends_conf()))

    def run_subproc(self, cmd):
        p = sp.Popen(["python","./capture_process.py","2>&1"], stdout=sp.PIPE ,stderr=sp.STDOUT,universal_newlines=True)
        self._proc_dict[p.pid] = p
        print("pid: ",p.pid)

    def wait_all(self):
        _p_statues = {}
        while True:
            # None 代表未 全部 退出 ,1 代表 所有sub p退出
            all_code = 1
            for p in self._proc_dict.values():
                ret_code = p.poll()
                if _p_statues.get(p.pid,"null") != ret_code:
                    _p_statues[p.pid] = ret_code
                    _out("{} stat: {}\n".format(p.pid,ret_code))
                if ret_code ==None:
                    # 代表 子进程还在运行
                    all_code = None
                    # 其实此时就可以终止判断， 但是为了 更好地体验交互，就不提前退出了
                    # break
            if all_code != None:
                break
            sleep(1)
        # [p.wait() for p in self._proc_dict.values()]
    
    def get_all_subp_out(self):
        def f():
            while True:
                sleep(1)
                for p in self._proc_dict.values():
                    self.get_subp_out(p)
        spawn(f)  

    @staticmethod
    def get_subp_out(p):
        def read_line(p):
            out = p.stdout.readline()
            _out(out)
        spawn(read_line,p)

    @staticmethod
    def real_kill(p):
        def force_kill(p):
            if p.poll() == None:
                p.kill()
        p.terminate()
        spawn_after(5,force_kill,p)
        



if __name__ == "__main__":
    VolumeProcessManager()
