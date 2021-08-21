



# 更换 zcloud
```bash


#解压ceph14安装包并安装
mkdir ceph14
cd ./ceph14
curl -u admin:brysjhhrhl356126155165352237656123565615 -o ceph14213latest.tgz  http://192.168.63.100:50000/remote.php/webdav/ceph/ceph14213latest.tgz
tar zxvf ceph14213latest.tgz
cd ./ceph14213latest/
# rpm -e ceph-libs-compat-10.2.10-20200528.x86_64 ceph-fuse-10.2.10-20200528.x86_6 libcephfs1-devel-10.2.10-20200528.x86_64
rpm -qa | grep ".*ceph.*" | xargs   rpm -e 
rpm -Uvh *.rpm
 
# 所有 安装完之后 记得重启 zkeeper服务
systemctl restart zkeeper



curl -u admin:brysjhhrhl356126155165352237656123565615 -o ceph14213latest.tgz  http://192.168.63.100:50000/remote.php/webdav/ceph/ceph14213latest.tgz


 rpm -qa | grep ".*ceph.*" | xargs   rpm -e 

```

# 平台更换ceph14存储


```bash


# 外网ip
# dav_ip='119.36.243.58'

# 武汉内网

mkdir -p /root/ceph14/

cd /root/ceph14

dav_ip='192.168.63.100'

for fn in 'ceph.tar.gz'  'gperftools-libs-2.6.1-1.el7.x86_64.rpm'   'liblz4.so.1.8.3'
do
curl -u admin:brysjhhrhl356126155165352237656123565615 -o /root/ceph14/${fn}  http://${dav_ip}:50000/remote.php/webdav/ceph/${fn}

done


tar xvf  ceph.tar.gz


for conflicts_pkg in 'ceph' 'librados'  'librbd'  'librgw2'  'gperftools'  'python-rados'  'python-rbd' 'rbd-nbd'
do
  rpm -qa | grep ${conflicts_pkg} | xargs -I {} rpm -e {} --nodeps
done


cd /root/ceph14
rpm -Uvh *.rpm  --nodeps  --force

systemctl restart zkeeper



```

# 开启 autoscale
```bash

ceph health detail

ceph osd pool application enable volumes  rgw

ceph mon enable-msgr2

ceph osd pool autoscale-status

Error ENOTSUP: Module 'pg_autoscaler' is not enabled (required by command 'osd pool autoscale-status'): use `ceph mgr module enable pg_autoscaler` to enable it

ceph mgr module enable pg_autoscaler
ceph osd pool autoscale-status

for pool_name in 'volumes' 'backups' 'fastpool' 
do
  ceph osd pool set $pool_name pg_autoscale_mode on
done


# 稍等 一些时间
ceph -s
  cluster:
    id:     f376cd93-b18d-41aa-bd2f-6fd6e0946518
    health: HEALTH_OK


```