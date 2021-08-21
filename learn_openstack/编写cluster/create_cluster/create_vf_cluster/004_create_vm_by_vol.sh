

# img_id 代表 配置好 bond dhcp 的 虚机镜像,   
# 注意 制作 zcloud 第一个镜像时, 需要 将 两张 网卡 的 bond 设置 成为 BOOTPROTO=dhcp, 并注销 ip 以及 网关 等.
img_name='zcloud'
flavor_name='zcloud_flavor'

vm_pwd='root@zetta'

# don't bigger than 90
vm_count="1"
echo_vm_vol_count="3"
sys_vol_size='100'
each_vol_size='100'

net_id='199'
net_name="ex${net_id}"
net_prefix="192.168.${net_id}"
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

# 并发 创建 需要在关键步骤 等待
for  idx in ${if1_range}
do
  create_vm ${idx} &
done
wait


# 为 虚机 挂载 存储盘
function bind_vol(){
  vol_name=${1}
  vm_id=${2}
  vol_id=$( cinder create --volume-type  ${vol_type}  --name ${vol_name}  ${each_vol_size} | grep ' id ' | awk '{print $4}' )
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



# 删除 网卡 之后 需要 自行 添加 sr iov 网卡
# 删除掉 所有 网卡 之后 就 看不到 vnc 了
function clear_if(){
  
    function detach_if(){
      nova  interface-detach  ${1} ${2}
    }

    vm_name=${1}
    port_id=$( nova interface-list ${1} | awk '{print $4}' | grep -oE '[a-z0-9-]{10,}' )
    
    for i in $port_id
    do
       detach_if ${1} ${i} &
    done
}

for idx in ${if1_range}
do
   clear_if ${vm_name_prefix}_${idx} &
done
wait




