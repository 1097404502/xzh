[DEFAULT]
osapi_volume_listen = 192.168.40.10
osapi_volume_workers = 4
backup_ceph_conf = /etc/ceph/ceph.conf
backup_ceph_user = backup
backup_ceph_chunk_size = 1048576
backup_ceph_pool = backups
backup_ceph_stripe_unit = 0
backup_ceph_stripe_count = 0
get_rados_info_user = openstack
my_ip = 192.168.40.10
glance_host = 192.168.40.10
glance_api_version = 2
default_volume_type = normal
auth_strategy = keystone
enabled_backends = normal
no_snapshot_gb_quota = true
volume_clear = none
volume_driver = cinder.volume.drivers.rbd.RBDDriver
nova_catalog_info = compute:Compute Service:publicURL
nova_catalog_admin_info = compute:Compute Service:adminURL
nova_endpoint_template = http://192.168.40.10:8774/v2/%(project_id)s
nova_endpoint_admin_template = http://192.168.40.10:8774/v2/%(project_id)s
os_region_name = RegionOne
debug = false
verbose = true
log_dir = /var/log/cinder
use_stderr = false
storage_availability_zone = zettakit
rpc_response_timeout = 60
enable_v1_api = false
control_exchange = cinder
notification_driver = messagingv2
enable_force_upload = true
quota_snapshots = -1
quota_backups = -1
quota_backup_gigabytes = -1
volume_service_inithost_offload = true

[database]
connection = mysql+pymysql://cinder:cinder_dbpass@192.168.40.10/cinder
max_retries = -1
retry_interval = 1
use_db_reconnect = true
db_max_retry_interval = 1
db_max_retries = -1

[keystone_authtoken]
auth_uri = http://192.168.40.10:5000
auth_url = http://192.168.40.10:35357
auth_version = v3
region_name = RegionOne
auth_type = password
project_domain_name = default
user_domain_name = default
project_name = service
username = cinder
password = cinder

[oslo_messaging_rabbit]
rabbit_host = 192.168.40.10
rabbit_port = 5672
rabbit_userid = openstack
rabbit_password = openstack

[normal]
volume_driver = cinder.volume.drivers.rbd.RBDDriver
rbd_pool = volumes
volume_backend_name = normal
rbd_user = openstack
rbd_ceph_conf = /etc/ceph/ceph.conf
rbd_secret_uuid = 7e0fb456-26bd-4b14-b039-2b986fdcbcc4
rbd_max_clone_depth = 5
rbd_store_chunk_size = 4
rados_connection_retries = 3
rados_connection_interval = 5
rados_connect_timeout = 5
rbd_flatten_volume_from_snapshot = false
rbd_cluster_name = ceph

[oslo_concurrency]
lock_path = $state_path/tmp

[resource]
project_domain_name = default
user_domain_name = default
project_name = service
username = cinder
password = cinder
auth_uri = http://192.168.40.10:5000/v3
