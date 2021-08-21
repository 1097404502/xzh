#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   capture_process.py
@Time    :   2021/01/29 09:31:18
@Author  :   lmk
@Version :   1.0
@Contact :   lmk@zettakit.com
@Purpose    :   mock one process can be terminate 
'''

# import signal
 
# signal.SIGABORT
# signal.SIGHUP  # 连接挂断
# signal.SIGILL  # 非法指令
# signal.SIGINT  # 连接中断
# signal.SIGKILL # 终止进程（此信号不能被捕获或忽略）
# signal.SIGQUIT # 终端退出
# signal.SIGTERM # 终止
# signal.SIGALRM  # 超时警告
# signal.SIGCONT  # 继续执行暂停进程

import signal,time
import sys
import eventlet
eventlet.monkey_patch()
from eventlet import sleep

def term_sig_handler(signum,frame):
    std_print("i do not want be kill ! you can not kill me ! hahaha !\n")

def std_print(*args):
    s = " ".join(args)+"\n"
    sys.stdout.write(s)
    sys.stdout.flush()


#  ps -aux|grep capture_process | grep -v grep|awk '{print $2}'|xargs kill -9
# ps -aux|grep capture_process | grep -v grep
if __name__ == "__main__":
    signal.signal(signal.SIGTERM,term_sig_handler)
    signal.signal(signal.SIGINT,term_sig_handler)
    std_print("start")
    while True:
        std_print("sleep module:",sleep.__module__ )
        sleep(10)
    std_print("end")
