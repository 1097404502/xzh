# 同步 代码 到集群当中

## 开发机 同步代码 到 node1
```bash

cinder_test_ip='192.168.166.151'
code_path='/usr/lib/python2.7/site-packages/cinder/'
# 先回退版本 到 没有 引入 backend mgr 之前 的 状态
rsync -a -v -e ssh  --exclude='*.pyc'  --exclude='*.pyo'  --exclude='.tox/' --exclude='.testrepository/'   /root/my_proj/cinder/cinder/  root@${cinder_test_ip}:${code_path}


```

## node1 分发代码 到其他节点

```bash

root_wrap_path='/usr/share/os-brick/rootwrap/os-brick.filters'

# 添加 额外的 权限
vi '/usr/share/os-brick/rootwrap/os-brick.filters' 

for i  in `seq 2 5 `;do rsync -avz ${root_wrap_path}  root@192.168.166.15${i}:${root_wrap_path} ;done

for i  in `seq 2 5 `;do rsync -avz ${code_path}  root@192.168.166.15${i}:${code_path} ;done

for i  in `seq 1 2`;do ssh  root@192.168.166.15${i}  'for i in "volume" "scheduler" "api" "backup" ;do /bin/bash -c "systemctl restart openstack-cinder-${i} &"  ;done ' ;done ; wait


```
