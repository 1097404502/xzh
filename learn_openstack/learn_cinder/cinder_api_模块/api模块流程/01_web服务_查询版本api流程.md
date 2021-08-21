
# 整个 web 服务入口

cmd 启动 cinder-volume-api 的 时候
/root/cinder/cinder/cmd/api.py
```bash
def main():
  .....
  server = service.WSGIService('osapi_volume')
  .....
```

## 创建 WsgiServer 的代码 片段

默认 conf 中存在 osapi_volume_listen, osapi_volume_listen_port
```bash
# IP address on which OpenStack Volume API listens (string value)
#osapi_volume_listen = 0.0.0.0

# Port on which OpenStack Volume API listens (port value)
# Minimum value: 0
# Maximum value: 65535
#osapi_volume_listen_port = 8776
```

```bash
class WSGIService(service.ServiceBase):
    """Provides ability to launch API from a 'paste' configuration."""

    def __init__(self, name, loader=None):
        """Initialize, but do not start the WSGI server.

        :param name: The name of the WSGI server given to the loader.
        :param loader: Loads the WSGI application using the given name.
        :returns: None

        """
        self.name = name
        self.manager = self._get_manager()
        self.loader = loader or wsgi.Loader(CONF)
        self.app = self.loader.load_app(name)
        self.host = getattr(CONF, '%s_listen' % name, "0.0.0.0")
        self.port = getattr(CONF, '%s_listen_port' % name, 0)
        self.workers = (getattr(CONF, '%s_workers' % name, None) or
                        processutils.get_worker_count())
        if self.workers and self.workers < 1:
            worker_name = '%s_workers' % name
            msg = (_("%(worker_name)s value of %(workers)d is invalid, "
                     "must be greater than 0.") %
                   {'worker_name': worker_name,
                    'workers': self.workers})
            raise exception.InvalidInput(msg)
        setup_profiler(name, self.host)

        self.server = wsgi.Server(CONF,
                                  name,
                                  self.app,
                                  host=self.host,
                                  port=self.port)
```


## paste 配置文件
./cinder/etc/cinder/api-paste.ini
按照 paste 书写了 composite, filter, app, pipeline 
```bash

[composite:osapi_volume]
use = call:cinder.api:root_app_factory
/: apiversions

```

1. 位于 cinder/api.py 中的 root_app_factory 方法
```bash

def root_app_factory(loader, global_conf, **local_conf):
    if CONF.enable_v1_api:
        LOG.warning(_LW('The v1 api is deprecated and is not under active '
                        'development. You should set enable_v1_api=false '
                        'and enable_v3_api=true in your cinder.conf file.'))
    return paste.urlmap.urlmap_factory(loader, global_conf, **local_conf)

```

2. 再继续 查找 apiversion
```bash

[pipeline:apiversions]
pipeline = cors http_proxy_to_wsgi faultwrap osvolumeversionapp

```

3. 再继续查找 osvolumeversionapp
```bash

[app:osvolumeversionapp]
paste.app_factory = cinder.api.versions:Versions.factory

```

4. 再继续 查找  cinder.api.versions:Versions.factory

其中 mapper 的 action 参数 负责调用 resource( 一个 controller 类 ) 中 同名的 方法

```bash

class Versions(openstack.APIRouter):
    """Route versions requests."""

    ExtensionManager = extensions.ExtensionManager

    def _setup_routes(self, mapper, ext_mgr):
        self.resources['versions'] = create_resource()
        mapper.connect('versions', '/',
                       controller=self.resources['versions'],
                       action='all')
        mapper.redirect('', '/')

```

5.  但是 Versions 类中 没有 factory 方法，那么 继续 去查找 他的 父类

```bash

class APIRouter(base_wsgi.Router):
    """Routes requests on the API to the appropriate controller and method."""
    ExtensionManager = None  # override in subclasses

    @classmethod
    def factory(cls, global_config, **local_config):
        """Simple paste factory, :class:`cinder.wsgi.Router` doesn't have."""
        return cls()

    省略 一些代码 .....
```

6. 找到了 工厂factory 方法，我们 就继续 回到 工厂 返回的 Versions 类

action='all' 绑定到了 create_resource() 返回的 controller 类
```bash

def create_resource():
    return wsgi.Resource(VersionsController())

```

再去查看 VersionController 类的定义
./cinder/cinder/api/versions.py
```bash

class VersionsController(wsgi.Controller):

    def __init__(self):
        super(VersionsController, self).__init__(None)
    
    省略一些代码...
    @wsgi.response(300)
    def all(self, req):
        """Return all known versions."""
        builder = views_versions.get_view_builder(req)
        known_versions = copy.deepcopy(_KNOWN_VERSIONS)
        return builder.build_versions(known_versions)

```
所以 在浏览器 输入 
http://volume_api_ip:8776/  
就会 被 转到 versionapp 的 all 方法, 最后 实际调用就是 

builder.build_versions(known_versions) 返回一个 可以被 json 的字典。

view 视图文件
./cinder/cinder/api/views/versions.py
```bash
class ViewBuilder(object):
    def __init__(self, base_url):
        """Initialize ViewBuilder.

        :param base_url: url of the root wsgi application
        """
        self.base_url = base_url

    def build_versions(self, versions):
        views = [self._build_version(versions[key])
                 for key in sorted(list(versions.keys()))]
        return dict(versions=views)
```


