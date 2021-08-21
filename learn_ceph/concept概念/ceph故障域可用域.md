
# 什么是故障域

相当于一种安全范围,
比如 有几种 灾难 分别会 摧毁 星球，大陆，国家。

那么对于 星球灾难来讲，地球 只有一个可用域。
对于 大陆级灾难 地球 有 6 块大陆 ， 所以 可用域是 6。

对于 国家级灾难讲， 地球 拥有 200多个 可用域。
懂了吗。

# crush 常用命令
ceph osd crush rule dump  < replicated_rule : rulename>

ceph osd crush tree 

ceph osd crush tree --verbose

--verbose 可以查看到 命令字典。
--format json 可以查看到 json 输出。

## 查看 crush rule
```bash
ceph osd crush rule dump replicated_rule

{
    "rule_id": 0,
    "rule_name": "replicated_rule",
    "ruleset": 0,
    "type": 1,
    "min_size": 1,
    "max_size": 10,
    "steps": [
        {
            "op": "take",
            "item": -1,
            "item_name": "default"
        },
        {
            "op": "chooseleaf_firstn",
            "num": 0,
            "type": "host"
        },
        {
            "op": "emit"
        }
    ]
}


```

## 查看 crush tree 
```bash
ceph osd crush tree 
ID  CLASS  WEIGHT   TYPE NAME                    
-1         0.15619  root default                 
-9         0.04880      host host-192-168-141-140
 3    hdd  0.04880          osd.3                
-3         0.04880      host host20              
 0    hdd  0.04880          osd.0                
-5         0.02930      host host23              
 1    hdd  0.02930          osd.1                
-7         0.02930      host host24              
 2    hdd  0.02930          osd.2   

ceph osd crush tree  --format json
-->
{"nodes":[{"id":-1,"name":"default","type":"root","type_id":11,"children":[-7,-5,-3,-9]},{"id":-9,"name":"host-192-168-141-140","type":"host","type_id":1,"pool_weights":{},"children":[3]},{"id":3,"device_class":"hdd","name":"osd.3","type":"osd","type_id":0,"crush_weight":0.048797607421875,"depth":2,"pool_weights":{}},{"id":-3,"name":"host20","type":"host","type_id":1,"pool_weights":{},"children":[0]},{"id":0,"device_class":"hdd","name":"osd.0","type":"osd","type_id":0,"crush_weight":0.048797607421875,"depth":2,"pool_weights":{}},{"id":-5,"name":"host23","type":"host","type_id":1,"pool_weights":{},"children":[1]},{"id":1,"device_class":"hdd","name":"osd.1","type":"osd","type_id":0,"crush_weight":0.029296875,"depth":2,"pool_weights":{}},{"id":-7,"name":"host24","type":"host","type_id":1,"pool_weights":{},"children":[2]},{"id":2,"device_class":"hdd","name":"osd.2","type":"osd","type_id":0,"crush_weight":0.029296875,"depth":2,"pool_weights":{}}],"stray":[]}

```