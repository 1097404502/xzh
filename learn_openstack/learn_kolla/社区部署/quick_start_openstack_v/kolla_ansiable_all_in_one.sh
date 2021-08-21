
# 前提 条件 
#  两张 网卡
#  三个 存储盘 , 其中 一个 做系统 两个 作为 cinder lvm
#  ubuntu20 os

# config  args
host_ip='192.168.199.10'
host_name='node01'

data_disks_path='/dev/sdb   /dev/sdc'

if_1='ens3'
if_2='ens4'
virtual_ip='192.168.199.250'
registry_url='192.168.164.200:5000'


function init_host_net(){

hostname ${host_name}

echo -e "\n${host_ip} ${host_name}" >> /etc/hosts

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
}


function create_vg(){
  pvcreate ${data_disks_path}
  vgcreate cinder-volumes ${data_disks_path}
  # 查看
  vgs
}


function install_dependency(){
    apt install python3-dev libffi-dev gcc libssl-dev  python3-venv python3-pip   docker.io -y
    pip install docker
    venv_path='/py3_env'
    mkdir -p ${venv_path}
    python3 -m venv ${venv_path}
    source ${venv_path}/bin/activate
    pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
    pip install -U pip
    # Name: ansible  Version: 2.9.22
    # Name: kolla-ansible Version: 11.0.0
    pip install 'ansible<2.10'
    pip install  'kolla-ansible<=11.0.0'
    sudo mkdir -p /etc/kolla
    sudo chown $USER:$USER /etc/kolla
    cd /etc/kolla
    cp -r ${venv_path}/share/kolla-ansible/etc_examples/kolla/* /etc/kolla
    cp  ${venv_path}/share/kolla-ansible/ansible/inventory/* .


mkdir -p  /etc/docker/
cat > /etc/docker/daemon.json <<EOF
{
    "log-level":        "error",
    "storage-driver":   "overlay2",
    "insecure-registries": ["${registry_url}"]
}
EOF

systemctl enable docker
systemctl daemon-reload
systemctl restart docker


}

function config_ansiable(){
mkdir -p  /etc/ansible
cat > /etc/ansible/ansible.cfg <<"EOF"
[defaults]
host_key_checking=False
pipelining=True
forks=100
EOF
}

function config_kolla(){
cd /etc/kolla
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
}

function kolla_deploy(){
venv_path='/py3_env'
source ${venv_path}/bin/activate

kolla-genpwd
kolla-ansible -i ./all-in-one prechecks
kolla-ansible -i ./all-in-one deploy

# 生成 授权 文件
kolla-ansible post-deploy

pip install python-openstackclient
}

init_host_net
create_vg
install_dependency
config_ansiable
config_kolla
kolla_deploy




