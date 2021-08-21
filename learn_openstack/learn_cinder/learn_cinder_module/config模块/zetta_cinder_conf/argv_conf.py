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

@File    :   argv_conf.py
@Time    :   2021/02/02 17:11:15
@Author  :   lmk
@Version :   1.0
@Contact :   lmk@zettakit.com
@Purpose    :   None
'''

import sys

from oslo_config import cfg

from cinder import version


cmd_opts = [
    cfg.StrOpt('log_path',help="save log path"),
    cfg.BoolOpt('run_proc',default=False,help="start subproc")
]


CONF = cfg.CONF
CONF.register_cli_opts(cmd_opts)

# python argv_conf.py  --log_path 1212
if __name__ == "__main__":
    CONF(sys.argv[1:], project='cinder',
         version=version.version_string())
    print(CONF.__dict__)
    print(CONF.log_path)
    print(CONF.run_proc)
    pass
