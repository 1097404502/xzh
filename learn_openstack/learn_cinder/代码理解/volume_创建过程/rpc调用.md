# cinder 中采用了 rpc 调用的方式

## 函数定义
/root/cinder/cinder/volume/rpcapi.py:441: def kill_cinder_volume_auto
```bash
def kill_cinder_volume_auto(self, ctxt, host, backend, stor_pool):
    version = self._compat_ver('2.0', '1.28')
    cctxt = self._get_cctxt(host, version)
    cctxt.cast(ctxt, 'kill_cinder_volume_auto',
                backend=backend, stor_pool=stor_pool)
```

## rpc 调用方
/root/cinder/cinder/volume/manager.py:3543

```bash

def kill_cinder_volume_auto(self, ctxt, backend, stor_pool):
    LOG.info("kill cinder-volume-auto begin-------[%s] [%s]"
              % (backend, stor_pool))
    cmd = "ps aux | grep cinder-volume-auto | grep -v grep | grep -w "
    cmd1 = cmd + " "+ backend + "| awk {'print $2'} " \
                                " >/var/log/cinder/auto_pid.txt"
    cmd = cmd + backend + "| awk {'print $2'}| xargs kill -9"
    try:
        subprocess.Popen(cmd1, shell=True)
        subprocess.Popen(cmd, shell=True)
        LOG.info("kill cinder-volume-auto end----")
    except Expection as exc:
            LOG.error(str(exc))

```

