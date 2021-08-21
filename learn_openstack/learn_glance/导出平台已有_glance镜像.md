# 根据 镜像 名称 导出 镜像

```bash

pool='volumes'

image_name='win10GPU'

rbd_block_id="$( glance image-list | grep -i " ${image_name} " | awk '{ print $2 }' )"
img_name="win10GPU.qcow2"

rm -rf ./image
mkdir -p image

cd image

# -m n 并发数   -W 允许 非顺序 写入, 与压缩 选项 -c 不可同时 使用
# time qemu-img convert -m 16  rbd:${pool}/${rbd_block_id} -c -p -O qcow2 ./${img_name}

nohup qemu-img convert -m 16   rbd:${pool}/${rbd_block_id} -c -p -O qcow2 ./${img_name} 2>&1 > convert.log &


# 上传
f_path=${img_name}
f_name=${f_path##*/}
inner_ip='192.168.63.100'
curl  --progress-bar -o ./progress.log -u admin:brysjhhrhl356126155165352237656123565615 -T ${f_path} "http://${inner_ip}:50000/remote.php/dav/files/admin/iso/${f_name}"


# 及时清空防止系统盘 被占满
rm -rf ./*


```










# 导出镜像 并提供下载 连接
```bash


mkdir -p /root/images && . /root/admin-openrc && glance image-list | grep -E '[a-z0-9]{6,}' | awk '{print "glance    image-download  --progress  --file  /root/images/" $4 "  "  $2  }'  |  xargs  -I {}  /bin/bash -c "{}"

# 提供 http 下载
cd /root/images 
nohup python -m SimpleHTTPServer 50000 2>&1 > ./py_server.log &

ssh root@192.168.64.2 "mkdir -p /root/images/"

# 2 选 1
scp -r /root/images/win10GPU root@192.168.64.2:/root/images

rsync -a -v -e ssh -P  --exclude='*.pyc'  --exclude='*.log'   /root/images/win10GPU0325 root@192.168.64.2:/root/images/



usage: glance image-upload [--file <FILE>] [--size <IMAGE_SIZE>] [--progress]
                           <IMAGE_ID>

glance image-upload  --file /root/images/win10GPU  --size 40 --progress  win1

cinder  create --image-id win1  --is_sys_vol true  40



```

# glance 同时 导出 大镜像时 网络 会变得 很卡


# 查看 并下载 所有镜像

```bash


mkdir -p /root/images ; . admin-openrc; glance image-list | grep -E '[a-z0-9]{6,}' | awk '{print "glance    image-download  --progress  --file  /root/images/" $4 "  "  $2  }'  |  xargs  -d \n  -I {}  /bin/bash -c "{}"

**************************************************************************************
glance help image-download
usage: glance image-download [--file <FILE>] [--progress] <IMAGE_ID>

Download a specific image.

Positional arguments:
  <IMAGE_ID>     ID of image to download.

Optional arguments:
  --file <FILE>  Local file to save downloaded image data to. If this is not
                 specified and there is no redirection the image data will be
                 not be saved.
  --progress     Show download progress bar.

***************************************************************************************

glance help image-upload
usage: glance image-upload [--file <FILE>] [--size <IMAGE_SIZE>] [--progress]
                           <IMAGE_ID>

Upload data for a specific image.

Positional arguments:
  <IMAGE_ID>           ID of image to upload data to.

Optional arguments:
  --file <FILE>        Local file that contains disk image to be uploaded.
                       Alternatively, images can be passed to the client via
                       stdin.
  --size <IMAGE_SIZE>  Size in bytes of image to be uploaded. Default is to
                       get size from provided data object but this is
                       supported in case where size cannot be inferred.
  --progress           Show upload progress bar.

************************************************************************

 glance help image-create
usage: glance image-create [--architecture <ARCHITECTURE>]
                           [--protected [True|False]] [--name <NAME>]
                           [--instance-uuid <INSTANCE_UUID>]
                           [--min-disk <MIN_DISK>] [--visibility <VISIBILITY>]
                           [--kernel-id <KERNEL_ID>]
                           [--tags <TAGS> [<TAGS> ...]]
                           [--os-version <OS_VERSION>]
                           [--disk-format <DISK_FORMAT>]
                           [--os-distro <OS_DISTRO>] [--id <ID>]
                           [--owner <OWNER>] [--ramdisk-id <RAMDISK_ID>]
                           [--min-ram <MIN_RAM>]
                           [--container-format <CONTAINER_FORMAT>]
                           [--property <key=value>] [--file <FILE>]
                           [--progress]


mkdir -p /root/images ; . admin-openrc; glance image-list | grep -E '[a-z0-9]{6,}' | awk '{print "glance    image-download  --progress  --file  /root/images/" $4 "  "  $2  }'  |  xargs    -I {}  /bin/bash -c "{}"

cd /root/images && python -m SimpleHTTPServer 50000 


```