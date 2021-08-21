```bash

curl -u admin:brysjhhrhl356126155165352237656123565615 -o ceph14213latest.tgz  http://192.168.63.100:50000/remote.php/dav/files/admin/ceph/ceph14213latest.tgz


mkdir ceph14
cd ./ceph14
tar zxvf ceph14213latest.tgz
cd ./ceph14213latest/
rpm -e ceph-libs-compat-10.2.10-20200528.x86_64 ceph-fuse-10.2.10-20200528.x86_6 libcephfs1-devel-10.2.10-20200528.x86_64
rpm -Uvh *.rpm
 
# 所有 安装完之后 记得重启 zkeeper服务
systemctl restart zkeeper


rpm -p  ceph-libs-compat-10.2.10-*

```