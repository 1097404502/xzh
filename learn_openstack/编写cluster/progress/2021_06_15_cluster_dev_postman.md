# 创建 cluster 数据库

```bash

```

# curl 
```bash

curl -s \
 -H "X-Auth-Token: $OS_TOKEN" \
 "http://localhost:5000/v3/projects" | python -mjson.tool

DEBUG:keystoneclient.auth.identity.v3.base:Making authentication request to http://192.168.64.1:35357/v3/auth/tokens

curl  -g -i --insecure -X GET http://10.10.10.10:8774/v2.1/d2df88256a464ef99dc4ab3d26335b52/servers/detail -H "User-Agent: python-novaclient" -H "Accept: application/json" -H "X-Auth-Token: {SHA1}4894992643cc84c63ed03cabba720ada01a59774"

 curl -g -i -X GET http://192.168.64.1:8776/v2/0e08a03e9389468391bdaf83ed3082c1/volumes/detail -H "User-Agent: python-cinderclient" -H "Accept-Language: en_US" -H "Accept: application/json" -H "X-Auth-Token: {SHA1}40e5be3feedaca27a083e5cad45fb1e2f673386f"

  curl -g -i  --insecure -X GET http://192.168.64.1:8776/v2/0e08a03e9389468391bdaf83ed3082c1/volumes/detail -H "User-Agent: python-cinderclient" -H "Accept-Language: en_US" -H "Accept: application/json" -H "X-Auth-Token: ZgAAAABgyVzAonMMj2OqbjdI808Sy2eEsC7MSiAoxgCstnF5_8W1XfIGW334RF1K6q1YTDhP1c0biUd3kAbArnUDJziD2OoialQKRW5zoBCrNlyEv7Dn9CXee6h5BUHK_HgAdPtjuH5b1DDZK8XjwXaUhQzvQiP74Q"

-g, --globoff       Disable URL sequences and ranges using {} and []
-i, --include       Include protocol headers in the output (H/F)
--insecure      Allow connections to SSL sites without certs (H)


```

# 测试 api

## login
```bash
35357
http://192.168.64.1:5000/v3/auth/tokens

post

{
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "name": "admin",
                    "domain": {
                        "name": "Default"
                    },
                    "password": "admin_pass"
                }
            },
            "scope": {
                "project": {
                    "name": "project1",
                    "domain": { "id": "default" }
                }
            }
        }
    }
}

# 返回的 token
token :
ZgAAAABgyF-tZkno61XAn6kAoru4W76xdFcBDHeLOKw6ViGPqUfhHuYClfcfVYzg1okTKhFa886yYnXkWPkSaxxSbtrSShFuIkowZbK-NDPzBY7uSUiEqQ0B2mw9PRpqjKkGI1h6O_860ha2EbnO-RyWIiWX4Nh58w
```

## projects
```bash
http://192.168.64.1:5000/v3/auth/projects

get

X-Auth-Token	是	header	string	认证令牌	

{
    "count": null,
    "links": {
        "self": "http://192.168.64.1:5000/v3%0A/v3/auth/projects",
        "previous": null,
        "next": null
    },
    "projects": [
        {
            "is_domain": false,
            "description": "Project No.1",
            "links": {
                "self": "http://192.168.64.1:5000/v3%0A/v3/projects/0e08a03e9389468391bdaf83ed3082c1"
            },
            "enabled": true,
            "id": "0e08a03e9389468391bdaf83ed3082c1",
            "parent_id": "default",
            "domain_id": "default",
            "name": "project1"
        }
    ]
}

```

## pools
```bash
http://192.168.64.1:8776/v2/{project_id}/os-ceph-pool

http://192.168.64.1:8776/v2/0e08a03e9389468391bdaf83ed3082c1/os-ceph-pool

get

请求参数

X-Auth-Token:ZgAAAABgyGTkp4e60wCdlrdRPaUj_r9lyVh4vhj5NfIaKISdtEEQPzVrR6EGp1Cr3nXRl0nVVfJif5tUhpIqybj5LejQGbGgfFSM3c3d_AK7-khGQ-aNfi7bs45BbnjxjgbgSKH-30teCTN0BB5MlY-G_FxRIPTJdA

X-Auth-Token	是	header	string	认证令牌	
project_id	是	url	string	项目ID	
请求参数示例

GET /v2/60cfef536bec4d5e933313608680f384/os-ceph-pool


```

## volumes
```bash

GET /v2/{project_id}/volumes

http://192.168.64.1:8776/v2/0e08a03e9389468391bdaf83ed3082c1/volumes


```