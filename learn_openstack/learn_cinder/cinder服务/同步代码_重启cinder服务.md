[toc]

# 连接开发集群
参考其他文档

# 从19.10 将代码 发送到 41
```bash
git checkout 稳定的版本

rsync -a -v -e ssh  --exclude='*.pyc'      /root/cinder/cinder root@192.168.41.1:/usr/lib/python2.7/site-packages

rsync -a -v -e ssh  --exclude='*.pyc'      /root/cinder/cinder root@192.168.40.10:/usr/lib/python2.7/site-packages



```

# 更新 filters
```bash
cat > /etc/cinder/rootwrap.d/volume.filters <<"EOF"
[Filters]
mkdir: RegExpFilter, mkdir, root, mkdir, -p, /etc/cinder/.*
chown: RegExpFilter, chown, root, chown, -R, cinder:cinder, /etc/cinder/.*

EOF
```

 rsync -a -v -e ssh  --exclude='*.pyc'  /usr/lib/python2.7/site-packages/cinder  root@192.168.40.10:/usr/lib/python2.7/site-packages/

# 手动启动服务测试代码
```bash

su -s /bin/sh -c "/usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/volume.log" cinder

如果没有问题，从 1节点 同步代码 to 其他节点，并且 重启服务 即可

```

# 同步代码重启cinder 服务
```bash
ssh-copy-id -i /root/.ssh/id_rsa.pub root@192.168.41.1

rsync -a -v -e ssh  --exclude='*.pyc'    /root/essay/learn_cinder/cinder服务/script  root@192.168.41.1:/root/

ssh root@192.168.41.1

/root/script/restart_all_cinder.sh

grep -E "`date -I`.*ERROR.* " -r /var/log/cinder/ | grep -v "oslo.messaging._drivers.impl_rabbit" |grep "ERROR"
grep -E "`date -I`.*ERROR.* " -r /etc/cinder/ | grep -v "oslo.messaging._drivers.impl_rabbit" |grep "ERROR"


```

# 查看 service 日志
```bash

# -u 指定 某个 service
journalctl -u openstack-cinder-api

# -f 持续监听
journalctl -f -u openstack-cinder-api

```

# 找回

None_backend-bdd09584-5282  policy.json                             testo_backend-b465050a-c7a9
api-paste.ini               rootwrap.conf                           use_backend_backend-bdd09584-5282
cinder.conf                 rootwrap.d                              volumes
normal_backend_0000         test_change_pool_backend-046e1866-c74d

su -s /bin/sh -c "/usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/volume.log" cinder
