[toc]

# rados 报错

cmd = json.dumps({"prefix": "osd pool ls detail","format": "json"})
r = cluster.mon_command(cmd,b"") 

err:
(-22, '', u'command not known')

# 故事开局
一天下午小k 在调试 cinder 项目。 其中调用了 ceph rados 接口。
在命令行中 执行 ceph osd pool ls detail 是ok的。
但是在 rades command 接口中调用 detail 是有错误的。
```bash

cmd = json.dumps({"prefix": "osd pool ls detail","format": "json"})
r = cluster.mon_command(cmd,b"detail") 
print(r)

python learn_rados.py 
-->
(-22, '', u'command not known')

```

但是更奇怪的是  osd pool ls 却可以执行成功。
```bash

cmd = json.dumps({"prefix": "osd pool ls detail","format": "json"})
r = cluster.mon_command(cmd,b"detail") 
print(r)

python learn_rados.py 
-->
(0, '["volumes","backups","nvme","rados_create_pool"]', u'')

```

# 解决思路
搞不定，求老板，滑稽。谁让我家老板都是 码农出身。

老板告诉我，官方的 /usr/bin/ceph 可以正常执行 ceph osd pool ls detail

你可以去调试一下 python 代码呀。

# 命令行 调试 python
```bash
# ！正确方式 在需要 调试的代码文件 位置 
# import pdb;pdb.set_trace()
# ！少用 python -m pdb  调试，无法正常捕获断点，多线程
python -m pdb   /root/codes/ceph.py osd pool ls detail
```
# vscode 界面调试
记得在 调试设置中， 设置 命令参数
```bash
cd /root/codes ; /usr/bin/env /usr/bin/python /root/.vscode-server/extensions/ms-python.python-2020.12.424452561/pythonFiles/lib/python/debugpy/launcher 14937 -- /root/codes/ceph.py osd pool ls detail 

```

# 解决问题

```bash

cmd = json.dumps({"prefix": "osd pool ls","detail":"detail","format": "json"})
r = cluster.mon_command(cmd,b"") 
print(r)

-->
python learn_rados.py 
(0, '[{"pool_id":1,"pool_name":"volumes","create_time":"2020-12-16 21:02:52.159080","flags":8193,"flags_names":"hashpspool,selfmanaged_snaps","type":1,"size":2,

```

# 关键变量
valid_dict