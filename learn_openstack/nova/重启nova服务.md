# 重启 nova 服务
```bash


sed   -i   's/virt_type = kvm/virt_type = qemu/g'  /etc/nova/nova.conf

systemctl | grep nova | awk '{print $1}' | xargs  systemctl restart

virsh console cvm --devname serial0

virsh console  instance-00000006   --devname serial1



```

