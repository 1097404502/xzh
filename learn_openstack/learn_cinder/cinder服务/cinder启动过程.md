# cinder 启动过程
cinder 目前包含四个服务

/usr/lib/systemd/system/openstack-cinder-api.service
/usr/lib/systemd/system/openstack-cinder-volume.service
/usr/lib/systemd/system/openstack-cinder-backup.service
/usr/lib/systemd/system/openstack-cinder-scheduler.service
这四个服务在 系统

## volume service
[Unit]
Description=OpenStack Cinder Volume Server
After=syslog.target network.target rabbitmq-server.service

[Service]
Type=simple
User=cinder
TimeoutStopSec=3
ExecStart=/usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/volume.log
Restart=on-failure
Environment="CINDER_LOCALEDIR=/usr/lib/python2.7/site-packages/cinder/locale"

[Install]
WantedBy=multi-user.target




[root@node01 ~]# systemctl status openstack-cinder-volume.service  -l
● openstack-cinder-volume.service - OpenStack Cinder Volume Server
   Loaded: loaded (/usr/lib/systemd/system/openstack-cinder-volume.service; disabled; vendor preset: disabled)
   Active: active (running) since Wed 2021-01-20 09:19:02 CST; 27s ago
 Main PID: 192896 (cinder-volume)
    Tasks: 66
   Memory: 382.6M
   CGroup: /system.slice/openstack-cinder-volume.service
           ├─192896 /usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/volume.log
           ├─194183 /usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/volume.log
           ├─195293 /usr/bin/python2 /usr/bin/cinder-volume-auto --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/volume.log backend-db02abac-e464 volumes
           ├─195294 /usr/bin/python2 /usr/bin/cinder-volume-auto --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/volume.log backend-2813902f-2c94 nvme
           ├─196383 /usr/bin/python2 /usr/bin/cinder-volume-auto --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/volume.log backend-2813902f-2c94 nvme
           └─196384 /usr/bin/python2 /usr/bin/cinder-volume-auto --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/volume.log backend-db02abac-e464 volumes


## service 如何进一步启动 cinder
四个服务类似，只用 api 服务来举例
```bash

import sys

from cinder.cmd.api import main


if __name__ == "__main__":
    sys.exit(main())

```


# 调试 cinder-volume 启动过程
```bash
在 41 节点上 进行调试
# ！正确方式 在需要 调试的代码文件 位置 
# import pdb;pdb.set_trace()
# ！少用 python -m pdb  调试，无法正常捕获断点，多线程
python -m pdb  /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/volume.log
```

## 查看 conf 解析参数过程
```bash
# conf 调用位置
> /usr/lib/python2.7/site-packages/cinder/cmd/volume.py(64)main()
->  CONF(sys.argv[1:], project='cinder',
->       version=version.version_string())
(Pdb) print(sys.argv)
['/usr/bin/cinder-volume', '--config-file', '/usr/share/cinder/cinder-dist.conf', '--config-file', '/etc/cinder/cinder.conf', '--logfile', '/var/log/cinder/volume.log']


# conf 初始化位置
> /usr/lib/python2.7/site-packages/oslo_config/cfg.py(2201)__call__()
->     def __call__(self,
                 args=None,
                 project=None,
                 prog=None,
                 version=None,
                 usage=None,
                 default_config_files=None,
                 validate_default_values=False):

  clear() 清空配置obj 属性 以及缓存
   |
   |
   |  解析项目 和 默认 配置文件
  prog, default_config_files = self._pre_setup(project, ... ) 
   |
    (Pdb) print(prog)
    cinder-volume
    (Pdb) !print(default_config_files)
    ['/usr/share/cinder/cinder-dist.conf', '/etc/cinder/cinder.conf']
   |
  加载完成后, 会在 CONF._namespace 中 加载 配置文件和命令行参数 中的所有 参数。


#  执行  sudo cinder-rootwrap /etc/cinder/rootwrap.conf
priv_context.init(root_helper=shlex.split(utils.get_root_helper()))
# 未执行
utils.monkey_patch()

# 创建执行器
-> launcher = service.get_launcher()
 | 真正使用的执行器
return process_launcher()

> /usr/lib/python2.7/site-packages/oslo_service/service.py(343)__init__()
-> rfd, self.writepipe = os.pipe()


# 启用的 后端存储 backends
print(CONF.enabled_backends)
['normal']

CONF.host
'node01'
print(host)
node01@normal

```

## 启动服务关键代码
```python

# 只在  数据库中 注册服务
# 并初始化 osProfiler 请求性能分析
#82 -- /root/cinder/cinder/cmd/volume.py
server = service.Service.create(host=host,
                                service_name=backend,
                                  binary='cinder-volume')
# cinder/service.py
service.Service.create(*args)
调用次序 create(*args) -> cls(*args) -> cls.__init__(*args)
此处的 cls 代表  service.Service



# Dispose of the whole DB connection pool here before
# starting another process.  Otherwise we run into cases where
# child processes share DB connections which results in errors.
session.dispose_engine()


# 实际启动服务
# 93 -- /root/cinder/cinder/cmd/volume.py
launcher.launch_service(server)


# 发射服务接收一个 服务对象
def serve(server, workers=None):
    global _launcher
    if _launcher:
        raise RuntimeError(_('serve() can only be called once'))
    _launcher = service.launch(CONF, server, workers=workers)

# /usr/lib/python2.7/site-packages/oslo_service/service.py(447)_start_child()
# 最终执行的 是 server.launch 方法
LOG.info(_LI('Starting %d workers'), wrap.workers)
while self.running and len(wrap.children) < wrap.workers:
  self._start_child(wrap)

# 查看子进程启动
grep ".Popen(" -r ./cinder
./cinder/backup/drivers/ceph.py:            p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE,
./cinder/backup/drivers/ceph.py:            p2 = subprocess.Popen(cmd2, stdin=p1.stdout,
./cinder/tests/unit/test_backup_ceph.py:        class MockPopen(object):
./cinder/volume/manager.py:        we use the subprocess.Popen() directly.
./cinder/volume/manager.py:            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,

```

# pdb 跨文件打断点

```bash
# ！正确方式 在需要 调试的代码文件 位置 
# import pdb;pdb.set_trace()
# ！少用 python -m pdb  调试，无法正常捕获断点，多线程
python -m pdb  /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/volume.log
> /usr/bin/cinder-volume(4)<module>()
-> import sys
(Pdb) b  /usr/lib/python2.7/site-packages/cinder/volume/manager.py:launch_cinder_volume_auto
*** Bad lineno: launch_cinder_volume_auto
(Pdb) b  /usr/lib/python2.7/site-packages/cinder/volume/manager.py:3798
Breakpoint 1 at /usr/lib/python2.7/site-packages/cinder/volume/manager.py:3798
(Pdb) c
Option "logdir" from group "DEFAULT" is deprecated. Use option "log-dir" from group "DEFAULT".
Option "verbose" from group "DEFAULT" is deprecated for removal.  Its value may be silently ignored in the future.
> /usr/lib/python2.7/site-packages/cinder/volume/manager.py(3798)VolumeManager()
-> def launch_cinder_volume_auto(self, ctxt, backend, stor_pool, is_reboot=False):

(Pdb) w
  /usr/lib64/python2.7/bdb.py(400)run()
-> exec cmd in globals, locals
  <string>(1)<module>()
  /usr/bin/cinder-volume(10)<module>()
-> sys.exit(main())
  /usr/lib/python2.7/site-packages/cinder/cmd/volume.py(83)main()
-> binary='cinder-volume')
  /usr/lib/python2.7/site-packages/cinder/service.py(269)create()
-> **kwargs)
  /usr/lib/python2.7/site-packages/cinder/service.py(128)__init__()
-> manager_class = importutils.import_class(self.manager_class_name)
  /usr/lib/python2.7/site-packages/oslo_utils/importutils.py(30)import_class()
-> __import__(mod_str)
  /usr/lib/python2.7/site-packages/cinder/volume/manager.py(220)<module>()
-> class VolumeManager(manager.SchedulerDependentManager):
> /usr/lib/python2.7/site-packages/cinder/volume/manager.py(3798)VolumeManager()
-> def launch_cinder_volume_auto(self, ctxt, backend, stor_pool, is_reboot=False):
```