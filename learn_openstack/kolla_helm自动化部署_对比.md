# kolla 从 os 开始部署


# helm 从 kubnute 开始部署


# kolla 自动部署
## 搭建 私有 镜像仓库
http: server gave HTTP response to HTTPS client

官方推荐尝试 安全的 register
https://docs.docker.com/registry/insecure/

Edit the daemon.json file, whose default location is /etc/docker/daemon.json on Linux or C:\ProgramData\docker\config\daemon.json on Windows Server. If you use Docker Desktop for Mac or Docker Desktop for Windows, click the Docker icon, choose Preferences (Mac) or Settings (Windows), and choose Docker Engine.

If the daemon.json file does not exist, create it. Assuming there are no other settings in the file, it should have the following contents:

{
  "insecure-registries" : ["myregistrydomain.com:5000"]
}
Substitute the address of your insecure registry for the one in the example.

With insecure registries enabled, Docker goes through the following steps:

First, try using HTTPS.
If HTTPS is available but the certificate is invalid, ignore the error about the certificate.
If HTTPS is not available, fall back to HTTP.
Restart Docker for the changes to take effect.

```bash
vi /etc/docker/daemon.json
->
{
  "insecure-registries" : ["192.168.19.10:5000"]
}

systemctl restart docker


docker run -d -p 5000:5000 --restart always --name registry registry:2

# 测试 本地镜像 仓库
docker pull nginx
docker tag nginx 192.168.19.10:5000/nginx:new
docker push 192.168.19.10:5000/nginx:new



docker images

docker rmi 192.168.19.10:5000/nginx:new

docker images

docker pull 192.168.19.10:5000/nginx:new

```


