# rbd 镜像复制 迁移

# 介绍
就是 在 两个集群之间的，进行 镜像 数据的迁移。

# 使用
功能 挺复杂， 暂时用不到。
留个 url ，慢慢学 

https://docs.ceph.com/en/latest/rbd/rbd-mirroring/#rbd-mirroring

# 重要命令
## ENABLE MIRRORING 启用镜像功能
```bash
rbd mirror pool enable {pool-name} {mode}

rbd --cluster site-a mirror pool enable image-pool image
rbd --cluster site-b mirror pool enable image-pool image


```

## BOOTSTRAP PEERS 初始化 对等交换 守护程序
```bash

rbd mirror pool peer bootstrap create [--site-name {local-site-name}] {pool-name}

```

## DISABLE MIRRORING 关闭 镜像 功能
```bash

rbd mirror pool disable {pool-name}

rbd --cluster site-a mirror pool disable image-pool
rbd --cluster site-b mirror pool disable image-pool

```