#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2021/02/01 09:32:35
@Author  :   lmk
@Version :   1.0
@Contact :   lmk@zettakit.com
@Purpose    :   None
'''

import sys
import sqlite3

def import_module(import_str):
    """Import a module.

    .. versionadded:: 0.3
    """
    __import__(import_str)
    return sys.modules[import_str]

def m():
    o = import_module("os")
    print(o)
    sq3 = import_module("sqlite3")
    print(sq3)

if __name__ == "__main__":
    m()
