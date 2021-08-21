
vm_name_prefix='zcloud_kk_197'

. ~/admin-openrc
# 删除 虚机
nova list | grep -E "${vm_name_prefix}" | awk '{print $2}' | xargs -I {} nova force-delete {} &
wait

# 删除 存储卷
cinder list | grep -E  "${vm_name_prefix}" | awk '{print $2}' | xargs -I {}  cinder force-delete {} &
wait




