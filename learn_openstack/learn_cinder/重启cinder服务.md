
# 重启 cinder 服务
```bash


function restart_service(){
  systemctl restart openstack-cinder-${1}
}

for i in "volume" "scheduler" "api" "backup" ;
do
  restart_service ${i} &
done 


```