[glusterfs]                                                          #最后添加  
volume_driver = cinder.volume.drivers.glusterfs.GlusterfsDriver      #驱动    
glusterfs_shares_config = /etc/cinder/shares.conf                    #glusterfs存储  
glusterfs_mount_point_base = /var/lib/cinder/volumes                 #挂载点  



[local_fs]                                                         
volume_driver = cinder.volume.drivers.local_fs.GlusterfsDriver