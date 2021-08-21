#!/bin/bash

vm_name=$1

save_path=$2

# 存储信息
volume_info=''
volume_id=''
volume_type="normal"
volume_path=''

# 确保导出的是 启动盘
is_bootable='true'

function check_input(){
  if [ "$vm_name" = '-h' ] ||  [ "$vm_name" = '--help' ]  ||  [ "$vm_name" = 'help' ] || [ "$vm_name" = '' ]
  then 
    echo 'USAGE:'
    echo './pack_and_download_vm_by_name.sh  <vm_name>  <download_save_path> '
    echo -e '\n请确保 磁盘 空间 充足, 避免 系统盘 爆盘\n'
    echo -e 'demo1: \n  仅测试导出是否正常执行 \n ./pack_and_download_vm_by_name.sh "kk开发" "/images/centos7_docker.qcow2"\n'
    echo -e 'demo2: \n  推荐的 导出方式       \n nohup /root/sp/pack_and_download_vm_by_name.sh  "kk开发" "/images/centos7_docker.qcow2" 2>&1 > ./revert.log & \n\n'
    echo -e '后台 执行时 查看 导出 进度:\n  查看 导出 进程 pid \nps -aux | grep "/pack_and_download_vm_by_name.sh"  \n   根据 pid 查看 导出 进度 \n tail -f /proc/<pid>/fd/1'
    exit 1
  fi

  if [ "$save_path" = '' ]
  then 
    echo '保存路径 不能为空'
    echo '第2个 参数 为 存储路径 建议 绝对路径'
    exit 1
  fi
}
check_input

function trim(){
  echo "trim  $1"
  $1=$(echo "$1" )
}

function get_volume_path_by_vm_name(){
. /root/admin-openrc
vm_id=$(nova list --all-tenants 1 | grep " ${vm_name} " | awk '{print $2}')

# | 83544c25-e9a5-4a0f-879d-db28ebe2f5fc | 91094a59edab496a8dca7e25196e41cd |   in-use  |                                                |  80  | performance |   true   | 6502cbcb-38fb-4b17-be12-d968b2e0d774 |    True    |
# volume_info=$(cinder list --all-tenants 1 | grep -E "${is_bootable}.*${vm_id}")
volume_info=$(cinder list --all-tenants 1 | grep "${vm_id}")


volume_id=$(echo "$volume_info"  | awk  '{print $2}' | grep -oE "[a-zA-Z0-9-]+"  )
volume_type=$(echo "$volume_info" | awk -F '|' '{print $7}' | grep -oE "[a-zA-Z0-9-]+")


volume_path="volume-${volume_id}"
if [ "$volume_type" = 'normal' ]
then
  volume_path="volumes/${volume_path}"
elif [  "$volume_type" = 'performance' ]
then
  volume_path="fastpool/${volume_path}"
fi



}

get_volume_path_by_vm_name


function download_img(){
  echo "导出的rbd image path:  $volume_path"
  echo '建议 nohup  & 执行 导出, 否则 连接 中断，导出 进程 会 失败'
  \rm ${save_path}
  qemu-img convert rbd:${volume_path} -c -p -O qcow2 ${save_path}
}

download_img

