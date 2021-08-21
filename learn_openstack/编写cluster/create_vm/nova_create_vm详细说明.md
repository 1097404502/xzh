
# 批量创建 虚机
手动 在云平台上传虚机 速度十分有限 批量任务必须使用  批量脚本 来进行创建

```bash
1. 获得授权
. ~/admin-openrc

2. 创建 风味( 规格 )
首先 查看 已有规格
nova flavor-list
...
| 4  | m1.large  | 8192      | 80   | 0         |      | 4     | 1.0         | True

都不合适的话 ，自定义一个规格 


3. 查看 所有的 可用的 image os
nova image-list
+--------------------------------------+----------------+--------+--------+
| ID                                   | Name           | Status | Server |
+--------------------------------------+----------------+--------+--------+
| 59450e19-6a27-4291-8f4d-47c52d768062 | Zettakit-tools | ACTIVE |        |
| 2d0ce29e-f71e-4c80-9f99-4f178f028a08 | centos7_免安装 | ACTIVE |        |

4. 创建虚拟机
nova boot --flavor 4 --poll --block-device source=image,id=2d0ce29e-f71e-4c80-9f99-4f178f028a08,dest=volume,size=80,shutdown=remove,bootindex=0   --volume_type performance autovm002

截止到此 虚机已经可以通过网页 vnc 可视化 访问了
user： root
pwd:   zettakit



5. 绑定额外 的 存储卷
cinder create --volume-type performance  --name autovolume001 80

6.绑定 volume
nova volume-attach ${vm_name}-$i  vlume_name

vol_name=autovolume001
cinder list | grep ${vol_name}  | awk '{print $2}' | xargs nova volume-attach autovm001


```

# 创建 虚拟磁盘 卷
```bash

1. 查看可用的 磁盘类型
 cinder type-list
+--------------------------------------+-------------+-------------+-----------+
|                  ID                  |     Name    | Description | Is_Public |
+--------------------------------------+-------------+-------------+-----------+
| 4dd7395c-4ad2-45df-8fe9-a321a678b08b | performance |      -      |    True   |
| a05ba102-a1cf-4417-bf4a-087258d24d78 |    normal   |      -      |    True   |
+--------------------------------------+-------------+-------------+-----------+

2. 创建一个 存储卷
cinder create --volume-type performance  --name autovolume001 80

```

# demo

```bash

# 创建存储卷
cinder create --volume-type $volume_type  --name ${vm_name}-$i-vol$j $ebs_size

# 创建虚拟机
nova boot --flavor $redisserverflavor --poll --block-device source=image,id=$imageid,dest=volume,size=$vol_size,shutdown=remove,bootindex=0  ${vm_name}-$1


--poll                        Report the new server boot progress until it
                                completes.

```
