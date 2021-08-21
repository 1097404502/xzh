
# 注意事项
必须 请求 project scoped 的 token 才可以 继续 请求 其他的 url


```bash


server_ip='192.168.64.1'

 curl -i   -H "Content-Type: application/json"   -d '
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
}'   "http://${server_ip}:35357/v3/auth/tokens"

--->
HTTP/1.1 201 Created
X-Subject-Token: ZgAAAABgyZKjnc8UPAQdEDq4v_PHi1W7Bd8o2mU6L-FbpyOeDe-OMVMR1m724QeXpG-KVD_wyWnkEJUjbtcynfPFmdWYy-9Cw1YDPThnIvzEfZ6M8hx4JUBEwZYKaEcMBI3ExIEL-OOmredX5M6FDd2VecDvySLPx4-sW_fVLVWfgOIQhp3tho0
Vary: X-Auth-Token
Content-Type: application/json
Content-Length: 31026
X-Openstack-Request-Id: req-975dbe7a-493e-4e46-a9cb-28865500ac7e
Date: Wed, 16 Jun 2021 05:56:51 GMT



```


# 修改 adminoprc
```bash

server_ip='192.168.91.1'

cat > /root/admin-openrc <<EOF
export OS_PROJECT_DOMAIN_NAME=default
export OS_USER_DOMAIN_NAME=default
export OS_PROJECT_NAME=project1
export OS_TENANT_NAME=admin
export OS_USERNAME=admin
export OS_PASSWORD=admin_pass
export OS_AUTH_URL=http://${server_ip}:35357/v3
export OS_IDENTITY_API_VERSION=3
export OS_VOLUME_API_VERSION=2
EOF

```

# 测试 环境 建议 延长 token 的 过期时间

```bash

# 替换 一下 参数 延长 授权时间
[token]
expiration = 3600

sed -i 's/^expiration\s*=\s*[0-9]*/expiration = 36000000/g'    /etc/keystone/keystone.conf
systemctl restart openstack-keystone.service

# 得到 长期 授权 token

server_ip='192.168.91.1'

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



# 常用的 一些 请求 项
## cinder
v2 cinder
https://docs.openstack.org/api-ref/block-storage/v2/?expanded=list-api-extensions-detail

```bash
/v2/{project_id}/extensions

server_ip='192.168.99.1'
project_id='cf04385a01004a24a1a0a5e491a35e7c'
os_token='ZgAAAABg0EV7149Exnfl43XmaB-lruUqpaVuhhZKLjuxKDkqtofn6GCW3TiSQ2yEWk8ictMWkoXAaFG8FTqQ7DlSEKgwXlPfFOgrvdnXaRrTiqnQSMLpPyr9rF7KXq6wltP-55b38rgfrTzehVLs2H22NVmIeA0njRquFkDQxQENvVThZbRr5sQ'

base_blk_v2_url="http://${server_ip}:8776/v2/${project_id}"

# 查看 所有 拓展 api
curl -sS -H  "X-Auth-Token: ${os_token}"  ${base_blk_v2_url}/extensions | python -mjson.tool

# 查看 ceph pool
curl -sS -H  "X-Auth-Token: ${os_token}"  ${base_blk_v2_url}/os-ceph-pool


# cluster
# list
curl -sS -H  "X-Auth-Token: ${os_token}"  ${base_blk_v2_url}/os-cluster

# 

```




# 请求头
```bash
X-Auth-Token: ZgAAAABgyZnZCkff-pp3O9MAkZWnWG7QNKt2HccuzJgtQkHqkSBNt0IKy8EQh_kM0y_Foy1YOE4QRU1uRkkdDIItHPbzFjo2-YSUXkPyg_PHKeyHdd4pwCY4nmnoKfSXwi_vpzVwXj3cLjrclE3k9NAvmqPHtmP0btFhzir70nUqXetGgXVfPBo
```