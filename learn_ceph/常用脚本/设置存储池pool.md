
# 并发 设置 pool size

```bash

# default_size='2'
default_size='1'
for _p in `ceph osd pool ls`
do
  for var_name in 'size' 
  do 
    /bin/bash -c "ceph osd pool  set  ${_p} ${var_name} ${default_size} &"
  done
done
wait



default_size='1'
for _p in `ceph osd pool ls`
do
  for var_name in  'min_size'
  do 
    /bin/bash -c "ceph osd pool  set  ${_p} ${var_name} ${default_size} &"
  done
done
wait



```