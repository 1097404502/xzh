# 初始化cinder 环境

```bash
cd /home/lmk/codes/cinder/ENV_py3/bin
source ./activate

```

# 可用的 cinder 命令
cinder-api     cinder-manage    cinder-rtstool    cinder-status  cinder-volume-usage-audit
cinder-backup  cinder-rootwrap  cinder-scheduler  cinder-volume  cinder-wsgi

# 41集群
192.168.41.1 - 3
192.168.41.10

admin
admin_pass

root@zetta

# 连接到 cinder 
```bash

 . admin-openrc

cat admin-openrc 

export OS_PROJECT_DOMAIN_NAME=default
export OS_USER_DOMAIN_NAME=default
export OS_PROJECT_NAME=ADMIN@INTERNAL
export OS_TENANT_NAME=ADMIN@INTERNAL
export OS_USERNAME=ADMIN@INTERNAL
export OS_PASSWORD=internal@zettakit.com
export OS_AUTH_URL=http://192.168.41.10:35357/v3
export OS_IDENTITY_API_VERSION=3
export OS_VOLUME_API_VERSION=2


```

# cinder 路径
```bash

/usr/lib/python2.7/site-packages/cinder

```

# 阅读cinder 代码

# cinder_old/cinder/volume/__init__.py

```bash

from oslo_utils import importutils

from cinder.common import config

CONF = config.CONF

def API(*args, **kwargs):
    class_name = CONF.volume_api_class
    return importutils.import_object(class_name, *args, **kwargs)

# 在 cinder_old/cinder/common/config.py 
# 找到的 对应的 class_name 的具体值
  cfg.StrOpt('volume_api_class',
               default='cinder.volume.api.API',

```

# 激活tox虚拟环境 并执行测试

```bash

source /root/codes/cinder/.tox/py27/bin/activate
cd /root/codes/cinder

python -m testtools.run /root/codes/cinder/cinder/tests/unit/volume/test_ceph_api.py


```

# 提交使用 英语
```bash

修复 overall_status 以及 id 字段错误,以及对应的ceph-api单元测试
cinder : fixed fields overall_status,id err for ceph-v14.
 And add corresponding unit test . 
```

# 重启进程
```bash

for i in 'openstack-cinder-api.service'        'openstack-cinder-backup.service'     'openstack-cinder-scheduler.service'  'openstack-cinder-volume.service'; do  systemctl restart $i & echo '' ;done ;wait

```

# 扩展云硬盘
```bash

扩容云硬盘失败：t3内部服务器错误: [Requested message version, 1.0 is incompatible. It needs to be equal in major version and less than or equal in minor version as the specified version cap 2.0.] .


```