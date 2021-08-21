
# 查看网卡 物理链路状态
```bash


 ip link | grep -i 'state up '
4: ens4f0: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc mq master bond0 state UP mode DEFAULT group default qlen 1000
8: bond0: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue master ovs-system state UP mode DEFAULT group default qlen 1000
9: vlan64@bond0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default qlen 1000


```

# 持久化 vf 网卡
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux_openstack_platform/7/html/networking_guide/sr-iov-support-for-virtual-networking

```bash

if_name='enp131s0f1'

echo 16 > /sys/class/net/${if_name}/device/sriov_numvfs
# However, this setting will not persist after a reboot. A possible workaround is to add this to rc.local, but this has its own limitation, as described in the note below:

chmod +x /etc/rc.local
echo "echo 16 > /sys/class/net/${if_name}/device/sriov_numvfs" >> /etc/rc.local


nova show zcloud_kk_ex199_11 | grep -ioE "instance-[a-z0-9]{7,}"

# 查看 vf slot 槽位
lshw -c network -businfo

# 挂载 vf 虚拟网卡
vm_name='ubuntu20_compose'

. ~/admin-openrc

instance_id=$( nova show  ${vm_name} | grep -ioE 'instance-[a-z0-9]{7,}' )

virsh autostart ${instance_id}

mkdir -p bind_device
cd ./bind_device

bus_no='85'
slot_no='10'

for function_no in '0' '2'
do

cat  > vf_device.xml <<EOF
<hostdev mode='subsystem' type='pci' managed='yes'>
      <source>
        <address domain='0x0000' bus='0x${bus_no}' slot='0x${slot_no}' function='0x${function_no}'/>
      </source>
</hostdev>
EOF

virsh attach-device ${instance_id} vf_device.xml --persistent  --live

done



# 卸载设备
virsh detach-device --domain ${instance_id}  vf_device.xml --persistent

```

# 信任vf网卡
```bash

ip link show ens3f0

1. 设置VF的mac地址：

ip link set dev ens3f0 vf 0 mac 82:cc:3d:3c:39:c7
2. 对指定的VF添加信任：

ip link set dev ens3f0 vf 0 trust on


ip link set dev p5p1 vf 4 trust on

This command enables trust on for Virtual Function 0 on Physical Device 'p5p1' and allows the VM to change the MAC address and enable multicast promiscuous mode on the VF.


```

# 查看网卡 信息

```bash

yum install lswh   -y


lshw -c network -businfo
Bus info          Device       Class          Description
=========================================================
pci@0000:01:00.0  enp1s0f0     network        Ethernet Controller 10-Gigabit X540-AT2
pci@0000:01:00.1  enp1s0f1     network        Ethernet Controller 10-Gigabit X540-AT2
pci@0000:82:00.0  ib0          network        MT27500 Family [ConnectX-3]
pci@0000:85:00.0  ens3f0       network        82599ES 10-Gigabit SFI/SFP+ Network Connection
pci@0000:85:00.1  ens3f1       network        82599ES 10-Gigabit SFI/SFP+ Network Connection
pci@0000:85:10.1               network        82599 Ethernet Controller Virtual Function
pci@0000:85:10.3  enp133s16f3  network        82599 Ethernet Controller Virtual Function
pci@0000:85:10.5  enp133s16f5  network        82599 Ethernet Controller Virtual Function
pci@0000:85:10.7  enp133s16f7  network        82599 Ethernet Controller Virtual Function
pci@0000:85:11.1  enp133s17f1  network        82599 Ethernet Controller Virtual Function


其中 0000:5e:12.0  分别对应 domain  bus 以及 slot


vm_name='zcloud_kk_iso_ex199_5'
nova show ${vm_name} | grep -i instance | awk '{print $4}'



virsh list  
2     instance-0000000d              running

virsh autostart ${instance_id}

virsh edit <name of virtual machine>

<hostdev mode='subsystem' type='pci' managed='yes'>
      <source>
        <address domain='0x0000' bus='0x01' slot='0x10' function='0x0'/>
      </source>
</hostdev>

virsh dump <name of virtual machine>


virsh destroy 

virsh start

```

# 直通设备接入

```bash


查看VF PCI的总线信息，也可以使用该脚本查看https://github.com/intel/SDN-NFV-Hands-on-Samples/blob/master/SR-IOV_Network_Virtual_Functions_in_KVM/listvfs_by_pf.sh

# lshw -c network -businfo
添加一个<hostdev>的tag到虚拟机。

通过上面的脚本将查看到的domain、bus、slot及function信息写入tag内。

# virsh edit <name of virtual machine>
# virsh dump <name of virtual machine>
<domain>
…
<devices>
…
<hostdev mode='subsystem' type='pci' managed='yes'>
      <source>
        <address domain='0x0000' bus='0x03' slot='0x10' function='0x0'/>
      </source>
</hostdev>
…
</devices>
…
</domain>
启动虚拟机。


```

# 修改虚机 xm

```bash

pci@0000:00:04.2  ens4f2          network        82599 Ethernet Controller Virtual Function


<hostdev mode='subsystem' type='pci' managed='yes'>
      <source>
        <address domain='0x0000' bus='0x00' slot='0x04' function='0x2'/>
      </source>
</hostdev>

```

