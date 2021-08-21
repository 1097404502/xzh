# 升级步骤

黄扬:
没写wiki

就是代码目录里面的build脚本
环境中先安装rpm-build软件包

黄扬:
编译环境必须是centos7.x的系统，或者我们的zcloud os


```bash
# 黄扬:
./build.sh master 20210511

# master是git的分支名，或者commit id都行
# 后面的数字是编译出来的rpm的release，你测试，自己定义就行


rsync -avz ~/my_proj/cinder root@192.168.66.1:/root/

https://pkgs.org/

yum install epel-release -y
yum install rpm-build -y
yum install intltool  python-d2to1  python2-oslo-sphinx python-reno   python-sphinx  python-oslotest -y

# 需要 安装 epel-release

./build.sh master 20210528


rpm -Uvh --nodeps  python2-oslotest-3.2.0-lp152.4.3.noarch.rpm


cd ../OUTPUT

rpm -Uvh *.rpm


/usr/lib/python2.7/site-packages/cinder/locale/zh_CN/LC_MESSAGES



```