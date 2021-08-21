[toc]
# 文档
https://docs.openstack.org/kolla-ansible/latest/user/quickstart.html

https://docs.openstack.org/kolla-ansible/latest/user/troubleshooting.html

# 安装 操作系统
我选择 ubuntu20.04
# Install dependencies
```bash

hostname node01

echo -e '\n192.168.199.10 node01' >> /etc/hosts

echo 'nameserver 114.114.114.114' > /etc/resolv.conf

cat >  /etc/apt/sources.list <<"EOF"
deb http://repo.huaweicloud.com/ubuntu/ focal main restricted
deb http://repo.huaweicloud.com/ubuntu/ focal-updates main restricted
deb http://repo.huaweicloud.com/ubuntu/ focal universe
deb http://repo.huaweicloud.com/ubuntu/ focal-updates universe
deb http://repo.huaweicloud.com/ubuntu/ focal multiverse
deb http://repo.huaweicloud.com/ubuntu/ focal-updates multiverse
deb http://repo.huaweicloud.com/ubuntu/ focal-backports main restricted universe multiverse
deb http://repo.huaweicloud.com/ubuntu/ focal-security main restricted
deb http://repo.huaweicloud.com/ubuntu/ focal-security universe
deb http://repo.huaweicloud.com/ubuntu/ focal-security multiverse
EOF

apt update -y
# apt upgrade -y

apt install python3-dev libffi-dev gcc libssl-dev  python3-venv python3-pip   docker.io -y

```

# Install dependencies using a virtual environment

```bash

# 除了虚拟环境 本机 也需要 安装
pip install docker

venv_path='/py3_env'
mkdir -p ${venv_path}

python3 -m venv ${venv_path}
source ${venv_path}/bin/activate

pip config set global.index-url https://mirrors.aliyun.com/pypi/simple

pip install -U pip

pip install 'ansible<2.10'

```

# install kolla-ansible
```bash

venv_path='/py3_env'
source ${venv_path}/bin/activate

pip install kolla-ansible

sudo mkdir -p /etc/kolla
sudo chown $USER:$USER /etc/kolla

cd /etc/kolla

cp -r ${venv_path}/share/kolla-ansible/etc_examples/kolla/* /etc/kolla


cp  ${venv_path}/share/kolla-ansible/ansible/inventory/* .


```

# config ansiable
```bash

mkdir -p  /etc/ansible

cat > /etc/ansible/ansible.cfg <<"EOF"

[defaults]
host_key_checking=False
pipelining=True
forks=100

EOF


```

# prepare deploy all-in-one
```bash
# check
ansible -i all-in-one all -m ping

kolla-genpwd

ll  /etc/kolla/

cat /etc/kolla/passwords.yml


vi   /etc/kolla/globals.yml

kolla_base_distro: "ubuntu"
network_interface: "eth0"
neutron_external_interface: "eth1"
kolla_internal_vip_address: "192.168.199.250"

net_prefix='192.168.164'
virtual_ip='192.168.164.250'
neutron port-list | grep -E ${net_prefix}  | awk '{print $2}' | xargs -I {} neutron port-update {} --allowed-address-pair ip_address=${virtual_ip}


cat > /etc/kolla/globals.yml <<EOF
---
kolla_base_distro: "ubuntu"
openstack_release: "victoria"
network_interface: "ens3"
neutron_external_interface: "ens15"
kolla_internal_vip_address: "${virtual_ip}"
EOF

# 可选
enable_redis: "yes"
enable_cinder: "yes"
docker_registry: "192.168.1.100:4000"

# 任选一种
enable_cinder_backend_lvm: "yes"
#enable_cinder_backend_nfs: "no"
#enable_cinder_backend_zfssa_iscsi: "no"
#enable_cinder_backend_quobyte: "no"

```

# use cinder lvm
```bash

pvcreate /dev/sdb /dev/sdc
vgcreate cinder-volumes /dev/sdb /dev/sdc

# 查看
vgs

# 请修改  根据 实际配置
if_1='ens3'
if_2='ens4'
virtual_ip='192.168.199.250'
registry_url='192.168.164.200:5000'

cat > /etc/kolla/globals.yml <<EOF
---
kolla_base_distro: "ubuntu"
openstack_release: "victoria"
network_interface: "${if_1}"
neutron_external_interface: "${if_2}"
kolla_internal_vip_address: "${virtual_ip}"
enable_redis: "yes"
enable_cinder: "yes"
enable_cinder_backend_lvm: "yes"
docker_registry: "${registry_url}"
EOF




```

# deplay all-in-one
```bash

venv_path='/py3_env'
source ${venv_path}/bin/activate




# Bootstrap servers with kolla deploy dependencies:
# 执行之后 docker 等 依赖环境会被删除
# !!!! 类似 环境 重置.  也可以 用来 裸os 自动 安装 依赖环境
# !!!!
kolla-ansible -i ./all-in-one bootstrap-servers

# gen pwd
# Do pre-deployment checks for hosts:
# Finally proceed to actual OpenStack deployment:
kolla-genpwd
kolla-ansible -i ./all-in-one prechecks
kolla-ansible -i ./all-in-one deploy

# 生成 授权 文件
kolla-ansible post-deploy

# pull images  if  deploy net is not fast
# 如果使用 私有 镜像源 也可以跳过这一步
kolla-ansible pull


# 停止 continer , 运行状态 占用 内存 太高.
kolla-ansible stop  --yes-i-really-really-mean-it

```

# cli 访问openstack
```bash
venv_path='/py3_env'
source ${venv_path}/bin/activate


# 生成 授权 文件
kolla-ansible post-deploy
. /etc/kolla/admin-openrc.sh

# 废弃
# pip install python3-openstackclient

pip install python-openstackclient



```

# 查看 账号密码 访问 服务

192.168.199.250

```bash

cat  /etc/kolla/admin-openrc.sh
export OS_USERNAME=admin
export OS_PASSWORD=i8PMCjPWYyGipI8cdyv3kiziNvI7TcrUfTpHejxI

# ubuntu image
http://192.168.63.100:50000/index.php/s/H7Vz7OgzsoTLlTu/download

```

# 可选服务()
```bash

enable_redis: "yes"
enable_cinder: "yes"

```

# bug
```bash
package_path="/py3_env/lib/python3.8/site-packages"

# (things that weren't automatically removed)

pip3 uninstall ansible
rm -rf  ${package_path}/ansible 
pip install 'ansible<2.10'

```

# cinder error
```bash

TASK [cinder : Checking at least one valid backend is enabled for Cinder] ***********************************************************************
fatal: [localhost]: FAILED! => {"changed": false, "msg": "Please enable at least one backend when enabling Cinder"}

fix: enable_cinder_backend_lvm: "yes"

# 

TASK [cinder : Checking LVM volume group exists for Cinder] *************************************************************************************fatal: [localhost]: FAILED! => {"changed": false, "cmd": ["vgs", "cinder-volumes"], "delta": "0:00:00.077736", "end": "2021-06-10 16:28:21.840556", "failed_when_result": true, "msg": "non-zero return code", "rc": 5, "start": "2021-06-10 16:28:21.762820", "stderr": "  Volume group \"cinder-volumes\" not found\n  Cannot process volume group cinder-volumes", "stderr_lines": ["  Volume group \"cinder-volumes\" not found", "  Cannot process volume group cinder-volumes"], "stdout": "", "stdout_lines": []}

https://docs.openstack.org/kolla-ansible/latest/reference/storage/cinder-guide.html

pvcreate /dev/sdb /dev/sdc
vgcreate cinder-volumes /dev/sdb /dev/sdc

# 查看
vgs

```

## 网络问题
```bash

mkdir -p /etc/docker
tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://registry.docker-cn.com"]
}
EOF
systemctl restart docker

```

```bash
RUNNING HANDLER [Restart neutron-dhcp-agent container] **************************************************************************************************************
fatal: [localhost]: FAILED! => {"changed": true, "msg": "'Traceback (most recent call last):\\n  File \"/usr/lib/python3.8/site-packages/docker/api/client.py\", line 268, in _raise_for_status\\n    response.raise_for_status()\\n  File \"/usr/lib/python3/dist-packages/requests/models.py\", line 940, in raise_for_status\\n    raise HTTPError(http_error_msg, response=self)\\nrequests.exceptions.HTTPError: 500 Server Error: Internal Server Error for url: http+docker://localhost/v1.41/images/create?tag=victoria&fromImage=kolla%2Fubuntu-binary-neutron-dhcp-agent\\n\\nDuring handling of the above exception, another exception occurred:\\n\\nTraceback (most recent call last):\\n  File \"/tmp/ansible_kolla_docker_payload_ihgh7llq/ansible_kolla_docker_payload.zip/ansible/modules/kolla_docker.py\", line 1131, in main\\n  File \"/tmp/ansible_kolla_docker_payload_ihgh7llq/ansible_kolla_docker_payload.zip/ansible/modules/kolla_docker.py\", line 785, in recreate_or_restart_container\\n  File \"/tmp/ansible_kolla_docker_payload_ihgh7llq/ansible_kolla_docker_payload.zip/ansible/modules/kolla_docker.py\", line 803, in start_container\\n  File \"/tmp/ansible_kolla_docker_payload_ihgh7llq/ansible_kolla_docker_payload.zip/ansible/modules/kolla_docker.py\", line 601, in pull_image\\n  File \"/usr/lib/python3.8/site-packages/docker/api/image.py\", line 430, in pull\\n    self._raise_for_status(response)\\n  File \"/usr/lib/python3.8/site-packages/docker/api/client.py\", line 270, in _raise_for_status\\n    raise create_api_error_from_http_exception(e)\\n  File \"/usr/lib/python3.8/site-packages/docker/errors.py\", line 31, in create_api_error_from_http_exception\\n    raise cls(e, response=response, explanation=explanation)\\ndocker.errors.APIError: 500 Server Error for http+docker://localhost/v1.41/images/create?tag=victoria&fromImage=kolla%2Fubuntu-binary-neutron-dhcp-agent: Internal Server Error (\"Get https://registry-1.docker.io/v2/: net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)\")\\n'"}
```