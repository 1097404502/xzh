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

@File    :   reset_conf.py
@Time    :   2021/02/02 09:55:45
@Author  :   lmk
@Version :   1.0
@Contact :   lmk@zettakit.com
@Purpose    :   None
'''

import re


class ConfReset(object):
    """
    how to use: 
    such as: i want change conf from ./cinder.conf  to  ./test.conf and rename [normal] -> [backend-111-111] ,
    reset [DEFAULT].workers ,
    add [normal].red_user

    [DEFAULT]
    osapi_volume_listen = 192.168.41.1
    osapi_volume_workers = 12  *
    ....
    [normal]
    volume_backend_name = normal
    rbd_user = openstack *

    *******************************************************************
    -->
    [DEFAULT]
    osapi_volume_listen = 192.168.41.1
    osapi_volume_workers = 24  *
    ....
    [backend-111-111] *
    volume_driver = cinder.volume.drivers.rbd.RBDDriver
    rbd_pool = volumes


    [add_section]   *
    new_param3 = @12,.12.   *
    new_param1 = h:pp:t@!   *

    [normal] *
    rbd_user = cinder  *


    just:
        ConfReset.reset("./cinder.conf", "./test.conf",
                        {"normal": "backend-111-111"},
                        {
                            "DEFAULT": {"osapi_volume_workers": "20"},
                            "normal": {"rbd_user": "cinder"},
                            "add_section": {
                                "new_param3": "@12,.12.",
                                "new_param1": "h:pp:t@!"
                            }
                        })
    """

    s_parrten = re.compile("^\s+$")

    def __init__(self):
        pass

    @staticmethod
    def reset(conf_path, out_path, rename_sections, changes):
        conf_path = conf_path or "/etc/cinder/cinder.conf"
        r = []
        with open(conf_path, "r") as f:
            r = f.readlines()

        r = ConfReset.rename_section(r, rename_sections)

        for section in changes.keys():
            for param in changes.get(section, {}).keys():
                val = changes.get(section).get(param)
                r = ConfReset.change_param(r, section, param, val)

        with open(out_path, "w") as f:
            f.writelines(r)

    @staticmethod
    def rename_section(r, rename_sections):
        """
        demo: rename [normal] -> [backend-111-111]
        """
        for section in rename_sections.keys():
            for i in range(len(r)):
                if r[i].startswith("[{}]".format(section)):
                    r[i] = "[{}]\n".format(rename_sections.get(section))
                    break
        return r

    @staticmethod
    def change_param(r, section, param, val):
        now_section = ""
        has_section = False
        has_param = False
        for i in range(len(r)):
            if r[i].startswith("[{}]".format(section)):
                now_section = section
                has_section = True
            if now_section == section and r[i].startswith("{}".format(param)):
                r[i] = "{} = {}\n".format(param, val)
                has_param = True
                break
        if not has_section:
            r = ConfReset.add_section(r, section)
        if not has_param:
            r = ConfReset.add_param(r, section, param, val)
        return r

    @staticmethod
    def add_section(r, section):
        if r[-1] != "\n":
            r.append("\n")
        r.append("[{}]\n".format(section))
        return r

    @staticmethod
    def add_param(r, section, param, val):
        now_section = ""
        for i in range(len(r)):
            if r[i].startswith("[{}]".format(section)):
                now_section = section
            if now_section == section and (ConfReset.s_parrten.match(r[i])
                                           or i == len(r) - 1
                                           ):
                r.insert(i + 1, "{} = {}\n".format(param, val))
                break
        return r


if __name__ == "__main__":
    ConfReset.reset("./cinder.conf", "./test.conf",
                    {"normal": "backend-111-111"},
                    {
                        "DEFAULT": {"osapi_volume_workers": "20"},
                        "normal": {"rbd_user": "cinder"},
                        "add_section": {
                            "new_param3": "@12,.12.",
                            "new_param1": "h:pp:t@!"
                        }
                    })
