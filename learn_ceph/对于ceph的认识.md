# 几种ceph组件
## monitor 监视器
ceph mon 负责监视系统状态，以及各种映射
包含，mon 映射，man映射 ， osd 映射，mds 映射，以及 crush 映射

mon 监视器还会负责 守护程序和 客户端之间的身份验证。
通常至少需要 三个以上的mon 来实现 冗余和高可用。 

## manager 管理器

ceph man 负责管理系统利用率，当前指标性能，以及系统负载。
同时负责使用python 管理以及 公开集群信息
（比如 提供给 dashboard）以及 提供给 rest api 接口使用。

最少建议两台 man

## object storge daemon 

ceph osd 负责数据存储，处理数据的复制，以及 重新平衡。
并通过检查其他的 osd 守护进程的心跳向管理器提供一些监视信息。

最少需要3个osd

## metadata server

ceph mds 代表ceph 文件系统存储元数据(cfs) 服务。 

**块存储 rbd 以及 对象存储 rgw 并不需要这个服务

ceph元数据服务器允许 posix 用户执行基本的 ls find 等命令 而不会给集群带来较大负担。

## rgw
rados 网关（Reliable, Autonomic Distributed Object Store）。
又被称作 ceph 网关 gateway。

# 存储单位概念

## ceph 对象
ceph 将所有的 data 抽象为对象，对象的数量很多，并不是ceph 进行调度的最小单元。
每个对象只能属于 一个 pg

## placement group 放置策略组
他是众多对象的集合。相同的 pg 会放置在相同的主机
每个pg 只能属于一个 pool

## pool 存储池
每个存储池规定了，数据存储的 类型，以及 对应的副本的分部策略。
比如，按照副本存储，还是按照纠删码存储。


## pg_num 
number of placement groups mapped to an OSD

## PGP 
Placement Group for Placement purpose

## 存储逻辑
ceph 会将 数据 作为对象， 存储在 逻辑存储 池 之中。
之后在通过 crush 算出 每个对象 可能在 哪个placement group中。
再进一步计算出 这个 placement group 存在于 那一个 osd 服务中。

crush 算法使得，ceph 可以动态的 扩容以及再平衡 和恢复。

# ceph 应用

## ceph 文件存储服务

提供分布式的文件存储

## ceph 块存储服务

分布式块存储，提供给 vm 虚机使用最合适。

## ceph 对象存储服务

ceph 将所用数据抽象成 对象进行存储
