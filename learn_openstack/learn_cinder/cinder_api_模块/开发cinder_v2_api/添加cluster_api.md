[toc]

# 主要流程
1. 设计数据库
2. 根据设计 书写  db model 文件
3. 书写 version 迁移, 生成 数据库 表
4. 编写 db api
5. 编写 cluster_api 调用 db api 并且转化 成 json 格式 的 dict 对象
6. 在 /root/zetta_code/cinder/cinder/api/contrib/cluster_manage.py 中 添加 ，处理 api 的函数


# 同步开发代码
```bash


ssh root@192.168.19.100 -t "rsync -avz /root/zetta_code/cinder/cinder/  --exclude='.vscode/'  root@192.168.64.1:/usr/lib/python2.7/site-packages/cinder/"



ssh root@192.168.64.1 'systemctl restart openstack-cinder-api.service'


ssh root@192.168.64.1 'systemctl status openstack-cinder-api.service'

# 同步数据库
su -s /bin/sh -c 'cinder-manage db sync' cinder


# pdb 调试 

systemctl stop openstack-cinder-api

ps -aux | grep '/usr/bin/python2 /usr/bin/cinder-api' | grep -v 'grep' | awk '{print $2}' | xargs -I {} kill -9 {}

su -s '/bin/bash' -c '/usr/bin/python2 /usr/bin/cinder-api --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/api.log' cinder

```

# cluster obj
```bash
(Pdb) p obj
<cinder.db.sqlalchemy.models.Cluster object at 0x86a1090>

(Pdb) p dir(obj)
['__class__', '__contains__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__getitem__', '__hash__', '__init__', '__iter__', '__mapper__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__table__', '__table_args__', '__table_initialized__', '__tablename__', '__weakref__', '_as_dict', '_decl_class_registry', '_extra_keys', '_sa_class_manager', '_sa_instance_state', 'cluster_metadata', 'created_at', 'delete', 'delete_values', 'deleted', 'deleted_at', 'get', 'id', 'items', 'iteritems', 'keys', 'metadata', 'name', 'next', 'save', 'update', 'updated_at']

(Pdb) p dict(obj)
{'name': None, 'deleted': False, 'created_at': datetime.datetime(2021, 6, 17, 7, 24, 48, 582608), 'updated_at': None, 'deleted_at': None, 'id': '0188e762-9b1a-42f4-8d95-eec46b2536d5', 'cluster_metadata': [<cinder.db.sqlalchemy.models.ClusterMetadata object at 0x86a1250>, <cinder.db.sqlalchemy.models.ClusterMetadata object at 0x86a1350>], 'metadata': {u'attr10': u'kaska', u'attr2': u'111'}}

``` 

# 编写 cluster_api 调用 db api 并且转化 成 json 格式 的 dict 对象
```bash

```

