

# 制作好的 镜像 如果 有缺陷, 可以 利用这个 脚本 进行 微调 并 再次 制作
# img_id 代表 配置好 bond dhcp 的 虚机镜像,   
# 注意 制作 zcloud 第一个镜像时, 需要 将 两张 网卡 的 bond 设置 成为 BOOTPROTO=dhcp, 并注销 ip 以及 网关 等.
img_name='dhcp_leifeng'
flavor_name='zcloud_flavor'

vm_pwd='root@zetta'

# don't bigger than 90
vm_count="1"
sys_vol_size='100'

net_id='198'
net_name="ex${net_id}"
net_prefix="192.168.${net_id}"
vm_name_prefix="zcloud_kk_vol_${net_name}"

# must smaller then 100
if1_begin='5'
# 两张 网卡 的 ip 范围
# if1_range="${net_prefix}.10"
if1_range=`seq ${if1_begin} $[${if1_begin}+${vm_count}-1]`

. ~/admin-openrc
img_id=$(nova image-list | grep -i "${img_name}" | awk '{print $2}')
flavor_id=$(nova flavor-list | grep -i "${flavor_name}" | awk '{print $2}')

function create_vm(){
  idx=${1}
  nova boot --flavor ${flavor_id} --poll --block-device source=image,id=${img_id},dest=volume,size=${sys_vol_size},shutdown=remove,bootindex=0   --volume_type normal  --admin-pass ${vm_pwd}  --nic net-name=${net_name},v4-fixed-ip=${net_prefix}.${idx}   ${vm_name_prefix}_${idx} 
}

# 并发 创建 需要在关键步骤 等待
for  idx in ${if1_range}
do
  create_vm ${idx} &
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


