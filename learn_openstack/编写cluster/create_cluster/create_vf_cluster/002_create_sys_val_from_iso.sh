

# img_id 代表 配置好 bond dhcp 的 虚机镜像,   
# 注意 制作 zcloud 第一个镜像时, 需要 将 两张 网卡 的 bond 设置 成为 BOOTPROTO=dhcp, 并注销 ip 以及 网关 等.
img_name='zcloud31'
flavor_name='zcloud_flavor'

vm_pwd='root@zetta'

# don't bigger than 90
vm_count="1"
sys_vol_size='100'

net_id='164'
net_name="ex${net_id}"
net_prefix="192.168.${net_id}"
vm_name_prefix="zcloud_kk_iso_${net_name}"

# must smaller then 100
if1_begin='5'
# 两张 网卡 的 ip 范围
# if1_range="${net_prefix}.10"
if1_range=`seq ${if1_begin} $[${if1_begin}+${vm_count}-1]`

. ~/admin-openrc
img_id=$(nova image-list | grep -i " ${img_name} " | awk '{print $2}')
flavor_id=$(nova flavor-list | grep -i " ${flavor_name} " | awk '{print $2}')

function create_vm(){
  idx=${1}
  nova boot --flavor ${flavor_id}   --image ${img_id}  --poll  --block-device source=blank,dest=volume,size=${sys_vol_size},shutdown=remove  --volume_type normal  --admin-pass ${vm_pwd}  --nic net-name=${net_name},v4-fixed-ip=${net_prefix}.${idx}   ${vm_name_prefix}_${idx} 
}

# 并发 创建 需要在关键步骤 等待
for  idx in ${if1_range}
do
  create_vm ${idx} &
done
wait




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

# 
# detach-usb                  Detach a network interface from a server.
# interface-attach            Attach a network interface to a server.
# interface-detach            Detach a network interface from a server.
# interface-list              List interfaces attached to a server.


#  nova help interface-detach
# usage: nova interface-detach <server> <port_id>

# Detach a network interface from a server.

# Positional arguments:
#   <server>   Name or ID of server.
#   <port_id>  Port ID.
