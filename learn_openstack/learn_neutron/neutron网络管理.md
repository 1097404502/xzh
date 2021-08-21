[toc]
# 创建and删除子网
```bash

neutron subnet-list

neutron subnet-delete 150511d7-f80a-45b1-ad7c-272801132756
neutron CLI is deprecated and will be removed in the future. Use openstack CLI instead.
Unable to complete operation on subnet 150511d7-f80a-45b1-ad7c-272801132756: One or more ports have an IP allocation from this subnet.
Neutron server returns request_ids: ['req-e2542e8e-4607-45ff-8e51-963bf0ae9a0a']

neutron port-delete 47f27dfa-ecd8-4d85-93d4-877e5fb02689
Port 47f27dfa-ecd8-4d85-93d4-877e5fb02689 cannot be deleted directly via the port API: has device owner  network:router_interface_distributed.


```

# 查看接口信息 ，并根据 ip 批量删除 接口
```bash
neutron port-list 2>&1 | grep "192.168.150"  |  grep -v "neutron" | awk '{print $2}' | neutron port-delete

 neutron port-list 2>&1 | grep "192.168.151"  |  grep -v "neutron" | awk '{print $2}' | xargs neutron port-delete
```

# neutron 模块学习

/home/lmk/codes/neutron/neutron/agent/l3/ha_router.py

/home/lmk/codes/neutron/neutron/agent/linux/keepalived.py