[toc]
# 步骤
1. 修改 vi admin-openrc 为 admin
2. 修改 参数
3. 创建 虚机
4. 创建 并 挂在磁盘
5. 挂载 额外的 网卡

# 参数讲解
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

# 批量创建 zcloud  搭建集群
修改 前几行 参数后, 直接 粘贴到 宿主机 shell 执行即可

```bash

# img_id 代表 配置好 bond dhcp 的 虚机镜像,   
# 注意 制作 zcloud 第一个镜像时, 需要 将 两张 网卡 的 bond 设置 成为 BOOTPROTO=dhcp, 并注销 ip 以及 网关 等.
img_name='dhcp_leifeng'
flavor_name='zcloud_flavor'

vm_pwd='root@zetta'

# don't bigger than 90
vm_count="5"
echo_vm_vol_count="3"
sys_vol_size='100'

net_name='ex199'
net_prefix="192.168.199"
vm_name_prefix="zcloud_kk_${net_name}"

# must smaller then 100
if1_begin='11'
# 两张 网卡 的 ip 范围
# if1_range="${net_prefix}.10"
if1_range=`seq ${if1_begin} $[${if1_begin}+${vm_count}-1]`

virtual_ip="${net_prefix}.250"

. ~/admin-openrc
img_id=$(nova image-list | grep -i "${img_name}" | awk '{print $2}')
flavor_id=$(nova flavor-list | grep -i "${flavor_name}" | awk '{print $2}')

function create_vm(){
  idx=${1}
  nova boot --flavor ${flavor_id} --poll --block-device source=image,id=${img_id},dest=volume,size=${sys_vol_size},shutdown=remove,bootindex=0   --volume_type normal  --admin-pass ${vm_pwd}  --nic net-name=${net_name},v4-fixed-ip=${net_prefix}.${idx}   ${vm_name_prefix}_${idx} 
}

# 并发 创建 似乎 会出错
for  idx in ${if1_range}
do
  create_vm ${idx} &
done
wait


# 为 虚机 挂载 存储盘
function bind_vol(){
  vol_name=${1}
  vm_id=${2}
  vol_id=$( cinder create --volume-type  ${vol_type}  --name ${vol_name}  100 | grep ' id ' | awk '{print $4}' )
  nova volume-attach ${vm_id}  ${vol_id}
}

vol_type='normal'
for  idx in ${if1_range}
do
   tmp_vm="${vm_name_prefix}_${idx}"
   tmp_vm_id=$(  nova list | grep ${tmp_vm} | awk '{print $2}' )
   for vol_idx in `seq 1 ${echo_vm_vol_count}` 
     do
        vol_name="${tmp_vm}_${vol_idx}"
        bind_vol  ${vol_name}  ${tmp_vm_id} &
     done
done
wait

# 为虚机 挂在 网卡
net_id=$( nova 'net-list' | grep "${net_name}" | awk '{print $2}' )

function bind_if(){
    nova interface-attach ${1} --net-id ${net_id} --fixed-ip ${2}
}

for idx in ${if1_range}
do
   bind_if ${vm_name_prefix}_${idx}   ${net_prefix}.$[${idx}+100] &
done
wait

# 放行 虚ip,  为  机器 绑定 虚 ip
neutron port-list | grep -E ${net_prefix}  | awk '{print $2}' | xargs -I {} neutron port-update {} --allowed-address-pair ip_address=${virtual_ip} 

function reboot_vm(){
  nova reboot ${1}
}

# 生效新 绑定 网卡 dhcp
for idx in ${if1_range}
do
  reboot_vm ${vm_name_prefix}_${idx}  &
done
wait



```

## 根据 正则 删除 虚拟机
```bash

vm_name_prefix='zcloud_kk'

. ~/admin-openrc
# 删除 虚机
nova list | grep -E "${vm_name_prefix}" | awk '{print $2}' | xargs -I {} nova force-delete {} &
wait

# 删除 存储卷
cinder list | grep -E  "${vm_name_prefix}" | awk '{print $2}' | xargs -I {}  cinder force-delete {} &
wait



# 为什么 有的 {} 有的没有呢?
# 因为 指令 如果支持 跟随 变长 参数, 比如 cinder delete ..... 多个 volume , 那么 就不需要 {}
# 如果 指令本身 并不支持 多个 变长参数, 那么 需要 指定 {} 来进行 换行切分

```


## 修改 存储 池 size  (除开发 测试环境 慎用, 因为 嵌套 三副本, 太吃 磁盘了....)
正常 环境 部署 禁止了 单副本 .
```bash

# 并发执行

default_size='1'

function set_pool_size(){
  ceph osd pool  set ${1} ${2} ${default_size} 
}

for _p in `ceph osd pool ls`
do
  for var_name in 'size' 'min_size'
  do 
    set_pool_size ${_p} ${var_name} &
  done
done
wait

```

## 修改 admin-openrc
并在 平台上 调整配额.  防止 创建磁盘 等 资源时 失败.
```bash
cat ~/admin-openrc
export OS_PROJECT_DOMAIN_NAME=default
export OS_USER_DOMAIN_NAME=default
export OS_PROJECT_NAME=project1
export OS_TENANT_NAME=default
export OS_USERNAME=admin
export OS_PASSWORD=admin_pass
export OS_AUTH_URL=http://192.168.66.1:35357/v3
export OS_IDENTITY_API_VERSION=3
export OS_VOLUME_API_VERSION=2

```


## 添加网卡
```bash

nova help interface-attach

Positional arguments:
  <server>               Name or ID of server.

Optional arguments:
  --port-id <port_id>    Port ID.
  --net-id <net_id>      Network ID
  --fixed-ip <fixed_ip>  Requested fixed IP.

```
