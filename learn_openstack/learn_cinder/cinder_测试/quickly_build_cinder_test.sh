#!/bin/bash

mkdir -p ~/.ssh
cat > ~/.ssh/config <<"EOF"
Host *
   StrictHostKeyChecking no
   UserKnownHostsFile=/dev/null
EOF

yum install wget -y
wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo
sudo yum clean all
sudo yum makecache
yum install git -y
cd ~
git clone ssh://limengkai@gerrit.dev.zettakit.com:29418/cinder

sudo yum install gcc python-devel  libxslt wget  -y

wget -O ./get-pip.py http://limengkai.work:50000/get-pip.py
python get-pip.py
pip install tox -i https://mirrors.aliyun.com/pypi/simple

mkdir -p ~/.config/pip
cat > ~/.config/pip/pip.conf <<"EOF"
[global]
timeout = 600
disable-pip-version-check = true
index-url = http://192.168.105.12:8082/simple/
trusted-host = 192.168.105.12

[install]
use-mirrors = true
mirrors = http://192.168.105.12:8082/simple/
trusted-host = 192.168.105.12
EOF

mkdir -p ~/.pip
cat > ~/.pip/pip.conf<<"EOF"
[global]  
timeout = 600
disable-pip-version-check = true
index-url = http://192.168.105.12:8082/simple/
trusted-host = 192.168.105.12

[install]
use-mirrors = true
mirrors = http://192.168.105.12:8082/simple/
trusted-host = 192.168.105.12
EOF

cat > ~/.pydistutils.cfg<<"EOF"
[easy_install]
index-url = http://192.168.105.12:8082/simple/
EOF



cd ~/cinder
sudo tox -e py27 -- cinder.tests.unit

