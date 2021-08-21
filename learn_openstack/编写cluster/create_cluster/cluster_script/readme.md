[toc]
# 脚本功能 介绍


## 001 
根据 上传的 iso 名称, 创建 第一台 虚机, 
安装 完成 之后, 
需要 创建 bond , 并且 编辑 bond 配置文件 修改为 dhcp , 注释掉 ip 以及 gateway

### 修改 bond 模式的 具体步骤
su - admin
分别给 两个 网卡 创建 bond , ip 以及 netmask 随便 填写 即可 1.1.1.1

修改 bond0  bond1 配置文件即可
```bash

cd /etc/sysconfig/network-scripts/
vi ifcfg-bond0
TYPE=Ethernet
NAME=bond0
DEVICE=bond0
ONBOOT=yes
BOOTPROTO=dhcp
BONDING_OPTS="mode=1 miimon=100 xmit_hash_policy=layer3+4"
# IPADDR=1.1.1.1
# NETMASK=1.1.1.1


```

修改 完成后, 需要 在 平台 中 系统 硬盘 中 制作镜像 ,
勾选强制 上传, 即可 在 私有镜像 中 看到 创建的 dhcpzcloud.iso

利用 创建的 镜像 之后 可以在 003 中 使用 该镜像 批量 创建虚机.


## 002
创建 集群 部署的 网络

## 003
根据 制作的 镜像 iso_name ,由于 已经 配置了 bond 为 dhcp
所以启动的 虚机 可以 直接 进入 zkeeper 平台 进行部署.

## 步骤
1. 修改 vi admin-openrc 为 admin
2. 修改 参数
3. 创建 虚机
4. 创建 并 挂在磁盘
5. 挂载 额外的 网卡

## 参数讲解
```bash

img_name     要启动的 镜像名称
flavor_name  要创建的 云主机 规格名称

vm_pwd       虚机密码, 需要 镜像 支持, 否则无效

vm_count     需要 创建的 虚机数目, 需要 小于 100 ,防止 ip 超出 255

echo_vm_vol_count   每个虚机 挂载的 硬盘数目
sys_vol_size        每个硬盘 的 大小 g

net_name            网络 名称
net_prefix          网络 前缀 x.x.x
vm_name_prefix      虚机名称 前缀

# must smaller then 100
if1_begin           第一块网卡 地址, 必须 小于 100, 因为 还要 挂在第二张网卡, 防止 进位后 超过 255,
              第一块网卡第一个ip = net_prefix.if1_begin
              第二块网卡第一个ip = net_prefix.if1_begin+100


```


## 004 
删除 虚机 以及 存储卷

## 005
删除 网络