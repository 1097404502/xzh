


# 添加 镜像源
```bash

echo "nameserver 114.114.114.114" > /etc/resolv.conf

/bin/cp -a /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak

curl -o  /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

yum clean all
yum makecache

curl -o /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo


yum update -y

yum install epel-release -y




```


# 浏览 ceph 国内的 镜像站 看看 有 那些版本

http://mirrors.163.com/ceph/

其中 有我们 需要的 cehp14 
http://mirrors.163.com/ceph/rpm-nautilus/

```bash



cat > /etc/yum.repos.d/ceph.repo << "EOF"
[ceph]
name=Ceph packages for x86_64
baseurl=http://mirrors.163.com/ceph/rpm-nautilus/el7/x86_64
enabled=1
gpgcheck=1
priority=1
type=rpm-md
gpgkey=http://mirrors.163.com/ceph/keys/release.asc

[ceph-noarch]
name=Ceph noarch packages
baseurl=http://mirrors.163.com/ceph/rpm-nautilus/el7/noarch
enabled=1
gpgcheck=1
priority=1
type=rpm-md
gpgkey=http://mirrors.163.com/ceph/keys/release.asc

[ceph-source]
name=Ceph source packages
baseurl=http://mirrors.163.com/ceph/rpm-nautilus/el7/SRPMS
enabled=0
gpgcheck=1
type=rpm-md
gpgkey=http://mirrors.163.com/ceph/keys/release.asc
priority=1

EOF

yum install epel-release -y
yum install ceph ceph-deploy  ceph-mgr-dashboard -y



```



# 修改主机名
```bash

hostname  node1

验证

yum install wget -y

wget -P ~/.ssh/ -r -np -nH  --cut-dirs=5  http://limengkai.work:50000/ssh/
chmod  700 -R ~/.ssh/


ssh node1


uuidgen
9762c648-539b-4707-a073-bd28675feac5

cat > /etc/hosts <<"EOF"
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6

192.168.166.201   node1
192.168.166.202   node2
192.168.166.203   node3
192.168.166.204   node4
192.168.166.205   node5

EOF

```

# 创建 ceph 配置文件

mon initial members = {hostname}[,{hostname}]
mon host = {ip-address}[,{ip-address}]


```bash


cat >  /etc/ceph/ceph.conf << "EOF"

[global]
fsid = 9762c648-539b-4707-a073-bd28675feac5

mon initial members = node1
mon host = 192.168.166.201
mon allow pool delete = true

public network = 192.168.166.0/24
auth cluster required = cephx
auth service required = cephx
auth client required = cephx
osd journal size = 1024
osd pool default size = 1
osd pool default min size = 1
osd pool default pg num = 333
osd pool default pgp num = 333
osd crush chooseleaf type = 1

[mon]
mgr initial modules = dashboard

EOF

# 生成 密匙

ceph-authtool --create-keyring /tmp/ceph.mon.keyring --gen-key -n mon. --cap mon 'allow *'
ceph-authtool --create-keyring /etc/ceph/ceph.client.admin.keyring --gen-key -n client.admin --cap mon 'allow *' --cap osd 'allow *' --cap mds 'allow *' --cap mgr 'allow *'
ceph-authtool --create-keyring /var/lib/ceph/bootstrap-osd/ceph.keyring --gen-key -n client.bootstrap-osd --cap mon 'profile bootstrap-osd' --cap mgr 'allow r'

ceph-authtool /tmp/ceph.mon.keyring --import-keyring /etc/ceph/ceph.client.admin.keyring
ceph-authtool /tmp/ceph.mon.keyring --import-keyring /var/lib/ceph/bootstrap-osd/ceph.keyring

chown ceph:ceph /tmp/ceph.mon.keyring

monmaptool --create --add node1  192.168.166.201  --fsid 9762c648-539b-4707-a073-bd28675feac5 /tmp/monmap

sudo -u ceph mkdir /var/lib/ceph/mon/ceph-node1

sudo -u ceph ceph-mon --mkfs -i node1 --monmap /tmp/monmap --keyring /tmp/ceph.mon.keyring


```

# 启动 第一天 monitor 节点
```bash

sudo systemctl start ceph-mon@node1

ceph -s
  cluster:
    id:     9762c648-539b-4707-a073-bd28675feac5
    health: HEALTH_WARN
            1 monitors have not enabled msgr2

ceph mon enable-msgr2

# 等待 一些时间
ceph -s
  cluster:
    id:     9762c648-539b-4707-a073-bd28675feac5
    health: HEALTH_OK


```

# 添加 osd
```bash
# 查看 当前磁盘信息
lsblk
NAME                        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda                           8:0    0   80G  0 disk
├─sda1                        8:1    0  500M  0 part /boot
└─sda2                        8:2    0 79.5G  0 part /
sdb                           8:16   0  100G  0 disk
sdc                           8:32   0  100G  0 disk
sdd                           8:48   0  100G  0 disk
sr0                          11:0    1 1024M  0 rom
sr1                          11:1    1  422K  0 rom
loop0                         7:0    0  100G  0 loop
└─docker-8:2-268437945-pool 253:0    0  100G  0 dm
loop1                         7:1    0    2G  0 loop
└─docker-8:2-268437945-pool 253:0    0  100G  0 dm



ssh node1
sudo ceph-volume lvm create --data /dev/sdb
sudo ceph-volume lvm create --data /dev/sdc
sudo ceph-volume lvm create --data /dev/sdd

```

# 查看 身份信息 并在 客户端 写入 身份信息
```bash

cat >  ceph.client.admin.keyring << "EOF"
[client.admin]
        key = AQDj0mtgCNBHBBAAJWnua9Vt8CKIJHB+Iep8nQ==
        caps mds = "allow *"
        caps mgr = "allow *"
        caps mon = "allow *"
        caps osd = "allow *"

EOF

```

# 添加 osd

```bash

#  add blue store   osd
sudo ceph-volume lvm create --data /dev/sdb

```

# 添加 mds  ( 需要 ceph 文件存储 才需要的 功能)
```bash

# 参考
# sudo -u ceph mkdir /var/lib/ceph/mon/ceph-node1
mkdir -p /var/lib/ceph/mds/ceph-node1

```


# 删除 添加 mon
```bash
# 添加 mon
ceph mon add <name> <IPaddr[:port]>


# 删除 ceph
service ceph -a stop mon.{mon-id}
ceph mon remove {mon-id}
# finial
# Remove the monitor entry from ceph.conf.


```


# 删除 添加 osd
```bash
ceph osd out {osd-num}

# 等待 数据 完成 均衡
  -w, --watch           watch live cluster changes
ceph -w

You should see the placement group states change from active+clean to active, some degraded objects, and finally active+clean when migration completes. (Control-c to exit.)

sudo systemctl stop ceph-osd@{osd-num}

ceph osd rm {osd-num}

```

# 添加 mgr
```bash

name='mgr'
sudo -u ceph  mkdir -p /var/lib/ceph/mgr/ceph-mgr/

ceph auth get-or-create mgr.$name mon 'allow profile mgr' osd 'allow *' mds 'allow *' |   cat >  /var/lib/ceph/mgr/ceph-mgr/keyring

保存结果存入 /var/lib/ceph/mgr/ceph-mgr/keyring 


sudo -u ceph cat >  /var/lib/ceph/mgr/ceph-mgr/keyring << "EOF"
[mgr.mgr]
        key = AQCQ62tgXk+tHRAA8i3SaE/yJ71eZlMSjFe4qA==

EOF

ceph-mgr -i $name
ceph status

```


# 开启 面板
```bash

ceph mgr module enable dashboard



ceph dashboard create-self-signed-cert

cat > /etc/ceph/dashboard.conf <<"EOF"
admin_pass
EOF


ceph dashboard ac-user-create admin -i  /etc/ceph/dashboard.conf  administrator

ceph mgr services

```