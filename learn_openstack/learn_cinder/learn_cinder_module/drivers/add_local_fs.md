
# 调试代码
```bash

# 同步代码
rsync -avz /root/my_proj/cinder/cinder/  root@192.168.99.1:/usr/lib/python2.7/site-packages/cinder/


# volume
su -s /bin/bash -c '/usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/localfs_backend-1a1aebe3-be75/cinder.conf --logfile /var/log/cinder/backend-1a1aebe3-be75.log --run_subproc' cinder


# schedular
su -s /bin/bash -c '/usr/bin/cinder-scheduler --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/scheduler.log' cinder


```
# bug

## 调度器 问题
```bash
2021-06-02 13:13:16.998 16629 INFO cinder.scheduler.base_filter [req-4ea1d276-73f4-4a12-88d6-631d983b0538 c0c8c10aeffb44c4a3d7f5af395361f8 36fd4b70c12a4d69b7c78eb771025200 - - -] Filter CapabilitiesFilter returned 0 host(s)
2021-06-02 13:13:16.999 16629 WARNING cinder.scheduler.filter_scheduler [req-4ea1d276-73f4-4a12-88d6-631d983b0538 c0c8c10aeffb44c4a3d7f5af395361f8 36fd4b70c12a4d69b7c78eb771025200 - - -] No weighed hosts found for volume with properties: {u'name': u'localfs', u'qos_specs_id': None, u'deleted': False, u'created_at': u'2021-06-02T04:43:54.000000', u'updated_at': None, u'extra_specs': {u'volume_backend_name': u'backend-1a1aebe3-be75'}, u'is_public': True, u'deleted_at': None, u'id': u'11165232-621a-4921-9d18-dcaeb274f6f9', u'description': u''}
2021-06-02 13:13:17.001 16629 ERROR cinder.scheduler.flows.create_volume [req-4ea1d276-73f4-4a12-88d6-631d983b0538 c0c8c10aeffb44c4a3d7f5af395361f8 36fd4b70c12a4d69b7c78eb771025200 - - -] Failed to run task cinder.scheduler.flows.create_volume.ScheduleCreateVolumeTask;volume:create: No valid host was found. No weighed hosts available

```

## 没有权限
```bash
     cmd=sanitized_cmd)
2021-06-02 13:01:28.515 272826 ERROR oslo_service.service ProcessExecutionError: Unexpected error while running command.
2021-06-02 13:01:28.515 272826 ERROR oslo_service.service Command: sudo cinder-rootwrap /etc/cinder/rootwrap.conf df --portability --block-size 1 /zettafs/mnt/6e1b4f290d46ce47cd1a212ed6bedf5a
2021-06-02 13:01:28.515 272826 ERROR oslo_service.service Exit code: 1

```

## 路径问题
```bash

2021-06-02 12:53:13.822 251627 ERROR cinder.volume.manager [req-b63cb4dc-727c-4f89-874c-e0a6002cebba - - - - -] Failed to initialize driver.
2021-06-02 12:53:13.822 251627 ERROR cinder.volume.manager Traceback (most recent call last):
2021-06-02 12:53:13.822 251627 ERROR cinder.volume.manager   File "/usr/lib/python2.7/site-packages/cinder/volume/manager.py", line 446, in init_host
2021-06-02 12:53:13.822 251627 ERROR cinder.volume.manager     self.driver.do_setup(ctxt)
2021-06-02 12:53:13.822 251627 ERROR cinder.volume.manager   File "/usr/lib/python2.7/site-packages/cinder/volume/drivers/local_fs.py", line 92, in do_setup
2021-06-02 12:53:13.822 251627 ERROR cinder.volume.manager     raise exception.GlusterfsException(msg)
2021-06-02 12:53:13.822 251627 ERROR cinder.volume.manager GlusterfsException: Gluster config file at /etc/cinder/glusterfs_shares doesn't exist
2021-06-02 12:53:13.822 251627 ERROR cinder.volume.manager
2021-06-02 12:53:13.849 251627 INFO cinder.volume.manager [req-b63cb4dc-727c-4f89-874c-e0a6002cebba - - - - -] Initializing RPC dependent components of volume driver GlusterfsDriver (1.3.0)
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service [req-b63cb4dc-727c-4f89-874c-e0a6002cebba - - - - -] Error starting thread.
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service Traceback (most recent call last):
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service   File "/usr/lib/python2.7/site-packages/oslo_service/service.py", line 680, in run_service
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service     service.start()
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service   File "/usr/lib/python2.7/site-packages/cinder/service.py", line 177, in start
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service     self.manager.init_host_with_rpc()
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service   File "/usr/lib/python2.7/site-packages/cinder/volume/manager.py", line 545, in init_host_with_rpc
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service     stats = self.driver.get_volume_stats(refresh=True)
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service   File "/usr/lib/python2.7/site-packages/cinder/volume/drivers/remotefs.py", line 504, in get_volume_stats
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service     self._update_volume_stats()
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service   File "/usr/lib/python2.7/site-packages/cinder/volume/drivers/local_fs.py", line 147, in _update_volume_stats
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service     super(GlusterfsDriver, self)._update_volume_stats()
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service   File "/usr/lib/python2.7/site-packages/cinder/volume/drivers/remotefs.py", line 523, in _update_volume_stats
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service     capacity, free, used = self._get_capacity_info(share)
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service   File "/usr/lib/python2.7/site-packages/cinder/volume/drivers/remotefs.py", line 803, in _get_capacity_info
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service     available, size = self._get_available_capacity(remotefs_share)
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service   File "/usr/lib/python2.7/site-packages/cinder/volume/drivers/remotefs.py", line 794, in _get_available_capacity
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service     run_as_root=self._execute_as_root)
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service   File "/usr/lib/python2.7/site-packages/cinder/utils.py", line 170, in execute
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service     return processutils.execute(*cmd, **kwargs)
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service   File "/usr/lib/python2.7/site-packages/oslo_concurrency/processutils.py", line 389, in execute
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service     cmd=sanitized_cmd)
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service ProcessExecutionError: Unexpected error while running command.
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service Command: sudo cinder-rootwrap /etc/cinder/rootwrap.conf df --portability --block-size 1 /var/lib/cinder/mnt/6e1b4f290d46ce47cd1a212ed6bedf5a
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service Exit code: 1
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service Stdout: u''
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service Stderr: u"/bin/df: '/var/lib/cinder/mnt/6e1b4f290d46ce47cd1a212ed6bedf5a': No such file or directory\n"
2021-06-02 12:53:13.963 251627 ERROR oslo_service.service

```