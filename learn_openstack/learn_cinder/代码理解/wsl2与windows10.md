# wsl2 访问 windows10
```bash

ls /mnt/c

```

# 吧windows下的 rmp 文件拷贝过来
```bash


```

# 解压rmp 包 
```bash

find ./Packages/ -name "python2-oslo*"

./Packages/python2-oslo-reports-1.6.0-1.el7.noarch.rpm
./Packages/python2-oslo-privsep-1.13.1-1.el7.noarch.rpm
./Packages/python2-oslo-utils-3.16.1-1.el7.noarch.rpm
./Packages/python2-oslo-service-1.7.0-1.el7.noarch.rpm
 
rpm2cpio rpm-4.8.0-32.el6.x86_64.rpm |cpio -div
 
 ```