# db_api 路径
/usr/lib/python2.7/site-packages/
    #调用
    cinder/db/api.py
    #实现层
    cinder/db/sqlalchemy/api.py

# 实现功能 根据 service.host 从数据库中删除数据
|      Binary |          Host  |   Zone   |  Status | State |         Updated_at         | Disabled Reason |
|  cinder-volume   | node01@backend-2813902f-2c94 | zettakit | enabled |   up  | 2021-01-|        -        |


# cinder数据库配置

[database]
connection = mysql+pymysql://cinder:cinder_dbpass@192.168.41.10/cinder
max_retries = -1
retry_interval = 1
use_db_reconnect = true
db_max_retry_interval = 1
db_max_retries = -1

# 实现思路
1. 学习 sqlalchemy 操作
完成  cinder/db/sqlalchemy/api.py 中 delete service 函数

根据 host 删除 service

2. 测试 函数。
3. 加入项目代码。


# service-list 调用过程
../cinderclient/cinderclient/v2/shell.py:    columns = ["Binary", "Host", "Zone", "Status", "State", "Updated_at"]

## do_service_list 实现
```bash
@utils.arg('--host', metavar='<hostname>', default=None,
           help='Host name. Default=None.')
@utils.arg('--binary', metavar='<binary>', default=None,
           help='Service binary. Default=None.')
@utils.arg('--withreplication',
           metavar='<True|False>',
           const=True,
           nargs='?',
           default=False,
           help='Enables or disables display of '
                'Replication info for c-vol services. Default=False.')
@utils.service_type('volumev2')
def do_service_list(cs, args):
    """Lists all services. Filter by host and service binary."""
    replication = strutils.bool_from_string(args.withreplication)
    result = cs.services.list(host=args.host, binary=args.binary)
    columns = ["Binary", "Host", "Zone", "Status", "State", "Updated_at"]
    if replication:
        columns.extend(["Replication Status", "Active Backend ID", "Frozen"])
    # NOTE(jay-lau-513): we check if the response has disabled_reason
    # so as not to add the column when the extended ext is not enabled.
    if result and hasattr(result[0], 'disabled_reason'):
        columns.append("Disabled Reason")
    utils.print_list(result, columns)
```

# 每一个 service 的属性
```bash

['HUMAN_ID', 'NAME_ATTR', '__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattr__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_add_details', '_append_request_id', '_info', '_loaded', 'append_request_ids', 'binary', 'disabled_reason', 'get', 'host', 'human_id', 'is_loaded', 'manager', 'request_ids', 'set_loaded', 'setup', 'state', 'status', 'to_dict', 'updated_at', 'x_openstack_request_ids', 'zone']

```

# 服务端代码 位置
```bash

../cinder/cinder/api/contrib/services.py:        resource = extensions.ResourceExtension('os-services', controller)

```


# 测试 修改结果
[root@node02 ~]# cinder backends-list
resp : 
body : 
+--------------------------------------+-----------------+-----------+---------+-----------------+-------------+
|                  ID                  |       Name      | Is_Public | Is_bind |    Stor_pool    | Description |
+--------------------------------------+-----------------+-----------+---------+-----------------+-------------+
| 2813902f-2c94-4ff9-988a-2b475e0bd5a5 |   performance   |    True   |   True  |       nvme      |      -      |
| deffaf27-95b1-41ca-862f-43075258a8e5 | web_backends222 |    True   |  False  | web_create_pool |      -      |
| ffdc2630-def2-4301-a21a-564792610430 |   web_backends  |    True   |  False  | web_create_pool |      -      |
+--------------------------------------+-----------------+-----------+---------+-----------------+-------------+


[root@node02 ~]# cinder service-list
resp : 
body : 
+------------------+------------------------------+----------+---------+-------+----------------------------+-----------------+
|      Binary      |             Host             |   Zone   |  Status | State |         Updated_at         | Disabled Reason |
+------------------+------------------------------+----------+---------+-------+----------------------------+-----------------+
|  cinder-backup   |            node01            | zettakit | enabled |   up  | 2021-01-12T09:28:10.000000 |        -        |
|  cinder-backup   |            node02            | zettakit | enabled |   up  | 2021-01-12T09:28:11.000000 |        -        |
| cinder-scheduler |            node01            | zettakit | enabled |   up  | 2021-01-12T09:28:18.000000 |        -        |
| cinder-scheduler |            node02            | zettakit | enabled |   up  | 2021-01-12T09:28:14.000000 |        -        |
|  cinder-volume   | node01@backend-2813902f-2c94 | zettakit | enabled |   up  | 2021-01-12T09:28:13.000000 |        -        |
|  cinder-volume   | node01@backend-deffaf27-95b1 | zettakit | enabled |   up  | 2021-01-12T09:28:13.000000 |        -        |
|  cinder-volume   | node01@backend-ffdc2630-def2 | zettakit | enabled |   up  | 2021-01-12T09:28:13.000000 |        -        |
|  cinder-volume   |        node01@normal         | zettakit | enabled |   up  | 2021-01-12T09:28:12.000000 |        -        |
|  cinder-volume   | node02@backend-2813902f-2c94 | zettakit | enabled |   up  | 2021-01-12T09:28:14.000000 |        -        |
|  cinder-volume   | node02@backend-deffaf27-95b1 | zettakit | enabled |   up  | 2021-01-12T09:28:13.000000 |        -        |
|  cinder-volume   | node02@backend-ffdc2630-def2 | zettakit | enabled |   up  | 2021-01-12T09:28:14.000000 |        -        |
|  cinder-volume   |        node02@normal         | zettakit | enabled |   up  | 2021-01-12T09:28:12.000000 |        -        |
+------------------+------------------------------+----------+---------+-------+----------------------------+-----------------+

cinder backends-create web_backends web_create_pool

cinder  type-key volume_type set 'volume_backend_name'='web_backends' 'backend_name'='web_backends'

cinder  type-key volume_type unset 'volume_backend_name' 'backend_name'

cinder backends-delete   c3a3e629-4c8d-46c1-9fc8-09364aedabff 

grep -E "$today.*ERROR" -r /var/log/cinder


today=`date "+%Y-%m-%d"`
grep -E "$today 18.*ERROR" -r /var/log/cinder

grep "Kill cinder volume service not found" -r /var/log/cinder

ps -axf |grep "ffdc2630-def2" 

ps -aux | grep "80522317-0ba1" |grep -v grep|awk '{print $2}'


# 根据进程关键字 查杀 进程
c3a3e629-4c8d
psinfo="80522317-0ba1"
for PID in `ps -aux | grep "$psinfo" |grep -v grep|awk '{print $2}'`
do
    echo "kill $PID success"
    kill $PID
done

psinfo="80522317-0ba1"
for PID in `ps -aux | grep "$psinfo" |grep -v grep|awk '{print $2}'`; do echo "kill $PID success"; kill $PID; done
