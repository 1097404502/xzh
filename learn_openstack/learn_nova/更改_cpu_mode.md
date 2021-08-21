
# 更改 cpu mode ，风险 操作

不清楚 影响的 不要 随便执行
```bash


sed -i 's/cpu_mode = custom/cpu_mode = host-passthrough/g'  /etc/nova/nova.conf
sed -i 's/cpu_model = EPYC//g'  /etc/nova/nova.conf
sed -i 's/cpu_model = SandyBridge/# cpu_model = SandyBridge/g'  /etc/nova/nova.conf




function restart_service(){
  systemctl restart ${1}
}

for i in 'openstack-nova-compute.service' 'openstack-nova-scheduler.service'
do
   restart_service ${i} &
done
wait



```


