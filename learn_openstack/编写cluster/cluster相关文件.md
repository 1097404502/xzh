# 定义相关的 文件

api 层面 
/root/community/cinder/cinder/api/v3/clusters.py

object 相关  
/root/community/cinder/cinder/objects/cluster.py

其中 object 中 用到了 动态 register class 的 手法，详细 参看 import_module

# 测试机规格

组件虚机
4核  mem 8   strage 40g

mysql  rabbit

mysql  Ver 15.1 Distrib 10.1.38-MariaDB, for Linux (x86_64) using readline 5.1
[{rabbit,"RabbitMQ","3.7.4"},

ceph -v
ceph version 0.2.10




