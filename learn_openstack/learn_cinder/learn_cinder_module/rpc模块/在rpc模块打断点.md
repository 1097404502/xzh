# 调试
```bash

cinder/service.py  174 左右

import pdb;pdb.set_trace()
self.rpcserver = rpc.get_server(target, endpoints, serializer)

su -s /bin/bash -c  '/usr/bin/cinder-scheduler --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/scheduler.log' cinder

(Pdb) p target.__dict__
{'version': None, 'exchange': None, 'accepted_namespaces': [None], 'namespace': None, 'server': 'node01', 'topic': 'cinder-scheduler', 'fanout': None}
(Pdb) p endpoints
[<cinder.scheduler.manager.SchedulerManager object at 0x4920510>, <cinder.scheduler.manager._SchedulerV1Proxy object at 0x48b2810>]
(Pdb) p serializer
<cinder.objects.base.CinderObjectSerializer object at 0x544cad0>




```
# 调试 schdural

# 调试 volume service
```bash

su -s /bin/bash -c '/usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/ceph2_backend-812ac12a-d779/cinder.conf --logfile /etc/cinder/ceph2_backend-812ac12a-d779/backend.log --run_subproc' cinder

p target
<Target topic=cinder-volume, server=node01@backend-812ac12a-d779>

systemctl status openstack-cinder-volume 

```

# 调试 volume api
```bash

systemctl stop openstack-cinder-api



su -s /bin/bash -c '/usr/bin/cinder-api --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/api.log' cinder

```

# 调试 volume
```bash

> /usr/lib/python2.7/site-packages/cinder/volume/backends.py(288)create_backend_bind()
-> for host in hosts:
(Pdb) l
283                 hosts = []
284                 for service in services:
285                     if utils.service_is_up(service):
286                         if service.host not in hosts:
287                             hosts.append(service.host)
288  ->             for host in hosts:
289                     LOG.info("launch cinder volume [%s] auto in host: "
290                         "[%s]" % (backend_type['name'], host))
291                     volume_rpcapi.launch_cinder_volume(context,
292                         host, backend_type['scheduler_name'],
293                         backend_type['stor_pool'])
(Pdb) n
> /usr/lib/python2.7/site-packages/cinder/volume/backends.py(289)create_backend_bind()
-> LOG.info("launch cinder volume [%s] auto in host: "
(Pdb) p host
u'node01@backend-39294f71-0a91'
(Pdb) p hosts
[u'node01@normal', u'node01@backend-39294f71-0a91', u'node01@backend-812ac12a-d779', u'node01@backend-f44f1809-aaf7', u'node01@backend-b87cda78-0d93', u'node01@backend-976e5f35-e952']
(Pdb)


hosts = [u'node01@normal', u'node01@backend-39294f71-0a91', u'node01@backend-812ac12a-d779', u'node01@backend-f44f1809-aaf7', u'node01@backend-b87cda78-0d93', u'node01@backend-976e5f35-e952']

node_list = []

for host in hosts:
    node = host.split('@')[0]
    if node in node_list:
        continue
    node_list += node

```

#  调试 api
```bash


rsync -avz /root/my_proj/cinder/cinder/  root@192.168.81.1:/usr/lib/python2.7/site-packages/cinder/

systemctl | grep openstack-cinder  | grep -v grep |  awk '{print $1}' | xargs systemctl restart

systemctl stop openstack-cinder-api.service

su -s /bin/bash  -c '/usr/bin/python2 /usr/bin/cinder-api --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/api.log' cinder

lsof -i:8776 | awk '{print $2}'  | grep -v PID | xargs kill -9

b12 The server has either erred or is incapable of performing the requested operation.


```

# 调试  数据库
```bash

mysql -u cinder -p 
 pwd: cinder_dbpass

use cinder;

show tables;

select * from services limit 1 ;

| created_at          | updated_at          | deleted_at | deleted | id | host   | binary        | topic         | report_count | disabled | availability_zone | disabled_reason | modified_at | rpc_current_version | rpc_available_version | object_current_version | object_available_version | replication_status | frozen | active_backend_id |

 node01@backend-251da9a3-4ccf
UPDATE services SET deleted = 1 WHERE host like '%@backend%' ;


```

