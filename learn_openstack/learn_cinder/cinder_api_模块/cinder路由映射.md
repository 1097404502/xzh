# 路由文件位置
/root/cinder/cinder/api/__init__.py

lineno:29
def root_app_factory(loader, global_conf, **local_conf):
    if CONF.enable_v1_api:
        LOG.warning(_LW('The v1 api is deprecated and is not under active '
                        'development. You should set enable_v1_api=false '
                        'and enable_v3_api=true in your cinder.conf file.'))
    return paste.urlmap.urlmap_factory(loader, global_conf, **local_conf)


# learn routes

pip install routes

https://www.cnblogs.com/Zzbj/p/11747525.html

# openstack route module

https://www.cnblogs.com/persevere/p/3611958.html

