# 为 cinder 增加版本适配

老版本采用 10
新版本 采用 14
```bash
/root/codes/cinder/cinder/volume/ceph_api.py
class API
根据 self.ceph_version 进行版本适配


```