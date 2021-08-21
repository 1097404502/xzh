

# 获得密码
```bash
cat ./keystonerc_admin | grep -E "(OS_USERNAME|OS_PASSWORD)"
    export OS_USERNAME=admin
    export OS_PASSWORD='69feb21954004508'
```
# cirros
http://download.cirros-cloud.net/0.5.1/cirros-0.5.1-x86_64-disk.img

# 成功安装后的输出
```bash
^M192.168.141.32_compute.pp:                           [ ESC[32mDONEESC[0m ]
Applying Puppet manifests                            [ ESC[32mDONEESC[0m ]
Finalizing                                           [ ESC[32mDONEESC[0m ]

 **** Installation completed successfully ******

Additional information:
 * ESC[0;31mParameter CONFIG_NEUTRON_L2_AGENT: You have chosen OVN Neutron backend. Note that this backend does not support the VPNaaS or FWaaS services. Geneve will be used as the encapsulation method for tenant networksESC[0m
 * A new answerfile was created in: /root/packstack-answers-20210122-160030.txt
 * Time synchronization installation was skipped. Please note that unsynchronized time on server instances might be problem for some OpenStack components.
 * File /root/keystonerc_admin has been created on OpenStack client host 192.168.141.32. To use the command line tools you need to source the file.
 * To access the OpenStack Dashboard browse to http://192.168.141.32/dashboard .
Please, find your login credentials stored in the keystonerc_admin in your home directory.
 * Because of the kernel update the host 192.168.141.32 requires reboot.
 * The installation log file is available at: /var/tmp/packstack/20210122-160030-HC7DON/openstack-setup.log
 * The generated manifests are available at: /var/tmp/packstack/20210122-160030-HC7DON/manifests

```

OS_AUTH_URL=http://192.168.141.32:5000/v3

backup_swift_auth_url=http://192.168.141.32:5000/v3

# 单机版快速搭建
https://blog.csdn.net/qq_28540443/article/details/109090698

# 添加dns
```bash
vi /etc/sysconfig/network-scripts/ifcfg-eth0

添加
DNS1=114.114.114.114

# 重启网络
systemctl restart network

```

# 查看cpu 虚拟化
```bash
##(for Intel CPU)
cat /proc/cpuinfo | grep vmx 

cat /proc/cpuinfo | grep svm ##（for AMD CPU）

dmesg |grep kvm


```

# 国内镜像
```bash
/bin/cp /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak
curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
yum makecache
yum clean all
yum update


```
# 关闭 selinux
```bash

sed -i '/^SELINUX=.*/c SELINUX=disabled' /etc/selinux/config
sed -i 's/^SELINUXTYPE=.*/SELINUXTYPE=disabled/g' /etc/selinux/config 
grep --color=auto '^SELINUX' /etc/selinux/config
setenforce 0

systemctl stop NetworkManager
systemctl disable NetworkManager


```

# 安装openstack 组件
```bash

yum list | grep openstack*
yum -y install centos-release-openstack-train
yum -y install python-openstackclient
yum install -y openstack-selinux.noarch
yum install -y openstack-utils

# 安装 rdo
yum install https://rdoproject.org/repos/rdo-release.rpm -y

```

# packstack 自动安装 openstack
```bash

yum -y install openstack-packstack

# 生成 自动安装 文件
packstack --gen-answer-file=~/openstack.txt


```
## 修改内容 为 自己对应的 信息
```bash
CONFIG_SWIFT_INSTALL=n  #y-n SWIFT是OpenStack的对象存储组件，默认是Y，在生产环境中一般是不装，所以改n
CONFIG_AODH_INSTALL=n   #y-n 不安装该服务
CONFIG_COMPUTE_HOSTS=192.168.1.100 #计算节点ip地址 
CONFIG_NEUTRON_ML2_TYPE_DRIVERS=vxlan,flat 
CONFIG_NEUTRON_ML2_TENANT_NETWORK_TYPES=vxlan 
CONFIG_NEUTRON_ML2_MECHANISM_DRIVERS=openvswitch 
CONFIG_NEUTRON_ML2_FLAT_NETWORKS=physnet1      #flat网络这边要设置物理网卡名字
CONFIG_NEUTRON_L2_AGENT=openvswitch            #L2网络的代理模式,也可选择linuxbridge
CONFIG_NEUTRON_OVS_BRIDGE_MAPPINGS=physnet1:br-ex    #这边要设置物理网卡的名字
CONFIG_NEUTRON_OVS_BRIDGE_IFACES=br-ex:eth0          #这边br-ex:eth0是网络节点的nat网卡，到时候安装完毕之后IP地址会漂到这个上

```

# 开始自动安装
```bash

packstack --answer-file=openstack.txt

# 只有一个节点 也可以直接 allinone
packstack --allinone

nohup  packstack --allinone 2>&1 > install_opsk.log &
```


# 失败提醒，
如果由于网络原因安装 失败了，那么 要么手动 清空数据库服务，删除所有数据 从新开始（不推荐，很繁琐）
重新初始化虚拟机重新 执行 安装脚本。


*****************
# 合并脚本
```bash


/bin/cp /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak
curl -o /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
yum makecache
yum clean all
yum update



sed -i '/^SELINUX=.*/c SELINUX=disabled' /etc/selinux/config
sed -i 's/^SELINUXTYPE=.*/SELINUXTYPE=disabled/g' /etc/selinux/config 
grep --color=auto '^SELINUX' /etc/selinux/config
setenforce 0

systemctl stop NetworkManager
systemctl disable NetworkManager



yum list | grep openstack*
yum -y install centos-release-openstack-train
yum -y install python-openstackclient
yum install -y openstack-selinux.noarch
yum install -y openstack-utils
yum install https://rdoproject.org/repos/rdo-release.rpm -y

yum -y install openstack-packstack
nohup  packstack --allinone 2>&1 > install_opsk.log &




```