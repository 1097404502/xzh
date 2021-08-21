# cinder 单元测试 是个 内存怪兽 并行 核数 越高 消耗内存越多
```bash

64 核心 上

KiB Mem : 32760932 total, 17293356 free, 13669540 used,  1798036 buff/cache

KiB Mem : 32760932 total, 16868740 free, 14075948 used,  1816244 buff/cache


real    1m29.818s
user    0m0.229s
sys     0m0.318s

```


# 查看 详细报错

list error

```bash

testr list-tests

```


#  使用 容器 单测 之前 先准备 目录 资料如下
```bash


--workdir
     |
     cinder (源代码)
     |
     packages (依赖环境)

cinder_test_ip='192.168.164.190'

rsync -a -v -e ssh  --exclude='*.pyc'  --exclude='*.pyo'  --exclude='.tox/' --exclude='.testrepository/'   /root/zetta_code/cinder  root@${cinder_test_ip}:/root/

rsync -a -v -e ssh  --exclude='*.pyc'  --exclude='*.pyo'  --exclude='.tox/' --exclude='.testrepository/'   /root/my_proj/my_pip/packages  root@${cinder_test_ip}:/root/

cinder_path='/root/cinder'
packages_path='/root/packages'

c_name='cinder-test-0'

# store_url='registry.cn-hangzhou.aliyuncs.com/mkmk/all'
# registry.cn-hangzhou.aliyuncs.com/mkmk/all:zcinder-test
# docker tag registry.cn-hangzhou.aliyuncs.com/mkmk/all:zcinder-test  192.168.63.100:5000/zcloud:zcinder-test

store_url=' 192.168.63.100:5000/zcloud'
zcinder_url="${store_url}:zcinder-test"

docker rm -f ${c_name}

docker run -d --privileged  --name ${c_name}  -v ${cinder_path}:/cinder -v ${packages_path}:/packages ${zcinder_url} init  


time docker exec -it ${c_name}  /bin/bash  -c 'cd /cinder ; /usr/bin/tox -e py27 -- cinder.tests.unit '


--> 64 核心 跑了 1min30s
real    1m28.717s
user    0m0.237s
sys     0m0.390s

# 查看 详细 报错
docker exec -it ${c_name}  /bin/bash 

cd /cinder

source /cinder/.tox/py27/bin/activate

testr list-tests



# 执行某个单侧

```
# 查看 单元测试 详细输出
```bash

source /cinder/.tox/py27/bin/activate
testr list-tests 

```
# 执行 指定 单侧 节约时间
```bash

source /cinder/.tox/py27/bin/activate

# 执行 某个 目录
python -m testtools.run discover cinder.tests.unit

# 执行 某个 具体单侧

python -m testtools.run cinder.tests.unit.api.contrib.test_ceph_pool

python -m testtools.run  cinder.tests.unit.scheduler.test_host_filters.CapacityFilterTestCase.test_filter_passes_extend_volume

python -m testtools.run  cinder.tests.unit.scheduler.test_rpcapi.SchedulerRpcAPITestCase.test_extend_volume_worker


cinder/tests/unit/scheduler/test_host_filters.py

```


# 上传镜像
```bash

store_url='registry.cn-hangzhou.aliyuncs.com/mkmk/all'

zcinder_url="${store_url}:zcinder-test"

docker commit cinder-test ${zcinder_url}

docker push ${zcinder_url}

docker tag 

```


# 配置 nginx 代理 packages 目录

```bash

    server {
        listen       80;
        server_name  localhost;

        add_header Access-Control-Allow-Origin *;
        add_header Access-Control-Allow-Headers X-Requested-With;
        add_header Access-Control-Allow-Methods GET,POST,OPTIONS;

        location / {
            root /packages;
            autoindex on;
        }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }

```

# 启动server
```bash

docker run -d --privileged  --net=host  --name cinder-host  ${zcinder_url} init

```

# 修改 cli 用户
```bash
vi admin-openrc

export OS_PROJECT_DOMAIN_NAME=default
export OS_USER_DOMAIN_NAME=default
export OS_PROJECT_NAME=project1
export OS_TENANT_NAME=default
export OS_USERNAME=admin
export OS_PASSWORD=admin_pass
export OS_AUTH_URL=http://192.168.66.1:35357/v3
export OS_IDENTITY_API_VERSION=3
export OS_VOLUME_API_VERSION=2

```





# 运行 测试 cinder 环境
```bash

docker run -d --privileged  --name cinder-test  centos:7 init

curl -u admin:brysjhhrhl356126155165352237656123565615 -o get-pip.py  http://192.168.63.100:50000/remote.php/webdav/python/get-pip.py

python2 get-pip.py  -i  https://pypi.tuna.tsinghua.edu.cn/simple  

rsync -a -v -e ssh  --exclude='*.pyc'  --exclude='*.pyo'  --exclude='.tox/' --exclude='.testrepository/'   /root/my_proj/cinder  root@192.168.166.15:/root/kk/

docker cp /root/kk/cinder cinder-test:/
docker cp /root/packages cinder-test:/

curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

yum install epel-release -y

yum install gcc git python-devel  libxslt  nginx -y

配置 代理 /packages 目录


pip install tox==2.4.1 -i  https://pypi.tuna.tsinghua.edu.cn/simple     https://pypi.org/simple

tox -e py27 -- cinder.tests.unit


```