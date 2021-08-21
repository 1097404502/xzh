[toc]
# cinder 开发环境
git clone ssh://limengkai@gerrit.dev.zettakit.com:29418/cinder


## 创建 centos7 虚机
ubuntu18 和 centos8 都试过了，会有很多不兼容。

## 安装 pip
```bash
yum install wget -y 
wget -O ./get-pip.py http://limengkai.work:50000/get-pip.py

python get-pip.py

```

## 使用 公网镜像源 安装 tox

```bash

pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
pip install tox

```
## 更换内部pip 源

```bash

pip源必须是我们内部的一个，否则安装的包版本不兼容

pypi使用国内源加速安装
用pip安装
$ cat ~/.pip/pip.conf
[global]  
timeout = 600
disable-pip-version-check = true
index-url = http://192.168.105.12:8082/simple/
trusted-host = 192.168.105.12

[install]
use-mirrors = true
mirrors = http://192.168.105.12:8082/simple/
trusted-host = 192.168.105.12
使用setup.py安装的时候，还是从默认的pypi.python.org下载的。 需要的是distutils的配置，可以通过~/.pydistutils.cfg来配置distutils的源。
$ cat ~/.pydistutils.cfg
[easy_install]
index-url = http://192.168.105.12:8082/simple/

```

```bash

cat >  ~/.pip/zetta_pip.conf <<"EOF"
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

cat > ~/.pydistutils.cfg <<"EOF"
[easy_install]
index-url = http://192.168.105.12:8082/simple/
EOF

# 取消 zetta pip 镜像源
mv ~/.pydistutils.cfg ~/.backuppydistutils.cfg 
mv ~/.pip/pip.conf ~/.pip/backupzetta.conf

# 恢复zetta pip镜像源
mv ~/.backuppydistutils.cfg  ~/.pydistutils.cfg 
mv  ~/.pip/backupzetta.conf  ~/.pip/pip.conf


```

```bash
/bin/cp  ~/.pip/zetta_pip.conf  ~/.pip/pip.conf

```

# 安装依赖环境

```bash
sudo yum install gcc python-devel  libxslt  -y

ubuntu 
  sudo apt install libpython2-dev gcc -y

运行单测环境，是一个python的虚拟环境

tox

#运行方法
sudo tox -e py27 -- cinder.tests.unit

首先会自动安装依赖（pip安装的）
安装成功就开始跑单测了

调试方法
source "/home/lmk/codes/cinder/.tox/py27/bin/activate"

# 执行某个目录下的测试用例
python -m testtools.run discover cinder.tests.unit

# 执行单个测试用例
python -m testtools.run cinder.tests.unit.api.contrib.test_ceph_pool

# 执行所有 测试
python -m testtools.run

# 查看 所有测试用例结果
testr list-tests

```

# 查看日志
```bash

git log --pretty=oneline 

```

# centos 缺少的依赖报错
ImportError: libxslt.so.1: cannot open shared object file: No such file or directory
```bash
yum install libxslt -y
```

# ubuntu 缺少的依赖
```bash
sudo apt install libpq-dev

```


# 查找错误
```bash

cinder create  --name test_k1 10

cinder list

grep -E "`date -I`.*ERROR.* " -r /var/log/cinder/ | grep -v "oslo.messaging._drivers.impl_rabbit" |grep "ERROR"

```