# 简单介绍 import
相信 小伙伴们 都 使用过
```python

import A

from B import C

```
但是 很多 py源代码 中 经常使用到 __import__, 甚至 在 openstack 中 还有 更加复杂的 自动加载 模块 ， 自动 import 创建实例
```python

from oslo_utils import importutils

importutils.import_object("learn_import.C1")
importutils.import_class("learn_import.C1")

```
基本上 就是 根据字符串 动态的 加载 模块 加载 实例。 

今天 我们 来讲讲 更 复杂 的 自动导入 class 到 指定 命名空间！

# 常规 import 放法 
__import__ 会返回 被引用的 模块对象

```bash

if __name__=='__main__':
    print(globals())
    be_imported =  __import__("be_imported")
    print(globals())
    y1 = be_imported.Y1()
    print(y1)

# output
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__file__': 'use_import.py', '__doc__': None, '__package__': None}

{'be_imported': <module 'be_imported' from '/root/cinder/.tox/local_test/__import__use/be_imported.pyc'>, '__builtins__': <module '__builtin__' (built-in)>, '__file__': 'use_import.py', '__package__': None, '__name__': '__main__', '__doc__': None}

<be_imported.Y1 object at 0x7f27e3f6b650>

```

# 自动注册 class
可以 在 被引用 模块中添加 自动注册 函数 将自身 注册到 整个 globals

在 cinder 中 object 文件夹 下 __init__.py 有 很多 没有返回值的 __improt__ object 对象。
但是 直接 __import__ 在 globals 中 是没有 引用 的 ， 也就是说 我们 访问不到 这些 匿名的 由 __import__ 引入的对象。

那他们是怎么 注册进来的呢 

首先阐述一下 我的观点， 这种 代码 写的 让 读者 很是崩溃，，，，

1. register_all 注册所有 objects

/root/community/cinder/cinder/objects/__init__.py

```bash

def register_all():
    # NOTE(danms): You must make sure your object gets imported in this
    # function in order for it to be registered by services that may
    # need to receive it via RPC.
    __import__('cinder.objects.backup')
    # NOTE(geguileo): Don't include cleanable to prevent circular imports
    __import__('cinder.objects.cleanup_request')
    __import__('cinder.objects.cgsnapshot')

```

匿名的 __import__ 并不能 将函数 注册到  globals 命名空间中去

2. 随便 挑选一个 cinder.objects.xxx 一探究竟
就是 一个 普通的 类 唯一不同 就是 多了 个 rigister 装饰器
```python

@base.CinderObjectRegistry.register
class Cluster(base.CinderPersistentObject, base.CinderObject,
              base.CinderComparableObject):

```
f12 跳转定义进去

3. 查看 cinderPersistentObject
并没有发现 rigister 装饰器 ，必定 在其 父类中 ， f12 进去看看
```python

class CinderObjectRegistry(base.VersionedObjectRegistry):
    def registration_hook(self, cls, index):
        """Hook called when registering a class.

        This method takes care of adding the class to cinder.objects namespace.

        Should registering class have a method called cinder_ovo_cls_init it
        will be called to support class initialization.  This is convenient
        for all persistent classes that need to register their models.
        """
        setattr(objects, cls.obj_name(), cls)

        # If registering class has a callable initialization method, call it.
        if isinstance(getattr(cls, 'cinder_ovo_cls_init', None),
                      abc.Callable):
            cls.cinder_ovo_cls_init()

```

4. 继续 查看  VersionedObjectRegistry

发现 rigister 装饰器 在 这个 父类中 ，但是实际 执行的时候 , 还是 执行了 一个 只有 pass 的 hook
所以 在 实际 调用中 还是 执行的 子类 中的  registration_hook 

那么 就来 回头 详细 阅读一下 子类 registration_hook 的 详细内容 

```python


class VersionedObjectRegistry(object):
    _registry = None

    def __new__(cls, *args, **kwargs):
        if not VersionedObjectRegistry._registry:
            VersionedObjectRegistry._registry = object.__new__(
                VersionedObjectRegistry, *args, **kwargs)
            VersionedObjectRegistry._registry._obj_classes = \
                collections.defaultdict(list)
        self = object.__new__(cls, *args, **kwargs)
        self._obj_classes = VersionedObjectRegistry._registry._obj_classes
        return self

    def registration_hook(self, cls, index):
        pass

    def _register_class(self, cls):
        def _vers_tuple(obj):
            return vutils.convert_version_to_tuple(obj.VERSION)
        # ......
        # Either this is the first time we've seen the object or it's
        # an older version than anything we'e seen.
        self._obj_classes[obj_name].append(cls)
        self.registration_hook(cls, 0)

    @classmethod
    def register(cls, obj_cls):
        registry = cls()
        registry._register_class(obj_cls)
        return obj_cls

```

5. 详细阅读  CinderObjectRegistry.registration_hook

代码 都用看 最重要的 就是 这一句 注释 

This method takes care of adding the class to cinder.objects namespace.

简单 来讲 废了 这么大 周折 就是 为了 把 函数 注册到 cinder.objects 命名空间 去

```python
    def registration_hook(self, cls, index):
        """Hook called when registering a class.

        This method takes care of adding the class to cinder.objects namespace.

        Should registering class have a method called cinder_ovo_cls_init it
        will be called to support class initialization.  This is convenient
        for all persistent classes that need to register their models.
        """
        setattr(objects, cls.obj_name(), cls)

        # If registering class has a callable initialization method, call it.
        if isinstance(getattr(cls, 'cinder_ovo_cls_init', None),
                      abc.Callable):
            cls.cinder_ovo_cls_init()
```

# 结尾

那么 读了 这么多 ， 动态 注册 这些 class 干嘛呢？
再去 回顾以下 register_all() 函数 的 注释

简单讲 就是 rpc 要用， rpc 是什么 远程过程调用， 在 openstack 中 基本 就是指 详细 队列 的 rpc api 中会用到

rpc api 用 这些 东西干嘛呢， 下一篇笔记中 继续读。

```python
def register_all():
    # NOTE(danms): You must make sure your object gets imported in this
    # function in order for it to be registered by services that may
    # need to receive it via RPC.
```

