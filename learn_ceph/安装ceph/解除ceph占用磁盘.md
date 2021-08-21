

# 解除 ceph 占用
```bash

dmsetup remove ceph--87fc13e3--32d8--4b4c--87a6--ecc1a7a84f00-osd--block--7b2a2d81--ed8c--4c9f--abfd--0ccfefbc07ef

mkfs.xfs /dev/sdb

将该磁盘 删掉
重新部署 平台

```


# 记录
dmsetup ls 查看谁在占用，找到ceph-**字样（ceph-**为lsblk显示的块设备具体信息）

使用dmsetup 删除字样

dmsetup remove ceph-**



