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

@File    :   test_spawn.py
@Time    :   2021/02/02 18:02:22
@Author  :   lmk
@Version :   1.0
@Contact :   lmk@zettakit.com
@Purpose    :   None
'''

from eventlet import spawn

def spawn_args(args):
    print( args )

def f():
    obj_list = [{"x":"121"},{"x":"zxc"}]
    map(spawn_args,obj_list)

if __name__ == "__main__":
    f()
