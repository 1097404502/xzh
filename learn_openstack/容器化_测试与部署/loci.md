# 简介
The instructions below can be used for any OpenStack service currently targeted by LOCI. 
For simplicity, we will continue to use Keystone as an example.

# build keystone locally

为了 构建的 快速性， 推荐在 世界的 服务器上 build
本人采用 香港的 云服务器 进行的 构建

ssh root@47.242.75.166 -p 10022



## 可选项 基于 代理的 构建
If building behind a proxy, remember to use build arguments to pass these through to the build:

```bash

docker build https://opendev.org/openstack/loci.git \
    --build-arg http_proxy=$http_proxy \
    --build-arg https_proxy=$https_proxy \
    --build-arg no_proxy=$no_proxy \
    --build-arg PROJECT=keystone \
    --tag keystone:ubuntu

```

```bash

# 构建基本镜像
docker build https://opendev.org/openstack/loci.git#master:dockerfiles/ubuntu_bionic \
    --tag loci-base:ubuntu

# 在基本镜像的 基础上构建 keystone 镜像
docker build https://opendev.org/openstack/loci.git \
    --build-arg FROM=loci-base:ubuntu \
    --build-arg PROJECT=keystone \
    --tag loci-keystone:ubuntu

```


