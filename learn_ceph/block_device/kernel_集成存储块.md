# 平台报错 504 打不开控制台

# 查询 可用块
```bash

rbd list my_rbd_pool

```

# 映射image
```bash

rbd device map {pool-name}/{image-name} --id {user-name}

rbd device map my_rbd_pool/bar 
->
rbd: sysfs write failed
RBD image feature set mismatch. You can disable features unsupported by the kernel with "rbd feature disable my_rbd_pool/bar object-map fast-diff deep-flatten".

rbd feature disable my_rbd_pool/bar object-map fast-diff deep-flatten

rbd device map my_rbd_pool/bar 
->
/dev/rbd0

```

# 列出所有 映射的 drivce
```bash

rbd device list
->
/dev/rbd0


fdisk -l
->
磁盘 /dev/rbd0：2147 MB, 2147483648 字节，4194304 个扇区
Units = 扇区 of 1 * 512 = 512 bytes
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：4194304 字节 / 4194304 字节


```

# 取消映射
```bash

rbd device unmap /dev/rbd/{poolname}/{imagename}

```

# 挂载磁盘
```bash


# 写入 文件系统信息  xfs 评分性能 都 比 ext4 好 
# mkfs.ext4 /dev/rbd0
mkfs.xfs /dev/rbd0


->
正在写入inode表: 完成                            
Creating journal (16384 blocks): 完成
Writing superblocks and filesystem accounting information: 完成 

mkdir /rbd_dir ; mount /dev/rbd0 /rbd_dir

mount_path='/images'
mkdir ${mount_path} ; mount /dev/rbd0 ${mount_path}

```

# 查看磁盘用量
```bash

df /dev/rbd0
文件系统         1K-块  已用    可用 已用% 挂载点
/dev/rbd0      1998672  6640 1870792    1% /rbd_dir


```
# 快速写磁盘
```bash

dd if=/dev/zero of=/tmp/file bs=1G count=1

dd if=/dev/zero of=/rbd_dir/test_zero bs=1G count=1
记录了1+0 的读入
记录了1+0 的写出
1073741824字节(1.1 GB)已复制，3.86441 秒，278 MB/秒

dd if=/dev/zero of=/rbd_dir/test_zero bs=1.5G count=1

```

# 动态扩容
```bash

# rbd resize image 2g -> 8g
rbd resize --size $[1024*8] my_rbd_pool/bar

rbd resize --size $[1024*1024] volumes/images

# 查看原有大小
df /dev/rbd0
->
文件系统         1K-块    已用   可用 已用% 挂载点
/dev/rbd0      1998672 1580532 296900   85% /rbd_dir

# 重新挂载
umount  /dev/rbd0 
umount /rbd_dir


# 自动挂在磁盘
# vi /etc/fstab
# /dev/vdb /storage xfs defaults 0 0
mount /dev/rbd0 /rbd_dir

#再次查看 df 信息
df /dev/rbd0

# fdisk -l /dev/rbd0

磁盘 /dev/rbd0：8589 MB, 8589934592 字节，16777216 个扇区
Units = 扇区 of 1 * 512 = 512 bytes
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：4194304 字节 / 4194304 字节


```

# 刷新rbd 信息 ，重新挂载即可
```bash

mount_path='/images'

umount ${mount_path}

rbd_path='volumes/images'
rbd resize --size $[1024*1024] $rbd_path

rbd device unmap  $rbd_path
rbd device map $rbd_path


mkfs.ext4 /dev/rbd0


mkdir -p ${mount_path} ; mount /dev/rbd0 ${mount_path}


```
