# 使用awk

## 查看所有存储池的 备份数目
```bash

ceph osd dump | grep 'replicated size' | awk  'BEGIN{ printf  "%-30s%-20s\n","pool_name","replic_count"  } { split($0,a," "); printf  "%-30s%-20s\n",a[3],a[6]; }' | grep -v "^pool\b"


pool_name                     replic_count        
'device_health_metrics'       3                   
'cephfs_data'                 3                   
'cephfs_metadata'             3                   
'cephfs2_metadata'            3    

```

