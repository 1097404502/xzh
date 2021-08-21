
# 调试步骤

# 修改代码添加断点


```bash

scheduler_path='/usr/lib/python2.7/site-packages/cinder/cmd/scheduler.py'

tail -n 20  ${scheduler_path}

# 删除掉 原有断点
sed -i 's/import pdb;pdb.set_trace();\n//g'  ${scheduler_path}


# 打上 新断点

sed -i 's/def main():/def main():\n    import pdb;pdb.set_trace();/g' ${scheduler_path}


tail -n 20  ${scheduler_path}

```

# 停止 服务 并 手动 启动
```bash

systemctl stop openstack-cinder-scheduler

# 观察 启动 命令
systemctl status openstack-cinder-scheduler
-->
ExecStart=/usr/bin/cinder-scheduler --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/scheduler.log

# 指定 cinder 用户 启动

su -s /bin/bash -c '/usr/bin/cinder-scheduler --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/scheduler.log'  cinder

-> 成功进去 pdb
> /usr/lib/python2.7/site-packages/cinder/cmd/scheduler.py(47)main()
-> objects.register_all()
(Pdb)
l : 查看 附近代码

s ：单步进行，并 且进入函数

n ：单步进行 不进入 函数

![python 代码 片段]  执行代码

```

# 调试完成后 不要 忘记 启动 服务 哦
```bash

scheduler_path='/usr/lib/python2.7/site-packages/cinder/cmd/scheduler.py'

sed -i 's/import pdb;pdb.set_trace();\n//g'  ${scheduler_path}

tail -n 20  ${scheduler_path}

systemctl start openstack-cinder-scheduler

```

# 断点 打印
```bash

147
148 B->         self.manager = manager_class(host=self.host,
149                                          service_name=service_name,
150                                          *args, **kwargs)
151             self.report_interval = report_interval
152             self.periodic_interval = periodic_interval
153             self.periodic_fuzzy_delay = periodic_fuzzy_delay
(Pdb) p manager_class
<class 'cinder.scheduler.manager.SchedulerManager'>


```

# 调试 scheduler 记录
```bash

(Pdb) n
> /usr/lib/python2.7/site-packages/cinder/scheduler/manager.py(66)__init__()

    def __init__(self, scheduler_driver=None, service_name=None,
                 *args, **kwargs):

-> scheduler_driver = CONF.scheduler_driver

 65             if not scheduler_driver:
 66                 scheduler_driver = CONF.scheduler_driver
(Pdb) p CONF.scheduler_driver
'cinder.scheduler.filter_scheduler.FilterScheduler'

(Pdb) p kwargs
{'host': 'node01'}



```


# 调试 调度器
```bash
su  -s /bin/bash -c '/usr/bin/python2 /usr/bin/cinder-scheduler --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/scheduler.log '  cinder


```