# api_paste.ini 文件中的 composite
```bash
[composite:osapi_volume]
use = call:cinder.api:root_app_factory
/: apiversions
/v1: openstack_volume_api_v1
/v2: openstack_volume_api_v2
/v3: openstack_volume_api_v3

[composite:openstack_volume_api_v1]
use = call:cinder.api.middleware.auth:pipeline_factory
noauth = cors http_proxy_to_wsgi request_id faultwrap sizelimit osprofiler noauth apiv1
keystone = cors http_proxy_to_wsgi request_id faultwrap sizelimit osprofiler authtoken keystonecontext apiv1
keystone_nolimit = cors http_proxy_to_wsgi request_id faultwrap sizelimit osprofiler authtoken keystonecontext apiv1

[composite:openstack_volume_api_v2]
use = call:cinder.api.middleware.auth:pipeline_factory
noauth = cors http_proxy_to_wsgi request_id faultwrap sizelimit osprofiler noauth apiv2
keystone = cors http_proxy_to_wsgi request_id faultwrap sizelimit osprofiler authtoken keystonecontext apiv2
keystone_nolimit = cors http_proxy_to_wsgi request_id faultwrap sizelimit osprofiler authtoken keystonecontext apiv2

.....
```
第一个 [composite:osapi_volume] 内容很好理解
use = call:... 
调用 相应文件中的 root_app_factory 方法
不同的 /  /v1  /v2  /v3 定向到 自己的 pipline 或者 composite

[pipeline:apiversions]
pipeline = cors http_proxy_to_wsgi faultwrap osvolumeversionapp

pipline 内容也很容易理解， 就是 去 调用 osvolumeversionapp

但是  [composite:openstack_volume_api_v1] 中的内容令人有些 费解
借用官方的描述 Composites are just slightly more complex

# 分析 use = call:cinder.api.middleware.auth:pipeline_factory

```bash

def pipeline_factory(loader, global_conf, **local_conf):
    """A paste pipeline replica that keys off of auth_strategy."""
    pipeline = local_conf[CONF.auth_strategy]
    if not CONF.api_rate_limit:
        limit_name = CONF.auth_strategy + '_nolimit'
        pipeline = local_conf.get(limit_name, pipeline)
    pipeline = pipeline.split()
    filters = [loader.get_filter(n) for n in pipeline[:-1]]
    app = loader.get_app(pipeline[-1])
    filters.reverse()
    for filter in filters:
        app = filter(app)
    return app

```
CONF.auth_strategy 授权策略 在 
/root/cinder/scripts/cinder-dist.conf
auth_strategy = keystone

noauth = cors http_proxy_to_wsgi request_id faultwrap sizelimit osprofiler noauth apiv2
keystone = cors http_proxy_to_wsgi request_id faultwrap sizelimit osprofiler authtoken keystonecontext apiv2
keystone_nolimit = cors http_proxy_to_wsgi request_id faultwrap sizelimit osprofiler authtoken keystonecontext apiv2

所以选中 第二个 pipeline

local_conf 就代表 对应的 composite section 部分 的 定义

pipeline = local_conf[CONF.auth_strategy]
得到 一长串的 filiter + 末尾的 app
将 他们 且分开来， 并将 filters 逆序， 一层层 包裹在 app 的外层，从而形成了 整个 完整的 app

# 最终的 app 
[app:apiv2]
paste.app_factory = cinder.api.v2.router:APIRouter.factory

