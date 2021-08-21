# 代码修改
```bash
root@DESKTOP-DMNTO28:~/my_proj/cinder# grep 'kill_cinder_volume_auto' -r ./
./cinder/volume/backends.py:                volume_rpcapi.kill_cinder_volume_auto(context, service.host,
./cinder/volume/rpcapi.py:    def kill_cinder_volume_auto(self, ctxt, host, backend, stor_pool):
./cinder/volume/rpcapi.py:        cctxt.cast(ctxt, 'kill_cinder_volume_auto',
Binary file ./cinder/volume/manager.pyc matches
./cinder/volume/manager.py:    def kill_cinder_volume_auto(self, ctxt, backend, stor_pool):


grep 'check_backend_auto_process' -r ./

```

# rpc 调用
```bash

def launch_cinder_volume(self, ctxt, host, backend, stor_pool):
   cctxt = self._get_cctxt(host, '2.0')
   cctxt.cast(ctxt, 'launch_cinder_volume',
               backend=backend, stor_pool=stor_pool)
               
```


#  创建一个 后端 存储 并且 创建 虚拟机 之后 
之前 有几个 存储 进程，
就会 双倍 翻， 直到 重启 cinder-volume- 服务 才会 还原成 两个。。 

```bash
[root@node01 ~]# systemctl status openstack-cinder-volume.service  -l
● openstack-cinder-volume.service - OpenStack Cinder Volume Server
   Loaded: loaded (/usr/lib/systemd/system/openstack-cinder-volume.service; enabled; vendor preset: disabled)
   Active: active (running) since Mon 2021-04-26 21:17:09 CST; 10min ago
 Main PID: 13105 (cinder-volume)
    Tasks: 133
   Memory: 862.5M
   CGroup: /system.slice/openstack-cinder-volume.service
           ├─13105 /usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/volume.log
           ├─13501 /usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/fast_backend-a9499bc1-903c/cinder.conf --logfile /etc/cinder/fast_backend-a9499bc1-903c/backend.log --backend backend-a9499bc1-903c --stor_pool fastpool --run_subproc
           ├─13502 /usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/normal_backend_0000/cinder.conf --logfile /etc/cinder/normal_backend_0000/backend.log --backend backend_0000 --stor_pool volumes --run_subproc
           ├─13503 /usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/performance_backend-688b754b-6e4a/cinder.conf --logfile /etc/cinder/performance_backend-688b754b-6e4a/backend.log --backend backend-688b754b-6e4a --stor_pool fastpool --run_subproc
           ├─13761 /usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/fast_backend-a9499bc1-903c/cinder.conf --logfile /etc/cinder/fast_backend-a9499bc1-903c/backend.log --backend backend-a9499bc1-903c --stor_pool fastpool --run_subproc
           ├─13762 /usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/performance_backend-688b754b-6e4a/cinder.conf --logfile /etc/cinder/performance_backend-688b754b-6e4a/backend.log --backend backend-688b754b-6e4a --stor_pool fastpool --run_subproc
           ├─13763 /usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/normal_backend_0000/cinder.conf --logfile /etc/cinder/normal_backend_0000/backend.log --backend backend_0000 --stor_pool volumes --run_subproc
           ├─49827 /usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/fast2_backend-01e77ece-fc92/cinder.conf --logfile /etc/cinder/fast2_backend-01e77ece-fc92/backend.log --backend backend-01e77ece-fc92 --stor_pool fastpool --run_subproc
           ├─49828 /usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/fast2_backend-01e77ece-fc92/cinder.conf --logfile /etc/cinder/fast2_backend-01e77ece-fc92/backend.log --backend backend-01e77ece-fc92 --stor_pool fastpool --run_subproc
           ├─49829 /usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/fast2_backend-01e77ece-fc92/cinder.conf --logfile /etc/cinder/fast2_backend-01e77ece-fc92/backend.log --backend backend-01e77ece-fc92 --stor_pool fastpool --run_subproc
           ├─49883 /usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/fast2_backend-01e77ece-fc92/cinder.conf --logfile /etc/cinder/fast2_backend-01e77ece-fc92/backend.log --backend backend-01e77ece-fc92 --stor_pool fastpool --run_subproc
           ├─49884 /usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/fast2_backend-01e77ece-fc92/cinder.conf --logfile /etc/cinder/fast2_backend-01e77ece-fc92/backend.log --backend backend-01e77ece-fc92 --stor_pool fastpool --run_subproc
           └─49887 /usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/fast2_backend-01e77ece-fc92/cinder.conf --logfile /etc/cinder/fast2_backend-01e77ece-fc92/backend.log --backend backend-01e77ece-fc92 --stor_pool fastpool --run_subproc
```