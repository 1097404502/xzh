

# docker 使用 http http_proxy
```bash
https://docs.docker.com/config/daemon/systemd/

# 代理 和  国内 镜像源 不要 同时使用，。。。

# "storage-driver":   "overlay2",


apt install docker.io -y

proxy_url='172.20.1.247:7890'

# proxy_url='192.168.10.20:7890'
self_hub='192.168.63.100:5000'

mkdir -p /etc/systemd/system/docker.service.d
cat > /etc/systemd/system/docker.service.d/http-proxy.conf <<EOF
[Service]
Environment="HTTP_PROXY=http://${proxy_url}"
Environment="HTTPS_PROXY=http://${proxy_url}"
EOF

cat > /etc/docker/daemon.json <<EOF
{
    "log-level":        "error",
    "insecure-registries": ["${self_hub}"]
}
EOF

systemctl enable docker
systemctl daemon-reload
systemctl restart docker


```

# snap 操作 docker
```bash

# 网易
cat > /var/snap/docker/current/config/daemon.json <<"EOF"
{
    "log-level":        "error",
    "storage-driver":   "overlay2",
    "registry-mirrors": ["http://hub-mirror.c.163.com"]
}
EOF


cat > /var/snap/docker/current/config/daemon.json <<"EOF"
{
    "log-level":        "error",
    "storage-driver":   "overlay2"
}
EOF

snap restart docker

```

# tag images and push self
```bash

self_hub='192.168.164.200:5000'

docker images | grep -v 'TAG' | awk '{print $1":"$2}'
kolla/ubuntu-binary-kolla-toolbox:victoria
kolla/ubuntu-binary-mariadb-server:victoria
kolla/ubuntu-binary-mariadb-clustercheck:victoria

#  script

self_hub='192.168.63.100:5000'

function tag_img_and_push(){
    docker tag ${1} ${self_hub}/${1}
    docker push  ${self_hub}/${1}
}

for i in $( docker images | grep -v 'TAG' | awk '{print $1":"$2}' | grep -i 'kolla' | grep -v '192.168'  )
do
   tag_img_and_push ${i} &
done

wait


# 批量 删除 标签
docker images  | grep '192.168' | awk '{print $1":"$2}' | xargs docker rmi

```

# 查看 仓库 内容

http://192.168.63.100:5000/v2/_catalog

