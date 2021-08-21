
# 平台更换ceph14存储


```bash

mkdir -p /root/ceph14/

# 下载 ceph14 rpm 以及依赖
# 如果 是 外网 请 更换 dav_ip

http://192.168.63.100:50000/remote.php/webdav/ceph/gperftools-libs-2.6.1-1.el7.x86_64.rpm

http://192.168.63.100:50000/remote.php/webdav/ceph/liblz4.so.1.8.3



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


# 建立 新的 iso 连接


# 卸载 旧的 依赖包

for conflicts_pkg in 'ceph' 'librados'  'librbd'  'librgw2'  'gperftools'  'python-rados'  'python-rbd' 'rbd-nbd'
do
  rpm -qa | grep ${conflicts_pkg} | xargs -I {} rpm -e {} --nodeps
done


# 清除完了之后，你就rpm -ivh *.rpm --nodeps或者不加--nodeps，看看rpm包安装是否需要兼容哪些rpm包
# yum localinstall *.rpm

# rpm -Uvh *.rpm


cd /root/ceph14
rpm -Uvh *.rpm  --nodeps  --force




# 安装 新的 依赖 so
ldd /usr/bin/ceph-mon
        linux-vdso.so.1 =>  (0x00007ffcb2971000)
        libceph-common.so.0 => /usr/lib64/ceph/libceph-common.so.0 (0x00007f1b2c066000)
        libdl.so.2 => /lib64/libdl.so.2 (0x00007f1b2be62000)
        librt.so.1 => /lib64/librt.so.1 (0x00007f1b2bc5a000)
        libresolv.so.2 => /lib64/libresolv.so.2 (0x00007f1b2ba40000)
        libleveldb.so.1 => /lib64/libleveldb.so.1 (0x00007f1b2b7ee000)
        libsnappy.so.1 => /lib64/libsnappy.so.1 (0x00007f1b2b5e8000)
        liblz4.so.1 => not found
        libz.so.1 => /lib64/libz.so.1 (0x00007f1b2b3d2000)


\cp /root/ceph14/liblz4.so.1.8.3  /lib64/

\rm /lib64/liblz4.so.1

ln -s /lib64/liblz4.so.1.8.3    /lib64/liblz4.so.1

# 验证一下 不再出现 not found 就好
ldd /usr/bin/ceph-mon


# 所有 安装完之后 记得  重启 zkeeper 部署工具
systemctl restart zkeeper



```



```bash

需要在
/usr/lib/python2.7/site-packages/zkeeper/storage/conf/10.2.5-ceph.conf.ex

sed -i 's/\[mon\]/\[mon\]\nmon_max_pg_per_osd = 2000/g'  /usr/lib/python2.7/site-packages/zkeeper/storage/conf/10.2.5-ceph.conf.ex

sed -i 's/mon_max_pg_per_osd = 2000/# mon_max_pg_per_osd = 2000/g'  /usr/lib/python2.7/site-packages/zkeeper/storage/conf/10.2.5-ceph.conf.ex

# 注释
sed -i 's/# mon_max_pg_per_osd = 2000/mon_max_pg_per_osd = 2000/g' /usr/lib/python2.7/site-packages/zkeeper/storage/conf/10.2.5-ceph.conf.ex

[mon]下添加
mon_max_pg_per_osd = 2000


若出现f
ull ratio(s) out of order
错误，可通过
ceph health detail | grep full查看详细报错信息，
需要 


ceph osd set-full-ratio 0.9


# 添加 选项

cp /usr/lib/python2.7/site-packages/zkeeper/storage/conf/10.2.5-ceph.conf.ex  /usr/lib/python2.7/site-packages/zkeeper/storage/conf/10.2.5-ceph.conf.ex.old

sed -i 's/\[mon\]/\[mon\]\nmon_max_pg_per_osd = 2000/g'  /usr/lib/python2.7/site-packages/zkeeper/storage/conf/10.2.5-ceph.conf.ex


```




```bash

需要在
/usr/lib/python2.7/site-packages/zkeeper/storage/conf/10.2.5-ceph.conf.ex


sed -i 's/mon_max_pg_per_osd = 2000/# mon_max_pg_per_osd = 2000/g'  /usr/lib/python2.7/site-packages/zkeeper/storage/conf/10.2.5-ceph.conf.ex

# 注释
sed -i 's/# mon_max_pg_per_osd = 2000/mon_max_pg_per_osd = 2000/g' /usr/lib/python2.7/site-packages/zkeeper/storage/conf/10.2.5-ceph.conf.ex

[mon]下添加
mon_max_pg_per_osd = 2000


若出现f
ull ratio(s) out of order
错误，可通过
ceph health detail | grep full查看详细报错信息，
需要 


ceph osd set-full-ratio 0.92

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