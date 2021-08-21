
# 将配置中的 multiattach 修改为 True 即可开启共享挂载
/root/cinder/cinder/volume/drivers/rbd.py (63ffc75)

  expected = dict(volume_backend_name='RBD',
                  vendor_name='Open Source',
                  driver_version=self.driver.VERSION,
                  storage_protocol='ceph',
                  total_capacity_gb='unknown',
                  free_capacity_gb='unknown',
                  reserved_percentage=0,
                  multiattach=False)