# 创建虚机


```bash

示例1
nova boot --flavor 4 --poll --block-device source=image,id=2d0ce29e-f71e-4c80-9f99-4f178f028a08,dest=volume,size=80,shutdown=remove,bootindex=0   --volume_type performance autovm002


示例2
nova boot --flavor 4 --poll --block-device source=image,id=2d0ce29e-f71e-4c80-9f99-4f178f028a08,dest=volume,size=80,shutdown=remove,bootindex=0   --volume_type performance  --admin-pass root  --nic net-name=perform,v4-fixed-ip=192.168.162.100   auto_lmk_cen7_100


3
 93ccaf27-0baf-4e62-8954-fca45d92fadc
nova boot --flavor 4 --poll --block-device source=image,id=93ccaf27-0baf-4e62-8954-fca45d92fadc,dest=volume,size=80,shutdown=remove,bootindex=0   --volume_type normal  --admin-pass root  --nic net-name=ex163,v4-fixed-ip=192.168.163.200   pxe_server

nova force-delete   pxe_server

```

规格id  通过 nova flavor-list 查看 
--flavor 4 

等待创建完成
--poll

启动镜像的类型以及 id 以及 大小 ，可以通过 nova image-list 查看
--block-device source=image,id=2d0ce29e-f71e-4c80-9f99-4f178f028a08,dest=volume,size=80,shutdown=remove,bootindex=0  

存储卷类型 cinder type-list 查看
--volume_type performance


密码
--admin-pass <value>          Admin password for the instance.

固定ip  可以通过 nova  net-list  查看
--nic net-name=perform,v4-fixed-ip=192.168.162.30


# 创建 指定 ip 的 虚机 以及 自定义 密码
```bash

nova boot --flavor 4 --poll --block-device source=image,id=2d0ce29e-f71e-4c80-9f99-4f178f028a08,dest=volume,size=80,shutdown=remove,bootindex=0   --volume_type performance  --admin-pass root  --nic net-name=perform,v4-fixed-ip=192.168.162.30   autovm_lmk_centos7_30


```


# 删除虚机
```bash

# 删除指定 名称
for server_name in  autovm001 autovm002;do nova delete ${server_name} ; done 

# 查看所有租户
nova list --all-tenants 1

# 正则  软删除 删除 虚机
nova  list | awk '{print $2}' | grep -v ID | grep -E '^.+$' | xargs -I {}  nova delete {} 


# 正则 彻底删除
nova  list | awk '{print $2}' | grep -v ID | grep -E '^.+$' | xargs -I {}  force-delete

```

# 查看网络
nova net-list
+--------------------------------------+---------+------+
| ID                                   | Label   | CIDR |
+--------------------------------------+---------+------+
| 0dc20660-2585-44d0-8986-5f27fc758bf6 | test    | None |
| 4e99b307-1900-42d8-b7b3-11e06fe7bb3b | perform | None |
+--------------------------------------+---------+------+


# 草稿本
```bash

nova boot --flavor 4 --poll --block-device source=image,id=2d0ce29e-f71e-4c80-9f99-4f178f028a08,dest=volume,size=80,shutdown=remove,bootindex=0   --volume_type performance autovm_lmk_centos7



nova boot --flavor 4 --poll --block-device source=image,id=2d0ce29e-f71e-4c80-9f99-4f178f028a08,dest=volume,size=80,shutdown=remove,bootindex=0   --volume_type performance  --admin-pass root  --access-ip-v4 192.168.162.20   autovm_lmk_centos7_20

--nic <net-id=net-uuid,net-name=network-name,v4-fixed-ip=ip-addr,v6-fixed-ip=ip-addr,port-id=port-uuid>


nova boot --flavor 4 --poll --block-device source=image,id=2d0ce29e-f71e-4c80-9f99-4f178f028a08,dest=volume,size=80,shutdown=remove,bootindex=0   --volume_type performance  --admin-pass root  --nic net-name=ex163,v4-fixed-ip=192.168.162.30   autovm_lmk_centos7_30


```

