[toc]
# 当前 系统中 的 实现
存储 逻辑层次 多了一层 backends， 
在上游 中 数据库中 并不存在 backends ， 
backend_name 只是 volume-type 的一个 拓展属性。

所以 当前 在我们的 系统中，volume type 本身 需要做的 工作，都被 划分到了 backend 上边去。

# cluster 与 backend 的选择
两者 都 可以用来 实现 对接 不同的 ceph 存储。
同一个 cluster 可以用 多个 backend。

简单 来讲 cluster 是给了 为 不同的 进程 节点 分组，使用 相同 配置的 节点 划分为 同一个 cluster。

backends 为了 实现 单个 节点 使用 多个 存储集群。

在 单个节点 没有实现 连接 两个不同存储 驱动 的情况下， cluster 想要 使用 两个 存储 驱动。 就需要 两个 cluster 分别 采用 不同的 配置文件。


# 概念区分 cinder cluster ， cinder beckend 的区别

## cinder cluster
cinder cluster 只是个 逻辑概念。
每次 新建 volume invoke _ensure_cluster_exists 函数。
如果不存在 则在 数据库中根据 参数 新建 一个 cluster 对象。

同一个 配置文件 只能 指定一个 cluster 。
使用  相同的 cluster 字段 的 host 会组成 一个 高可用域。

官方 描述如下。
Name of this cluster. Used to group volume hosts that share the same backend  configurations to work in HA Active-Active mode.

db 中的 cluster 主要 包含了，sum_host 等 主机 数目 信息， 心跳 信息。 

## cinder backend
只存在于 配置文件 以及 作为 调用 传递的 参数。

1. 配置中定义 backends
```bash
enabled_backends=lvmdriver-1,lvmdriver-2,lvmdriver-3
[lvmdriver-1]
volume_group=cinder-volumes-1
volume_driver=cinder.volume.drivers.lvm.LVMVolumeDriver
volume_backend_name=LVM_iSCSI
[lvmdriver-2]
volume_group=cinder-volumes-2
volume_driver=cinder.volume.drivers.lvm.LVMVolumeDriver
volume_backend_name=LVM_iSCSI
[lvmdriver-3]
volume_group=cinder-volumes-3
volume_driver=cinder.volume.drivers.lvm.LVMVolumeDriver
volume_backend_name=LVM_iSCSI_b
```

2. 关联 type 与 backends
volume-type-1
```bash
openstack --os-username admin --os-tenant-name admin volume type create lvm

openstack --os-username admin --os-tenant-name admin volume type set lvm \
  --property volume_backend_name=LVM_iSCSI

```

volume-type-2
```bash
openstack --os-username admin --os-tenant-name admin volume type create lvm_gold

openstack --os-username admin --os-tenant-name admin volume type set lvm_gold \
  --property volume_backend_name=LVM_iSCSI_b

```
此时 
使用 volume type = lvm ，则会调用 driver = lvmdriver-[1|2]
使用 volume type = lvm_gold ，则会调用 driver = lvmdriver-3


db 中 是没有 这个 对象的。

