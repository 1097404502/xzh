# 在cinder 集群之外安装 qemu

```bash
# 好像需要开启 
yum install epel-release -y
yum install qemu -y
```

# 在 客户 机上 放置 授权文件
```bash

qemu-img {command} [options] rbd:glance-pool/maipo:id=glance:conf=/etc/ceph/ceph.conf
由于 qemu 命令 需要 /etc/ceph/ceph.conf 以及 keyring 
所以我们去 集群中 取一下
scp -rp root@192.168.141.20:/etc/ceph /etc

```

# 创建 image
```bash
# 第二个 rbd 是 pool 存储池名称
qemu-img create -f raw rbd:rbd/foo 1G

qemu-img create -f raw rbd:rbd/qemu_img_client 1G



rbd info  qemu_img_client
->
rbd image 'qemu_img_client':
        size 1 GiB in 256 objects
        order 22 (4 MiB objects)
        snapshot_count: 0
        id: 391b7fcc6093


```

# qemu 查看镜像信息
```bash

qemu-img info rbd:rbd/foo
->
image: rbd:rbd/foo
file format: raw
virtual size: 1.0G (1073741824 bytes)
disk size: unavailable


```

# qemu resize 镜像
```bash

qemu-img resize rbd:rbd/foo 3G

```

# qemu 根据镜像创建 image
```bash

qemu-img convert -f qcow2 -O raw debian_squeeze.qcow2 rbd:data/squeeze

qemu-img convert -f raw -O raw /a_dir/cirros-0.5.1-x86_64-disk.img rbd:rbd/cirros

qemu-img convert -f qcow2 -O raw /a_dir/cirros-0.5.1-x86_64-disk.img rbd:rbd/cirros
qemu-img create -f raw rbd:rbd/qemu_img_client 

```

# 
```bash

qemu -m 1024 -drive format=raw,file=rbd:rbd/cirros

qemu-system-x86_64 -m 1024 -drive format=raw,file=rbd:rbd/cirros

qemu-kvm -m 256 -smp 2 -name 'test' -hda /a_dir/cirros-0.5.1-x86_64-disk.img


qemu-kvm -m 128 -cpu host -smp 2 -name "test" -drive file=/images/kvm/cirros-0.3.4-x86_64-disk.img,if=virtio,media=disk,format=qcow2,cache=writeback -nographic -net nic -net tap,name=vif0.0,script=/etc/qemu-ifup

qemu-kvm -m 128 -cpu host -smp 2 -name "test" -drive file=/a_dir/cirros-0.5.1-x86_64-disk.img,if=virtio,media=disk,format=qcow2,cache=writeback -nographic -net nic -net tap,name=vif0.0,script=/a_dir/qemu-ifup

qemu-kvm -m 256 -smp 2 -name 'test' -hda /a_dir/cirros-0.5.1-x86_64-disk.img


qemu-kvm -cpu Broadwell -m 512 -smp 2 -name "test" \
-drive file=cirros-0.5.1-x86_64-disk.img,if=virtio,media=disk,format=qcow2,cache=writeback -vnc 0.0.0.0:0


```


# 
```bash
ss -tnl
yum install tigervnc -y
vncviewer :5900

```