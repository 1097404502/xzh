
vm_name_prefix='zcloud_kk'

. ~/admin-openrc
# 重启 虚机
nova list | grep -E "${vm_name_prefix}" | awk '{print $2}' | xargs -I {} nova reboot {} &
wait



