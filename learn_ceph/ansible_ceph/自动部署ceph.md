# 国外镜像

git clone https://github.com/ceph/ceph-ansible.git
# 我的 国内链接

git@code.aliyun.com:734449600/ceph-ansible.git

remote set-url --add <name> <newurl>

git remote add origin git@code.aliyun.com:734449600/ceph-ansible.git

# 使用 我的 仓库 安装 ceph14
```bash

git clone -b  stable-4.0 https://code.aliyun.com/734449600/ceph-ansible.git

pip install -r requirements.txt

yum install ansible

# host net /etc/ansible/hosts
cat > /etc/ansible/hosts  <<"EOF"
[mons]
192.168.170.201
192.168.170.202
192.168.170.203


[osds]
192.168.170.201
192.168.170.202
192.168.170.203



```

# 安装 ceph
```bash

# 修改主机名
hostnamectl set-hostname  node1

setenforce 0
sed -i  "s/SELINUX=enforcing/SELINUX=permissive/g" /etc/selinux/config
systemctl disable firewalld.service
systemctl stop firewalld.service


# 修改 源
yum -y install epel-release centos-release-ceph-nautilus centos-release-openstack-stein


cat <<"EOF" > /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
192.168.170.201 node1
192.168.170.202 node2
192.168.170.203 node3
EOF

# 
yum -y install ceph-ansible


cat  > /usr/share/ceph-ansible/group_vars/all.yml <<"EOF"
ceph_origin: repository
ceph_repository: community
ceph_mirror: http://mirrors.aliyun.com/ceph
ceph_stable_key: http://mirrors.aliyun.com/ceph/keys/release.asc
ceph_stable_release: nautilus
ceph_stable_repo: "{{ ceph_mirror }}/rpm-{{ ceph_stable_release }}"
public_network: 192.168.170.0/24
cluster_network: "{{ public_network }}"
monitor_interface: eth0

EOF


cat > /usr/share/ceph-ansible/group_vars/osds.yml  << "EOF"
devices:
  - /dev/vdb
  - /dev/vdc
  - /dev/vdd

EOF



cat >  /etc/ansible/hosts < ""
[all:vars]
ansible_connection=ssh
ansible_ssh_pass='root@zetta'
dashboard_admin_password='root@zetta' 
grafana_admin_password='root@zetta'
[mons]
node1
node2
node3
[mgrs]
node1
node2
node3
[osds]
node1
node2
node3
[grafana_server_group_name] 
node1
[grafana-server]
node1
[rgws]
node1
node2
node3
[mdss]
node1
node2
node3

EOF


cd /usr/share/ceph-ansible
cp -p site.yml.sample site.yml

vi site.yml
- hosts:
  - mons
  #- agents
  - osds
  #- mdss
  #- rgws
  #- nfss
  #- restapis
  #- rbdmirrors
  #- clients
  - mgrs
  #- iscsigws
  #- iscsi-gws # for backward compatibility only!

echo -e 'radosgw_interface: eth0 ' > /usr/share/ceph-ansible/group_vars/rgws.yml


# 开始安装
cd /usr/share/ceph-ansible
ansible-playbook site.yml



```

完成安装 查看页面
```bash

# ceph mgr services
{
    "dashboard": "http://192.168.80.91:8443/",
    "prometheus": "http://node2:9283/"
}

```

