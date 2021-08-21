# 搜索启动文件

```bash

find / -name  "*ceph-2aa7de1c-497a-11eb-b926-fa163e717f07*" 
/sys/fs/cgroup/systemd/system.slice/system-ceph\x2d2aa7de1c\x2d497a\x2d11eb\x2db926\x2dfa163e717f07.slice/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@mds.my_fs.host-192-168-141-20.mcwtpb.service
/sys/fs/cgroup/systemd/system.slice/system-ceph\x2d2aa7de1c\x2d497a\x2d11eb\x2db926\x2dfa163e717f07.slice/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@osd.0.service
/sys/fs/cgroup/systemd/system.slice/system-ceph\x2d2aa7de1c\x2d497a\x2d11eb\x2db926\x2dfa163e717f07.slice/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@prometheus.host-192-168-141-20.service
/sys/fs/cgroup/systemd/system.slice/system-ceph\x2d2aa7de1c\x2d497a\x2d11eb\x2db926\x2dfa163e717f07.slice/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@alertmanager.host-192-168-141-20.service
/sys/fs/cgroup/systemd/system.slice/system-ceph\x2d2aa7de1c\x2d497a\x2d11eb\x2db926\x2dfa163e717f07.slice/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@grafana.host-192-168-141-20.service
/sys/fs/cgroup/systemd/system.slice/system-ceph\x2d2aa7de1c\x2d497a\x2d11eb\x2db926\x2dfa163e717f07.slice/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@node-exporter.host-192-168-141-20.service
/sys/fs/cgroup/systemd/system.slice/system-ceph\x2d2aa7de1c\x2d497a\x2d11eb\x2db926\x2dfa163e717f07.slice/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@crash.host-192-168-141-20.service
/sys/fs/cgroup/systemd/system.slice/system-ceph\x2d2aa7de1c\x2d497a\x2d11eb\x2db926\x2dfa163e717f07.slice/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@mgr.host-192-168-141-20.fsdiay.service
/sys/fs/cgroup/systemd/system.slice/system-ceph\x2d2aa7de1c\x2d497a\x2d11eb\x2db926\x2dfa163e717f07.slice/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@mon.host-192-168-141-20.service
/etc/logrotate.d/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07
/etc/systemd/system/multi-user.target.wants/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07.target
/etc/systemd/system/ceph.target.wants/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07.target
/etc/systemd/system/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07.target
/etc/systemd/system/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@.service
/etc/systemd/system/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07.target.wants
/etc/systemd/system/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07.target.wants/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@mon.host-192-168-141-20.service
/etc/systemd/system/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07.target.wants/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@mgr.host-192-168-141-20.fsdiay.service
/etc/systemd/system/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07.target.wants/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@alertmanager.host-192-168-141-20.service
/etc/systemd/system/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07.target.wants/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@crash.host-192-168-141-20.service
/etc/systemd/system/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07.target.wants/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@grafana.host-192-168-141-20.service
/etc/systemd/system/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07.target.wants/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@node-exporter.host-192-168-141-20.service
/etc/systemd/system/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07.target.wants/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@prometheus.host-192-168-141-20.service
/etc/systemd/system/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07.target.wants/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@osd.0.service
/etc/systemd/system/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07.target.wants/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@mds.my_fs.host-192-168-141-20.mcwtpb.service


```
# docker 加速
```bash

sudo docker login --username=漱石者枕夏目 registry.cn-hangzhou.aliyuncs.com

sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://wm12hkla.mirror.aliyuncs.com"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker


```

# 尝试恢复一个 cephadm 集群
```bash
恢复集群，首先需要确保
/etc/systemd/system 下有相应的启动文件

ls /etc/systemd/system
basic.target.wants                                      ceph-2aa7de1c-497a-11eb-b926-fa163e717f07.target.wants  dbus-org.freedesktop.nm-dispatcher.service  network-online.target.wants
ceph-1064116e-4976-11eb-b4ae-fa163e717f07@.service      ceph-dc05693c-48bb-11eb-84da-fa163e717f07@.service      default.target                              sockets.target.wants
ceph-1064116e-4976-11eb-b4ae-fa163e717f07.target        ceph-dc05693c-48bb-11eb-84da-fa163e717f07.target        default.target.wants                        sysinit.target.wants
ceph-1064116e-4976-11eb-b4ae-fa163e717f07.target.wants  ceph-dc05693c-48bb-11eb-84da-fa163e717f07.target.wants  getty.target.wants                          system-update.target.wants
ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@.service      ceph.target                                             local-fs.target.wants
ceph-2aa7de1c-497a-11eb-b926-fa163e717f07.target        ceph.target.wants    

ls /var/lib/ceph
1064116e-4976-11eb-b4ae-fa163e717f07  2aa7de1c-497a-11eb-b926-fa163e717f07  dc05693c-48bb-11eb-84da-fa163e717f07

问题在于 有三个集群的配置文件，把多余的删掉
先安装 cephadm
cephadm rm-cluster --fsid dc05693c-48bb-11eb-84da-fa163e717f07 --force
cephadm rm-cluster --fsid 1064116e-4976-11eb-b4ae-fa163e717f07 --force


# 列出所有的 ceph 服务依赖
systemctl list-dependencies ceph.target

systemctl list-dependencies  multi-user.target 



# 不重启机器，切换运行状态， 
# 此步骤可以将 multi-user.target  下的所有依赖 target 全部重启
systemctl isolate multi-user.target 

```


