# Libvirt主要支持三种 CPU mode：

## host-passthrough
: libvirt 令 KVM 把宿主机的 CPU 指令集全部透传给虚拟机。因此虚拟机能够最大限度的使用宿主机 CPU 指令集，故性能是最好的。但是在热迁移时，它要求目的节点的 CPU 和源节点的一致。
## host-model
: libvirt 根据当前宿主机 CPU 指令集从配置文件 /usr/share/libvirt/cpu_map.xml 选择一种最相配的 CPU 型号。在这种 mode 下，虚拟机的指令集往往比宿主机少，性能相对 host-passthrough 要差一点，但是热迁移时，它允许目的节点 CPU 和源节点的存在一定的差异。
## custom
:这种模式下虚拟机 CPU 指令集数最少，故性能相对最差，但是它在热迁移时跨不同型号 CPU 的能力最强。此外，custom 模式下支持用户添加额外的指令集。
三种mode的性能排序是：host-passthrough > host-model > custom
三种mode的热迁移通用性是： custom > host-model > host-passthrough


# 修改 nova cpu mode
```bash

# cat /etc/nova/nova.conf | grep cpu_mode
cpu_mode = custom


sed -i 's/cpu_mode = custom/cpu_mode = host-passthrough/g'  /etc/nova/nova.conf

cpu_mode = custom
cpu_model = SandyBridge



sed -i 's/cpu_mode = custom/cpu_mode = host-passthrough/g'  /etc/nova/nova.conf
sed -i 's/cpu_model = SandyBridge//g'  /etc/nova/nova.conf



./sp/all_do.sh "sed -i 's/cpu_mode = custom/cpu_mode = host-passthrough/g'  /etc/nova/nova.conf"

./sp/all_do.sh "sed -i 's/cpu_model = SandyBridge//g'  /etc/nova/nova.conf"

./sp/all_do.sh "systemctl restart openstack-nova-compute "




grep  "cpu_" nova.conf
cpu_allocation_ratio = 3.0
enable_cpu_pin = false
cpu_mode = custom
cpu_model = EPYC


sed -i 's/cpu_mode = custom/cpu_mode = host-passthrough/g'  /etc/nova/nova.conf

sed -i 's/cpu_model = EPYC//g'  /etc/nova/nova.conf

sed -i 's/cpu_mode = custom/cpu_mode = host-passthrough/g'  /etc/nova/nova.conf.bak

sed -i 's/cpu_model = EPYC//g'  /etc/nova/nova.conf.bak

grep "cpu_"  /etc/nova/nova.conf


sed  's/cpu_allocation_ratio/cpu_allocation_ratio = 50.0 \n# cpu_allocation_ratio /g'  /etc/nova/nova.conf

# 进入虚机 查看 是否打开
cat /proc/cpuinfo |grep -ioE 'vmx|svm'

```


# 修改 adm   epyc 嵌套虚拟化
```bash
sed -i 's/cpu_mode = custom/cpu_mode = host-passthrough/g'  /etc/nova/nova.conf
sed -i 's/cpu_model = EPYC//g'  /etc/nova/nova.conf
```

```bash
修改回来

./sp/all_do.sh "sed -i 's/cpu_mode = host-passthrough/cpu_mode = custom/g'  /etc/nova/nova.conf"
./sp/all_do.sh "systemctl restart openstack-nova-compute "
 
 /var/log/nova/

grep -E "`date -I`.*ERROR" /var/log/nova/nova-compute.log
```

# 日志报错
```bash
 Invalid: A CPU model name should not be set when a host CPU model is requested
2021-01-21 15:58:20.007 1129190 ERROR nova.compute.manager [instance: a2178c64-2913-402e-a48f-ffef5e705b3d] 

```


# xml 被限制
```bash
ls /usr/share/libvirt/schemas

```

# 虚机启动之后修改 cpu mode
```bash
virsh edit instance-00000007

 2     instance-00000568              running


virsh shutdown  instance-00000568
修改

<cpu mode='custom' match='exact' check='partial'>

<cpu mode='custom' match='exact' check='partial'>
  <model fallback='allow'>SandyBridge</model>
  <topology sockets='64' cores='1' threads='2'/>
  <numa>
    <cell id='0' cpus='0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,65       <cell id='1' cpus='1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61     66     </numa>
</cpu>


 <numa>
     64       <cell id='0' cpus='0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,9
     65       <cell id='1' cpus='1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93,95,9
     66     </numa>



<cpu mode='host-passthrough' match='exact' check='partial'>
  <topology sockets='64' cores='1' threads='2'/>
  <numa>
    <cell id='0' cpus='0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60     65       <cell id='1' cpus='1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61     66     </numa>
</cpu>

virsh start  instance-00000568

i 忽略错误

```

# virsh commend
```bash

编辑：virsh edit 

定义：virsh define xxx.xml xxx为xml文件所在的路径及文件名称，在当前目录下则不写路径

启动：virsh start xyz xyz为虚拟机xml配置文件中虚拟机的名字<name>rhel6.2_2</name>

停止：virsh shutdownxyz 此方法为正常关机方法，需要一段才能关机

下电：virsh destroy xyz 此方法为暴力下电，虚拟机立即关闭

删除：virsh undefinexxx 关闭了的虚拟机，只是不在运行状态而已，通过virsh undefine xxx就能从virsh列表里面（virsh list查看当前系统中的虚拟机列表，详见第2.4节）将其删除，undefine命令不会删除镜像文件和xml文件。运行状态的虚拟机是不能删除的。

临时起虚拟机：virsh create xxx.xml 此方法为方便开发调试等临时需求，不会持久化，虚拟机关机后就消失了，不推荐生产系统使用。

查看VNC端口：virshvncdisplay xx 查看VNC端口，其中xx可通过virsh list查看
```

# 发现 nova 一直被 定时 修改

```bash

echo "nameserver 114.114.114.114" > /etc/resolv.conf

/bin/cp -a /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak

curl -o  /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

yum clean all
yum makecache


aditctl -w /root/.ssh/authorized_keys -p war -k auth_key

-w 指明要监控的文件
-p awrx 要监控的操作类型，append, write, read, execute
-k 给当前这条监控规则起个名字，方便搜索过滤
查看修改纪录：ausearch -i -k auth_key，生成报表 aureport.
```
