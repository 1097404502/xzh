# pdb 调试
```bash

systemctl stop openstack-cinder-volume

su -s /bin/bash -c ' /usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/volume.log'  cinder


su -s /bin/bash -c "/usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/normal_backend-normal/cinder.conf --logfile /etc/cinder/normal_backend-normal/backend.log --backend backend-normal --stor_pool volumes --run_subproc" cinder

/etc/cinder/test2_backend-7251256d-dab3/


su -s /bin/bash -c "/usr/bin/python2 /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/test2_backend-7251256d-dab3/cinder.conf --logfile /etc/cinder/test2_backend-7251256d-dab3/backend.log --run_subproc" cinder

```

 p type(CONF)
<class 'oslo_config.cfg.ConfigOpts'>

CONF(sys.argv[1:], project='cinder',version=version.version_string())




