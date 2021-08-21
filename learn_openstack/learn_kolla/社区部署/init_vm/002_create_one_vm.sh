
# kk 网盘中的 ubuntu  docker 
img_name='docker_ubuntu'
flavor_name='zcloud_flavor'

vm_pwd='root'

# don't bigger than 90
vm_count="1"
echo_vm_vol_count="2"
sys_vol_size='100'
each_vol_size='100'

net_id='199'
net_name="ex${net_id}"
net_prefix="192.168.${net_id}"
vm_name_prefix="openstack_v_kk_${net_name}"

# must smaller then 100
if1_begin='10'
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





