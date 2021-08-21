# 初始化脚本

```bash

sudo sed -i 's/ONBOOT="no"/ONBOOT="yes"/g' /etc/sysconfig/network-scripts/ifcfg-eth0
echo -e  '\nDNS1="114.114.114.114"' >> /etc/sysconfig/network-scripts/ifcfg-eth0
service network restart


/bin/cp -a /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak

wget -O /etc/yum.repos.d/CentOS-Base.repo https://repo.huaweicloud.com/repository/conf/CentOS-7-reg.repo

yum clean all
yum makecache

systemctl stop firewalld.service
systemctl disable firewalld.service
systemctl status firewalld.service



sudo yum remove docker docker-common docker-selinux docker-engine
sudo yum install -y yum-utils device-mapper-persistent-data lvm2

yum install wget -y

wget -O /etc/yum.repos.d/docker-ce.repo https://repo.huaweicloud.com/docker-ce/linux/centos/docker-ce.repo


sudo sed -i 's+download.docker.com+repo.huaweicloud.com/docker-ce+' /etc/yum.repos.d/docker-ce.repo


sudo yum makecache fast
sudo yum install docker-ce -y
systemctl enable docker
systemctl start docker





/bin/cp -a /etc/yum.repos.d/epel.repo /etc/yum.repos.d/epel.repo.backup
/bin/mv /etc/yum.repos.d/epel-testing.repo /etc/yum.repos.d/epel-testing.repo.backup


wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo

yum update -y

yum install epel-release -y

yum install python36 -y


wget -O ./get-pip.py http://limengkai.work:50000/get-pip.py
/usr/bin/python3.6 get-pip.py



```
国外镜像
curl -O https://bootstrap.pypa.io/get-pip.py


# 更改docker 镜像源

```bash

sudo docker login --username=漱石者枕夏目 registry.cn-hangzhou.aliyuncs.com

sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://wm12hkla.mirror.aliyuncs.com"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker


```


# 时间同步

## sync server
```bash

yum -y install chrony

vim /etc/chrony.conf
###################
allow 192.168.141.0/24
###################
systemctl enable chronyd
systemctl restart chronyd

```

## sync client

```bash


yum -y install chrony
echo "server 192.168.141.20 iburst" > /etc/chrony.conf
systemctl enable chronyd
systemctl restart chronyd
chronyc sources



```

# 时区设置
```bash

将你的硬件时钟设置为本地时区：

# timedatectl set local rtc 1

timedatectl set local-rtc 1
 
将你的硬件时钟设置为协调世界时（UTC）：

# timedatectl set-local-rtc 0

```

# 查看dns
```bash
cat /etc/resolv.conf

```