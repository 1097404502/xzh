# 使用 导出 镜像的 脚本
```bash


curl -o pack_and_download_vm_by_name.sh http://192.168.63.100:50000/index.php/s/AAJeGvxyb3xO34S/download


demo1:
  仅测试导出是否正常执行
 ./pack_and_download_vm_by_name.sh "kk开发" "/images/centos7_docker.qcow2"

demo2:
  推荐的 导出方式
 nohup /root/sp/pack_and_download_vm_by_name.sh  "kk开发" "/images/centos7_docker.qcow2" 2>&1 > ./revert.log &


# 导出 安装好的 zcloud
nohup /root/sp/pack_and_download_vm_by_name.sh  "zcloud" "/images/zcloud_v30_05_07.qcow2" 2>&1 > ./revert.log &

```