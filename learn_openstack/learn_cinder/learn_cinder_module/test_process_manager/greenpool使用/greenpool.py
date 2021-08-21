#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   greenpool.py
@Time    :   2021/01/29 13:47:46
@Author  :   lmk
@Version :   1.0
@Contact :   lmk@zettakit.com
@Purpose    :   None
'''
import cProfile
from eventlet.greenpool import GreenPool

def profile_statics(f):
    def wrap(*args,**kwargs):
        with cProfile.Profile() as pr:
            # ... do something ...
            f()
        pr.print_stats(sort=1)
    return wrap

# @profile_statics
def m():

    def f(args):
        def x(*y):
            print(y)
        grp =  GreenPool()
        list(grp.starmap(x , [[1,2,3] for x in  range(1000)]))
        grp.waitall()
    f(0)


# run sequence
def s():
    [ print([1,2,3]) for x in range(1000)]

if __name__ == "__main__":
    # with cProfile.Profile() as pr:
    pr = cProfile.Profile()
    pr.enable()
    #   63852 function calls (62836 primitive calls) in 1.378 seconds
    # m()
    #   1621 function calls in 0.045 seconds
    s()
    pr.print_stats(sort=1)




