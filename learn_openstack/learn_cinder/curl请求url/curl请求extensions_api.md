


# curl 请求 拓展 apI
```bash


server_ip='192.168.64.1'
project_id='0e08a03e9389468391bdaf83ed3082c1'
os_token='ZgAAAABgyZnZCkff-pp3O9MAkZWnWG7QNKt2HccuzJgtQkHqkSBNt0IKy8EQh_kM0y_Foy1YOE4QRU1uRkkdDIItHPbzFjo2-YSUXkPyg_PHKeyHdd4pwCY4nmnoKfSXwi_vpzVwXj3cLjrclE3k9NAvmqPHtmP0btFhzir70nUqXetGgXVfPBo'

base_blk_v2_url="http://${server_ip}:8776/v2/${project_id}"

# 查看 所有 拓展 api
curl -sS -H  "X-Auth-Token: ${os_token}"  ${base_blk_v2_url}/extensions | python -mjson.tool

# 查看 所有 拓展 api
curl -sS -H  "X-Auth-Token: ${os_token}"  ${base_blk_v2_url}/os-ceph-pool | python -mjson.tool


```



# 获取token 详细步骤
```bash

# 测试 环境 建议 延长 token 的 过期时间

```bash

# 替换 一下 参数 延长 授权时间
[token]
expiration = 3600

sed -i 's/^expiration\s*=\s*[0-9]*/expiration = 36000000/g'    /etc/keystone/keystone.conf
systemctl restart openstack-keystone.service

# 得到 长期 授权 token

server_ip='192.168.64.1'

curl -sS -i   -H "Content-Type: application/json"   -d '
{ "auth": {
    "identity": {
      "methods": ["password"],
      "password": {
        "user": {
          "name": "admin",
          "domain": { "id": "default" },
          "password": "admin_pass"
        }
      }
    },
    "scope": {
      "project": {
        "name": "project1",
        "domain": { "id": "default" }
      }
    }
  }
}'   "http://${server_ip}:35357/v3/auth/tokens" | grep 'X-Subject-Token:' | awk '{print $2}'

ZgAAAABgyZnZCkff-pp3O9MAkZWnWG7QNKt2HccuzJgtQkHqkSBNt0IKy8EQh_kM0y_Foy1YOE4QRU1uRkkdDIItHPbzFjo2-YSUXkPyg_PHKeyHdd4pwCY4nmnoKfSXwi_vpzVwXj3cLjrclE3k9NAvmqPHtmP0btFhzir70nUqXetGgXVfPBo

```

```