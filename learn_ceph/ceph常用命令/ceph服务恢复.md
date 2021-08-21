# ceph 容器服务恢复

# 一条命令执行恢复 （你最好还是读读 为什么可以一条命令恢复 ceph 服务）
支持版本 ceph 15 + ，cephadm 自动部署
```bash

systemctl isolate multi-user.target 

```

## 前提条件
知晓 fsid
大部分文件未丢失


## 安装cephadm

完整步骤可以参考 官网，或者博主的 其他 ceph 系列博客
cephadm 依赖 python36 ，
安装时，请打开代理工具
```bash

curl --silent --remote-name --location https://github.com/ceph/ceph/raw/octopus/src/cephadm/cephadm

chmod +x cephadm

./cephadm --help

./cephadm add-repo --release octopus
./cephadm install

```

## 查看ceph 服务依赖
```bash
systemctl list-dependencies ceph.target

ceph.target
● └─ceph-2aa7de1c-497a-11eb-b926-fa163e717f07.target
●   ├─ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@alertmanager.host-192-168-141-20.service
●   ├─ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@crash.host-192-168-141-20.service
●   ├─ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@grafana.host-192-168-141-20.service
●   ├─ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@mds.my_fs.host-192-168-141-20.mcwtpb.service
●   ├─ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@mgr.host-192-168-141-20.fsdiay.service
●   ├─ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@mon.host-192-168-141-20.service
●   ├─ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@node-exporter.host-192-168-141-20.service
●   ├─ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@osd.0.service
●   └─ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@prometheus.host-192-168-141-20.service

保证整个ceph 下尽量只有一个集群配置。
如果存在多余的 ceph 服务， 可以通过 cephadm 进行删除

```

## 删除多余的集群 (可选)



博主一开始不太会使用， 多次执行了 cephadm bootstrap 指令，创建了 多个 ceph 服务
只保留一个集群

```bash

# rm--cluster 会删除
# /var/lib/ceph/<fsid>
# /var/log/ceph/<fsid>
# /etc/systemd/system/*<fsid>*
# 并且移除多余的 正在运行  docker 容器
cephadm rm-cluster --fsid dc05693c-48bb-11eb-84da-fa163e717f07 --force

# 删除之后可以确认一下
ls  /var/lib/ceph/
2aa7de1c-497a-11eb-b926-fa163e717f07

ls  /var/log/ceph/
2aa7de1c-497a-11eb-b926-fa163e717f07

ls  /etc/systemd/system/
。。。。。

docker ps
。。。。

```


## 一条命令执行恢复 ***
```bash

systemctl isolate multi-user.target 

```

## systemctl 恢复命令 解读

### 什么是 systemctl taget 以及 want 

systemctl 中包含 以下概念
systemctl  service
systemctl  unit
systemctl  want
systemctl  target
多个 service 组成 unit
unit 可以被 其他unit 依赖 形成
unit_1 target unit_2
然后 具体的 want 关系又会存放在 相应的 wants 目录中 



### ceph 启动解读

```bash

systemctl isolate multi-user.target 
真实作用是 切换 linux 操作系统的 工作模式

我们的服务器运行在 多用户 无界面模式。

cephadm bootstrap 集群的时候，会在 /etc/systemd/system 下安装 ceph 集群自启动服务

cat /etc/systemd/system/ceph.target

[Unit]
Description=All Ceph clusters and services

[Install]
WantedBy=multi-user.target

***
文件的意思 就是 ceph.target 依赖于 多用户启动 target
所以我们 重新加载 多用户模式的同时。 也会去重新加载 ceph 的集群服务。

/etc/systemd/system/ceph.target 会去遍历 相应的 wants 目录
-->
ls  /etc/systemd/system/ceph.target.wants
ceph-2aa7de1c-497a-11eb-b926-fa163e717f07.target

相应的 ceph-2aa7de1c-497a-11eb-b926-fa163e717f07.target 又会去遍历 对应的 want 目录
--> 
ls /etc/systemd/system/ceph-2aa7de1c-497a-11eb-b926-fa163e717f07.target.wants
ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@alertmanager.host-192-168-141-20.service      ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@mon.host-192-168-141-20.service
ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@crash.host-192-168-141-20.service             
 ..................



```

### 我们也可以通过 依赖搜索命令 直接 查看 ceph.target 将会 启动的 所有服务
```bash

systemctl list-dependencies ceph.target
-->
ceph.target
● └─ceph-2aa7de1c-497a-11eb-b926-fa163e717f07.target
●   ├─ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@alertmanager.host-192-168-141-20.service
●   ├─ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@crash.host-192-168-141-20.service
●   ├─ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@grafana.host-192-168-141-20.service
●   ├─ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@mds.my_fs.host-192-168-141-20.mcwtpb.service
●   ├─ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@mgr.host-192-168-141-20.fsdiay.service
●   ├─ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@mon.host-192-168-141-20.service
●   ├─ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@node-exporter.host-192-168-141-20.service
●   ├─ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@osd.0.service
●   └─ceph-2aa7de1c-497a-11eb-b926-fa163e717f07@prometheus.host-192-168-141-20.service


```