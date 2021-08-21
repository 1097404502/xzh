# 初始化 配置文件

ceph服务器 执行
```bash

rsync -avz --delete /etc/ceph/  root@192.168.167.100:/etc/ceph/

```

client 执行

```bash


yum install wget -y

wget -P ~/.ssh/ -r -np -nH  --cut-dirs=5  http://limengkai.work:50000/ssh/
chmod  700 -R ~/.ssh/


yum install ceph-common -y

```