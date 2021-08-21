# rbd 创建 磁盘 并 格式化 xfs 并 挂载


```bash

rbd create --size $[1024*1024] fastpool/images



rbd feature disable fastpool/images object-map fast-diff deep-flatten
rbd map fastpool/images

mkfs.xfs /dev/rbd0

mkdir -p /images

mount /dev/rbd0  /images


```

# 查看 挂载结果
```bash

rbd info fastpool/images

-->
  rbd image 'images':
        size 1024 GB in 262144 objects
        order 22 (4096 kB objects)
        block_name_prefix: rbd_data.ec4cc6b8b4567
        format: 2
        features: layering, exclusive-lock
        flags:


df -h
-->  
   /dev/rbd0       1.0T   34M  1.0T   1% /images

```

# 使用1 ： 导出 vm
```bash
# 填写 导出的 虚机名称 ， 以及 要上传的 镜像名称
image_path="/images/centos7_pip_hub.qcow2"
vm_name='register'

inner_ip='192.168.63.100'
script_path='/root/sp/pack_and_download_vm_by_name.sh'


script_name=${script_path##*/}
mkdir -p ${script_path%/*}

curl -u admin:brysjhhrhl356126155165352237656123565615 -o ${script_path}  http://${inner_ip}:50000/remote.php/webdav/common_script/${script_name}

chmod +x -R ${script_path}




image_name=${image_path##*/}
mkdir -p ${image_path%/*}


nohup ${script_path}  "${vm_name}" "${image_path}" 2>&1 > ./revert.log &

nohup curl  --progress-bar -o ./progress.log -u admin:brysjhhrhl356126155165352237656123565615 -T ${image_path} "http://${inner_ip}:50000/remote.php/dav/files/admin/iso/${image_name}" 2>&1  > ./upload_centos7.log &


```