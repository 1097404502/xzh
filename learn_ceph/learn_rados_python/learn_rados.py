#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@File    :   learn_rados.py
@Time    :   2021/01/05 13:37:15
@Author  :   lmk
@Version :   1.0
"""

from __future__ import print_function

import rados
import re
import json
import traceback

cluster = rados.Rados(
    conffile="/etc/ceph/ceph.conf",
    conf=dict(keyring="/etc/ceph/ceph.client.admin.keyring"),
)


def safe_connect_c(f):
    def x(*args, **kargs):
        try:
            cluster.connect()
            f(*args, **kargs)
        except Exception as e:
            traceback.print_exc()
        cluster.shutdown()

    return x


def get_cluster():
    fs_id = cluster.get_fsid()
    print(cluster.get_fsid())
    cluster_stats = cluster.get_cluster_stats()
    print(cluster_stats)
    cluster.create_pool("rados_create_pool")
    pools = cluster.list_pools()
    print(pools)


def use_mon_commend():
    # ceph osd ls
    # cmd = json.dumps({"prefix": "osd ls", "ids": ["2"], "format": "json"})
    # r = cluster.mon_command(cmd,"")
    # print(r)
    cmd = json.dumps({"prefix": "osd pool ls", "detail": "detail", "format": "json"})
    r = cluster.mon_command(cmd, b"")
    print(r)
    # cmd = json.dumps({"prefix": "osd pool ls detail","format": "json"})
    # r = cluster.mon_command(cmd,b"detail")
    # print(r)
    # cmd = json.dumps({"prefix": "osd pool ls","format": "json"})
    # r = cluster.mon_command(cmd,b"detail")
    # print(r)


@safe_connect_c
def main0():
    # get_cluster()
    use_mon_commend()


if __name__ == "__main__":
    main0()