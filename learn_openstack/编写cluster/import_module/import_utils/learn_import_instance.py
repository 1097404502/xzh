class C1(object):
    def __init__(self,*args,**kwargs):
        self.x = 0X10

from oslo_utils import importutils

if __name__=='__main__':
    __instance = importutils.import_object("learn_import.C1")
    print( __instance )
    print( __instance.x )
