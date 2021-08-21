
# 查找一个用户的基本信息

```bash

ceph auth get {TYPE.ID}

ceph auth get client.admin
->
exported keyring for client.admin
[client.admin]
        key = AQCpjupfug8aIhAAHPEyPiqcLPuytx3WjCwB+Q==
        caps mds = "allow *"
        caps mgr = "allow *"
        caps mon = "allow *"
        caps osd = "allow *"

# 导出到文件
ceph auth get client.admin -o ./admin.keyring

ceph auth get client.lmk -o /etc/ceph/ceph.client.lmk.keyring

export 和 get 效果相同
ceph auth export {TYPE.ID}
ceph auth export client.admin
```

# 创建用户并指定相应的权限
```bash

ceph auth get-or-create client.george mon 'allow r' osd 'allow rw pool=liverpool' -o george.keyring

ceph auth get-or-create client.lmk mon 'allow rw' osd 'allow * pool=my_rbd_pool' -o lmk.keyring

```

# 修改已有用户的权限
```bash

ceph auth get client.john
ceph auth caps client.john mon 'allow r' osd 'allow rw pool=liverpool'
ceph auth caps client.paul mon 'allow rw' osd 'allow rwx pool=liverpool'
ceph auth caps client.brian-manager mon 'allow *' osd 'allow *'

```
# 删除用户
```bash

ceph auth del client.lmk

```

# 打印用户信息
```bash

mount -t ceph serverhost:/ mountpoint -o name=client.user,secret=`ceph auth print-key client.user`

```


# 从文件 导入 用户信息

```bash

sudo ceph auth import -i /etc/ceph/ceph.keyring

```


# 借助工具 创建 keyring
```bash

ceph-authtool --create-keyring -g -n client.lmk /root/test/keyring

```
