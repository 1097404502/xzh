# cephadm 是什么

cephadm 是容器搭建 ceph 的 一种新方式

# 创建一个规格不小的虚拟机
按照ceph 官网 推荐，大于 24 g

# 安装cephadm
```bash

# curl --silent --remote-name --location https://github.com/ceph/ceph/raw/octopus/src/cephadm/cephadm

# 国内加速 可能已经失效
wget -O ./cephadm http://limengkai.work:50000/cephadm

chmod +x cephadm

./cephadm --help

./cephadm add-repo --release octopus
./cephadm install

which cephadm

/usr/sbin/cephadm

--docker 
```

# To bootstrap the cluster

```bash

mkdir -p /etc/ceph

# cephadm bootstrap --mon-ip <you_pmon_ip>
cephadm  --docker  bootstrap --mon-ip 192.168.141.20 

# 允许主机名和 ip 相同， 在没有 dns 服务器的时候比较推荐
cephadm  --docker  bootstrap --mon-ip 192.168.141.20  --skip-pull  --allow-fqdn-hostname
```

# enable ceph cli

```bash

cephadm shell 


cephadm shell -- ceph -s 

cephadm add-repo --release octopus
cephadm install ceph-common

# than you can diracet use

ceph -v
ceph status

```


# ADD HOSTS TO THE CLUSTER
To add each new host to the cluster, perform two steps:

Install the cluster’s public SSH key in the new host’s root user’s authorized_keys file:

```bash

ssh-copy-id -f -i /etc/ceph/ceph.pub root@*<new-host>*

```
For example:

```bash

ssh-copy-id -f -i /etc/ceph/ceph.pub root@host2
ssh-copy-id -f -i /etc/ceph/ceph.pub root@host3


```
Tell Ceph that the new node is part of the cluster:

ceph orch host add *newhost*
For example:

```bash

ceph orch host add host2
ceph orch host add host3

```

## add my node
```bash

ssh-copy-id -f -i /etc/ceph/ceph.pub root@192.168.141.23
ssh-copy-id -f -i /etc/ceph/ceph.pub root@192.168.141.24
ssh-copy-id -f -i /etc/ceph/ceph.pub root@192.168.141.140

ceph orch host add  host-192-168-141-23
ceph orch host add  host-192-168-141-24
ceph orch host add  host-192-168-141-140

```

## add my node
```bash

ssh-copy-id -f -i /etc/ceph/ceph.pub root@192.168.141.23
ssh-copy-id -f -i /etc/ceph/ceph.pub root@192.168.141.24

ceph orch host add  host23
ceph orch host add  host24


ceph orch host add  192.168.141.23
ceph orch host add  192.168.141.24


```

# add additional mon

```bash

ceph config set mon public_network *<mon-cidr-network>*
ceph config set mon public_network 192.168.0.0/16

```

# add osd

```bash

ceph orch device ls

ceph orch device zap host-192-168-141-20 /dev/sdb --force
ceph orch device zap host-192-168-141-23 /dev/sdb --force
ceph orch device zap host-192-168-141-24 /dev/sdb --force

ceph orch device zap host-192-168-141-140 /dev/sdb --force

ceph orch daemon add osd host-192-168-141-20:/dev/sdb
ceph orch daemon add osd host-192-168-141-23:/dev/sdb
ceph orch daemon add osd host-192-168-141-24:/dev/sdb


ceph orch daemon add osd host-192-168-141-140:/dev/sdb



ceph orch device zap host20 /dev/sdb --force
ceph orch device zap host23 /dev/sdb --force
ceph orch device zap host24 /dev/sdb --force

ceph orch daemon add osd host20:/dev/sdb
ceph orch daemon add osd host23:/dev/sdb
ceph orch daemon add osd host24:/dev/sdb


orch device ls [<hostname>...] [plain|json|json-pretty|yaml] [--refresh] [--wide]            List devices on a host
orch device zap <hostname> <path> [--force]                                                  Zap (erase!) a device so it can be re-used


# 成功创建三个 osd ceph 设备
[root@host-192-168-141-20 ~]# ceph orch device ls
Hostname             Path      Type  Serial                                Size   Health   Ident  Fault  Available  
host-192-168-141-20  /dev/sdb  hdd   32007f50-1e38-4a84-8f63-1e69c674f43d  53.6G  Unknown  N/A    N/A    No         
host-192-168-141-23  /dev/sdb  hdd   0652ea45-425d-40cd-bd20-b2e50123e9bf  32.2G  Unknown  N/A    N/A    No         
host-192-168-141-24  /dev/sdb  hdd   32ec781d-cea2-4f67-b1e1-78e7a1104940  32.2G  Unknown  N/A    N/A    No  

```

# 创建ceph文件系统
```bash

ceph osd pool create cephfs_data
ceph osd pool create cephfs_metadata

ceph fs new my_fs cephfs_metadata cephfs_data 

ceph fs ls

其中：<pg_num> = 128 ,

关于创建存储池

确定 pg_num 取值是强制性的，因为不能自动计算。下面是几个常用的值：

　　*少于 5 个 OSD 时可把 pg_num 设置为 128

```

# 创建 mdss
```bash

ceph orch apply mds *<fs-name>* --placement="*<num-daemons>* [*<host1>* ...]"

ceph fs ls
output:  name: my_fs, metadata pool: cephfs_metadata, data pools: [cephfs_data ]

ceph orch apply mds my_fs  --placement=3
output:   Scheduled mds.my_fs update..

ceph orch apply mds my_fs  --placement="3 192.168.141.20 192.168.141.23 192.168.141.24"

ceph mds stat
output:   my_fs:1 {0=my_fs.host-192-168-141-20.tfeucj=up:active} 2 up:standby

```

# 创建 DEPLOY RGWS
```bash

radosgw-admin realm create --rgw-realm=my_realm --default
radosgw-admin zonegroup create --rgw-zonegroup=my_zonegroup  --master --default
radosgw-admin zone create --rgw-zonegroup=my_zonegroup --rgw-zone=my_zone --master --default
radosgw-admin period update --rgw-realm=my_realm --commit

ceph orch apply rgw my_realm my_zone --placement=3
```

# 创建 nfs
```bash

ceph osd pool create my_nfs_pool

ceph orch apply nfs my_nfs my_nfs_pool nfs-ns

ceph osd pool application enable my_nfs_pool cephfs


这里我们使用了rbd（块设备），pool 只能对一种类型进行 enable，另外两种类型是cephfs（文件系统），rgw（对象存储）

```
# 创建 rbd
```bash
ceph osd pool create rbd

ceph osd pool application enable rbd rbd

rbd pool init rbd

rbd pool stats 

rbd create --size 1024 bar

```

# using dashboard
```bash

ceph dashboard ac-user-create kk lmk@19980312! administrator

ceph dashboard ac-user-show kk

ceph mgr services 

```
访问 
https://192.168.141.20:8443/#/dashboard

usercount :  kk
pwd :        lmk@19980312!


```bash

Ceph Dashboard is now available at:

             URL: https://host-192-168-141-20.zettakit:8443/
            User: admin
        Password: 03d5auyq0n

You can access the Ceph CLI with:

        sudo /usr/sbin/cephadm shell --fsid 2aa7de1c-497a-11eb-b926-fa163e717f07 -c /etc/ceph/ceph.conf -k /etc/ceph/ceph.client.admin.keyring

Please consider enabling telemetry to help improve Ceph:

        ceph telemetry on

For more information see:

        https://docs.ceph.com/docs/master/mgr/telemetry/

Bootstrap complete.


```


# 删除集群
```bash

cephadm rm-cluster --fsid 2aa7de1c-497a-11eb-b926-fa163e717f07 --force
ERROR: must pass --force to proceed: this command may destroy precious data!

cephadm rm-cluster --fsid dc05693c-48bb-11eb-84da-fa163e717f07 --force
cephadm rm-cluster --fsid 1064116e-4976-11eb-b4ae-fa163e717f07 --force

cephadm rm-daemon   --fsid 2aa7de1c-497a-11eb-b926-fa163e717f07

```


# 删除当前集群
```bash

fs_id=$(grep -Eo "fsid = .*$" /etc/ceph/ceph.conf  | grep -Eo "\S+\s*$" 2>&1);cephadm rm-cluster --fsid $fs_id --force

# 快速创建
cephadm  --docker  bootstrap --mon-ip 192.168.141.20  --skip-pull 

 --allow-fqdn-hostname

```

# 决定最后 url 是host 还是 ip
```bash
Ceph Dashboard is now available at:

             URL: https://host-192-168-141-20.zettakit:8443/

/etc/hosts 中有没有 ip 映射关系
如果没有, ceph 集群会去 dns 做查询，然后 再将 url 替换成 域名

for ip_0 in `seq 0 255`;do echo "192.168.141.$ip_0 host$ip_0" >> /etc/hosts ;done
```

# scp 复制文件
```bash
for i in "192.168.141.23"  "192.168.141.24"  ; do scp -rp /etc/hosts root@$i:/etc ;done
```