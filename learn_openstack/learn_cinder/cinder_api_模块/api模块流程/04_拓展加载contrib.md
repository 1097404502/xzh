# 拓展加载
除了 cinder/api/v1 v2 v3 中 根据 routes , controller 定义的 一些 函数以外
在 cinder/api/contrib 中也定义了 很多 操作 view 函数

下边来 探究以下 他们 加载的 过程
rep "api.contrib" -r ~/cinder/cinder/

/root/cinder/cinder/common/config.py:                     'volume_extension option with cinder.api.contrib.'
/root/cinder/cinder/common/config.py:                    default=['cinder.api.contrib.standard_extensions'],

```bash

cfg.MultiStrOpt('osapi_volume_extension',
                default=['cinder.api.contrib.standard_extensions'],
                help='osapi volume extension to load'),

```

grep "standard_extensions" -r ./

/root/cinder/cinder/api/contrib/__init__.py
```bash

def standard_extensions(ext_mgr):
    extensions.load_standard_extensions(ext_mgr, LOG, __path__, __package__)

```

