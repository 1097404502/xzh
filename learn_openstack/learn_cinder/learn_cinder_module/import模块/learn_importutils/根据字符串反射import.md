# 引入 类 import_class

```python

class C1(object):
    def __init__(self,*args,**kwargs):
        self.x = 0X10

from oslo_utils import importutils

if __name__=='__main__':
    __class_name = importutils.import_class("learn_import.C1")
    print( __class_name )
    print( __class_name() )


-->
<class 'learn_import.C1'>
<learn_import.C1 object at 0x7f2aedfdee90>


```

# 直接引入实例

```python

class C1(object):
    def __init__(self,*args,**kwargs):
        self.x = 0X10

from oslo_utils import importutils

if __name__=='__main__':
    __instance = importutils.import_object("learn_import.C1")
    print( __instance )
    print( __instance.x )

-->
<learn_import.C1 object at 0x7f4149d89e90>
16


```

