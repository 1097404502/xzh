# 介绍
cephfs 遵循 posix 标准的文件系统。在 ceph 分布式对象存储 之上构建。
最先进，高用途，高可用，高性能。
可以实现，应用程序，以及共享主机目录等用例。


# cephfs-shell

## 安装ceph 命令行
```bash
cp -a /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak

wget -O /etc/yum.repos.d/CentOS-Base.repo https://repo.huaweicloud.com/repository/conf/CentOS-7-reg.repo

yum clean all
yum makecache

#启用 epel

cp -a /etc/yum.repos.d/epel.repo /etc/yum.repos.d/epel.repo.backup
mv /etc/yum.repos.d/epel-testing.repo /etc/yum.repos.d/epel-testing.repo.backup

sed -i "s/#baseurl/baseurl/g" /etc/yum.repos.d/epel.repo
sed -i "s/metalink/#metalink/g" /etc/yum.repos.d/epel.repo
sed -i "s@https\?://download.fedoraproject.org/pub@https://repo.huaweicloud.com@g" /etc/yum.repos.d/epel.repo

yum update -y

yum install ceph-commen -y

```

## 创建 cepffs 目录
```bash

#需要保证 存储池 cephfs_metadata cephfs_data  都已经存在

ceph osd pool create cephfs2_metadata  32

ceph fs new my_fs2 cephfs2_metadata cephfs_data 
Error EINVAL: Creation of multiple filesystems is disabled.  To enable this experimental feature, use 'ceph fs flag set enable_multiple true'
默认是不可以创建两个 存储池的。

```
## 挂载创建好的 cephfs 目录

```bash
# 现在本地创建个文件夹
mkdir /a_cephfs

mount.ceph 192.168.141.20:6789:/ /a_cephfs  -o name=admin,secret=AQCpjupfug8aIhAAHPEyPiqcLPuytx3WjCwB+Q==

```

### 挂载 demo
```bash

Pass the port along with IP address if it’s running on a non-standard port:

mount.ceph 192.168.0.1:7000:/ /mnt/mycephfs
If there are multiple monitors, passes addresses separated by a comma:

mount.ceph 192.168.0.1,192.168.0.2,192.168.0.3:/ /mnt/mycephfs

mount.ceph 192.168.141.20:6789:/ /a_cephfs  -o name=admin,secret=AQCpjupfug8aIhAAHPEyPiqcLPuytx3WjCwB+Q==


```

## 指定远程文件目录

Mount only part of the namespace/file system:

mount.ceph :/some/directory/in/cephfs /mnt/mycephfs

当前 整个 ceph 集群中，只存在 一个 cephfs 系统，namespace 叫做 my_fs
由于 ceph 默认只允许创建一个 分布式文件系统，所以 不需要指定，我们的挂载路径都是挂载到 my_fs 中
```bash
完成之后
mount.ceph :/ /a_cephfs  -o name=admin,secret=AQCpjupfug8aIhAAHPEyPiqcLPuytx3WjCwB+Q==

# 本地目录操作
cd   /a_cephfs
mkdir dir1

```

### 挂载子目录
我们已经在 my_fs 中创建了 dir1
```bash

mount.ceph :/ /a_cephfs  -o name=admin,secret=AQCpjupfug8aIhAAHPEyPiqcLPuytx3WjCwB+Q==
mkdir /a_dir1
mount.ceph :/dir1 /a_dir1  -o name=admin,secret=AQCpjupfug8aIhAAHPEyPiqcLPuytx3WjCwB+Q==

cd /a_dir1 ; mkdir dir1_1

ls /a_dir1
dir1_1

ls /a_cephfs/dir1
dir1_1

```



## 挂载目录后，万万不可，直接删除目录

### 直接删除的 后果
```bash

mount.ceph :/ /a_cephfs  -o name=admin,secret=AQCpjupfug8aIhAAHPEyPiqcLPuytx3WjCwB+Q==
mount.ceph :/ /a_ceph2  -o name=admin,secret=AQCpjupfug8aIhAAHPEyPiqcLPuytx3WjCwB+Q==
cd /a_cephfs
mkdir dir1

# 此时 /a_cephfs  /a_ceph2 都挂在了 远程同一个分布式目录
ls /a_ceph2
dir1

ls /a_cephfs
dir1


rm -rf /a_ceph2

ls /a_cephfs

将会导致所有的文件都消失了。

```

### 请先 unmount 目标文件夹，然后再删除。
```bash

mount.ceph :/ /a_ceph2  -o name=admin,secret=AQCpjupfug8aIhAAHPEyPiqcLPuytx3WjCwB+Q==
cd /a_cephfs
mkdir dir1


ls /a_ceph2
dir1

ls /a_cephfs
dir1

umount /a_ceph2 ; rm -rf /a_ceph2;

ls /a_cephfs
dir1

```


# 远程主机挂载 cephfs

## 安装 mount.ceph

```bash

yum install epel-release -y

cp -a /etc/yum.repos.d/epel.repo /etc/yum.repos.d/epel.repo.backup
mv /etc/yum.repos.d/epel-testing.repo /etc/yum.repos.d/epel-testing.repo.backup

sed -i "s/#baseurl/baseurl/g" /etc/yum.repos.d/epel.repo
sed -i "s/metalink/#metalink/g" /etc/yum.repos.d/epel.repo
sed -i "s@https\?://download.fedoraproject.org/pub@https://repo.huaweicloud.com@g" /etc/yum.repos.d/epel.repo

yum update -y

yum install ceph-commen -y
# 包含了 mount.ceph

```

## 使用 mount.ceph

```bash

mount.ceph 192.168.141.20:6789:/ /a_ceph  -o name=admin,secret=AQCpjupfug8aIhAAHPEyPiqcLPuytx3WjCwB+Q==

```

