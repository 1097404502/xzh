#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   load_conf.py
@Time    :   2021/01/27 15:33:40
@Author  :   lmk
@Version :   1.0
@Contact :   lmk@zettakit.com
@Purpose    :   None
'''

# import oslo_config
import sys
import six

from oslo_config import types

from oslo_service import service
from oslo_config import cfg,generator
from oslo_reports import guru_meditation_report as gmr

from oslo_reports import opts as gmr_opts

# if you want --log  unrecognized arguments: --logfile /var/log/cinder/volume.log
from cinder.common import config  # noqa


deprecated_host_opt = cfg.DeprecatedOpt('host')
host_opt = cfg.StrOpt('backend_host', help='Backend override of host value.',
                      deprecated_opts=[deprecated_host_opt])
cfg.CONF.register_cli_opt(host_opt)
CONF = cfg.CONF

deprecated_use_chap_auth_opts = [cfg.DeprecatedOpt('eqlx_use_chap')]
deprecated_chap_username_opts = [cfg.DeprecatedOpt('eqlx_chap_login')]
deprecated_chap_password_opts = [cfg.DeprecatedOpt('eqlx_chap_password')]


#  /usr/bin/cinder-volume --config-file /usr/share/cinder/cinder-dist.conf --config-file /etc/cinder/cinder.conf --logfile /var/log/cinder/volume.log

# get conf file to test
# scp root@192.168.41.1:/usr/share/cinder/cinder-dist.conf  ./
# scp root@192.168.41.1:/etc/cinder/cinder.conf   ./

#  /usr/bin/cinder-volume --config-file ./cinder-dist.conf --config-file ./cinder.conf --logfile /var/log/cinder/volume.log


class Configuration(object):

    def __init__(self, volume_opts, config_group=None):
        """Initialize configuration.

        This takes care of grafting the implementation's config
        values into the config group
        """
        self.config_group = config_group

        # set the local conf so that __call__'s know what to use
        if self.config_group:
            self._ensure_config_values(volume_opts)
            self.local_conf = CONF._get(self.config_group)
        else:
            self.local_conf = CONF

    def _ensure_config_values(self, volume_opts):
        CONF.register_opts(volume_opts, group=self.config_group)

    def append_config_values(self, volume_opts):
        self._ensure_config_values(volume_opts)

    def safe_get(self, value):
        try:
            return self.__getattr__(value)
        except cfg.NoSuchOptError:
            return None

    def __getattr__(self, value):
        # Don't use self.local_conf to avoid reentrant call to __getattr__()
        local_conf = object.__getattribute__(self, 'local_conf')
        return getattr(local_conf, value)


def f():
    # 添加日志项 配置 else can not apply --logfile
    gmr_opts.set_defaults(CONF)
    CONF(sys.argv[1:], project='cinder',
         version=3)
    register_volume()


# 生成文件oslo-config-generator

def gen_conf(o_path):
    CONF.output_file = o_path
    CONF.namespace = "xx"
    # print(CONF._namespace)

    generator.generate(CONF)

def get_pool_conf():
    for i in CONF._namespace._normalized:
        if i.get("pool_args"):
            print(i)
        if i.get("normal"):
            # print(i)
            print(i.get("normal"))
    CONF.output_file = "as"
    print(CONF.output_file)

class DictCONF(six.with_metaclass(service.Singleton, object)):
    def __init__(self):
        self._v = {}
        CONF = cfg.CONF
        for x in CONF._namespace._normalized:
            self.compose(x)
            print(x.get("DEFAULT"))
    
    def compose(self,m):
        for k in m.keys():
            if k in self._v:
                if type(self._v[k]) == dict:
                    self._v[k].update(m[k])
                elif type(self._v[k]) == list:
                    self._v[k] += m[k]
            else:
                self._v[k] = m[k].copy()

    def get(self, full_path):
        return self._v.get(full_path)

def register_volume():
    volume_opts = [
        
        cfg.IntOpt('num_shell_tries',
                default=3,
                help='Number of times to attempt to run flakey shell commands'),
        cfg.IntOpt('reserved_percentage',
                default=0,
                min=0, max=100,
                help='The percentage of backend capacity is reserved'),
        cfg.StrOpt('iscsi_target_prefix',
                default='iqn.2010-10.org.openstack:',
                help='Prefix for iSCSI volumes'),
        cfg.StrOpt('iscsi_ip_address',
                default='$my_ip',
                help='The IP address that the iSCSI daemon is listening on'),
        cfg.ListOpt('iscsi_secondary_ip_addresses',
                    default=[],
                    help='The list of secondary IP addresses of the iSCSI daemon'),
        cfg.PortOpt('iscsi_port',
                    default=3260,
                    help='The port that the iSCSI daemon is listening on'),
        cfg.IntOpt('num_volume_device_scan_tries',
                default=3,
                help='The maximum number of times to rescan targets'
                        ' to find volume'),
        cfg.StrOpt('volume_backend_name',
                help='The backend name for a given driver implementation'),
        cfg.BoolOpt('use_multipath_for_image_xfer',
                    default=False,
                    help='Do we attach/detach volumes in cinder using multipath '
                        'for volume to image and image to volume transfers?'),
        cfg.BoolOpt('enforce_multipath_for_image_xfer',
                    default=False,
                    help='If this is set to True, attachment of volumes for '
                        'image transfer will be aborted when multipathd is not '
                        'running. Otherwise, it will fallback to single path.'),
        cfg.StrOpt('volume_clear',
                default='zero',
                choices=['none', 'zero', 'shred'],
                help='Method used to wipe old volumes'),
        cfg.IntOpt('volume_clear_size',
                default=0,
                help='Size in MiB to wipe at start of old volumes. 0 => all'),
        cfg.StrOpt('volume_clear_ionice',
                help='The flag to pass to ionice to alter the i/o priority '
                        'of the process used to zero a volume after deletion, '
                        'for example "-c3" for idle only priority.'),
        cfg.StrOpt('iscsi_helper',
                default='tgtadm',
                choices=['tgtadm', 'lioadm', 'scstadmin', 'iseradm', 'iscsictl',
                            'ietadm', 'fake'],
                help='iSCSI target user-land tool to use. tgtadm is default, '
                        'use lioadm for LIO iSCSI support, scstadmin for SCST '
                        'target support, iseradm for the ISER protocol, ietadm '
                        'for iSCSI Enterprise Target, iscsictl for Chelsio iSCSI '
                        'Target or fake for testing.'),
        cfg.StrOpt('volumes_dir',
                default='$state_path/volumes',
                help='Volume configuration file storage '
                'directory'),
        cfg.StrOpt('iet_conf',
                default='/etc/iet/ietd.conf',
                help='IET configuration file'),
        cfg.StrOpt('chiscsi_conf',
                default='/etc/chelsio-iscsi/chiscsi.conf',
                help='Chiscsi (CXT) global defaults configuration file'),
        cfg.StrOpt('iscsi_iotype',
                default='fileio',
                choices=['blockio', 'fileio', 'auto'],
                help=('Sets the behavior of the iSCSI target '
                        'to either perform blockio or fileio '
                        'optionally, auto can be set and Cinder '
                        'will autodetect type of backing device')),
        cfg.StrOpt('volume_dd_blocksize',
                default='1M',
                help='The default block size used when copying/clearing '
                        'volumes'),
        cfg.StrOpt('volume_copy_blkio_cgroup_name',
                default='cinder-volume-copy',
                help='The blkio cgroup name to be used to limit bandwidth '
                        'of volume copy'),
        cfg.IntOpt('volume_copy_bps_limit',
                default=0,
                help='The upper limit of bandwidth of volume copy. '
                        '0 => unlimited'),
        cfg.StrOpt('iscsi_write_cache',
                default='on',
                choices=['on', 'off'],
                help='Sets the behavior of the iSCSI target to either '
                        'perform write-back(on) or write-through(off). '
                        'This parameter is valid if iscsi_helper is set '
                        'to tgtadm or iseradm.'),
        cfg.StrOpt('iscsi_target_flags',
                default='',
                help='Sets the target-specific flags for the iSCSI target. '
                        'Only used for tgtadm to specify backing device flags '
                        'using bsoflags option. The specified string is passed '
                        'as is to the underlying tool.'),
        cfg.StrOpt('iscsi_protocol',
                default='iscsi',
                choices=['iscsi', 'iser'],
                help='Determines the iSCSI protocol for new iSCSI volumes, '
                        'created with tgtadm or lioadm target helpers. In '
                        'order to enable RDMA, this parameter should be set '
                        'with the value "iser". The supported iSCSI protocol '
                        'values are "iscsi" and "iser".'),
        cfg.StrOpt('driver_client_cert_key',
                help='The path to the client certificate key for verification, '
                        'if the driver supports it.'),
        cfg.StrOpt('driver_client_cert',
                help='The path to the client certificate for verification, '
                        'if the driver supports it.'),
        cfg.BoolOpt('driver_use_ssl',
                    default=False,
                    help='Tell driver to use SSL for connection to backend '
                        'storage if the driver supports it.'),
        cfg.FloatOpt('max_over_subscription_ratio',
                    default=3.0,
                    help='Float representation of the over subscription ratio '
                        'when thin provisioning is involved. Default ratio is '
                        '3.0, meaning provisioned capacity can be 3 times of '
                        'the total physical capacity. If the ratio is 10.5, it '
                        'means provisioned capacity can be 10.5 times of the '
                        'total physical capacity. A ratio of 1.0 means '
                        'provisioned capacity cannot exceed the total physical '
                        'capacity. The ratio has to be a minimum of 1.0.'),
        cfg.StrOpt('scst_target_iqn_name',
                help='Certain ISCSI targets have predefined target names, '
                        'SCST target driver uses this name.'),
        cfg.StrOpt('scst_target_driver',
                default='iscsi',
                help='SCST target implementation can choose from multiple '
                        'SCST target drivers.'),
        cfg.BoolOpt('use_chap_auth',
                    default=False,
                    help='Option to enable/disable CHAP authentication for '
                        'targets.',
                    deprecated_opts=deprecated_use_chap_auth_opts),
        cfg.StrOpt('chap_username',
                default='',
                help='CHAP user name.',
                deprecated_opts=deprecated_chap_username_opts),
        cfg.StrOpt('chap_password',
                default='',
                help='Password for specified CHAP account name.',
                deprecated_opts=deprecated_chap_password_opts,
                secret=True),
        cfg.StrOpt('driver_data_namespace',
                help='Namespace for driver private data values to be '
                        'saved in.'),
        cfg.StrOpt('filter_function',
                help='String representation for an equation that will be '
                        'used to filter hosts. Only used when the driver '
                        'filter is set to be used by the Cinder scheduler.'),
        cfg.StrOpt('goodness_function',
                help='String representation for an equation that will be '
                        'used to determine the goodness of a host. Only used '
                        'when using the goodness weigher is set to be used by '
                        'the Cinder scheduler.'),
        cfg.BoolOpt('driver_ssl_cert_verify',
                    default=False,
                    help='If set to True the http client will validate the SSL '
                        'certificate of the backend endpoint.'),
        cfg.StrOpt('driver_ssl_cert_path',
                help='Can be used to specify a non default path to a '
                'CA_BUNDLE file or directory with certificates of '
                'trusted CAs, which will be used to validate the backend'),
        cfg.ListOpt('trace_flags',
                    help='List of options that control which trace info '
                        'is written to the DEBUG log level to assist '
                        'developers. Valid values are method and api.'),
        cfg.MultiOpt('replication_device',
                    item_type=types.Dict(),
                    secret=True,
                    help="Multi opt of dictionaries to represent a replication "
                        "target device.  This option may be specified multiple "
                        "times in a single config section to specify multiple "
                        "replication target devices.  Each entry takes the "
                        "standard dict config form: replication_device = "
                        "target_device_id:<required>,"
                        "key1:value1,key2:value2..."),
        cfg.BoolOpt('image_upload_use_cinder_backend',
                    default=False,
                    help='If set to True, upload-to-image in raw format will '
                        'create a cloned volume and register its location to '
                        'the image service, instead of uploading the volume '
                        'content. The cinder backend and locations support '
                        'must be enabled in the image service, and '
                        'glance_api_version must be set to 2.'),
        cfg.BoolOpt('image_upload_use_internal_tenant',
                    default=False,
                    help='If set to True, the image volume created by '
                        'upload-to-image will be placed in the internal tenant. '
                        'Otherwise, the image volume is created in the current '
                        'context\'s tenant.'),
        cfg.BoolOpt('image_volume_cache_enabled',
                    default=False,
                    help='Enable the image volume cache for this backend.'),
        cfg.IntOpt('image_volume_cache_max_size_gb',
                default=0,
                help='Max size of the image volume cache for this backend in '
                        'GB. 0 => unlimited.'),
        cfg.IntOpt('image_volume_cache_max_count',
                default=0,
                help='Max number of entries allowed in the image volume cache. '
                        '0 => unlimited.'),
        cfg.BoolOpt('report_discard_supported',
                    default=False,
                    help='Report to clients of Cinder that the backend supports '
                        'discard (aka. trim/unmap). This will not actually '
                        'change the behavior of the backend or the client '
                        'directly, it will only notify that it can be used.'),
    ]

    # _option_group = 'oslo_reports'
    # conf.register_opts(_options, group=_option_group)
    CONF.register_opts(volume_opts, group = "normal")


# python load_conf.py --config-file ./cinder-dist.conf --config-file ./cinder.conf --config-file my_pool.conf --logfile /var/log/cinder/volume.log
if __name__ == "__main__":
    f()
    # print(CONF.__dict__)
    # print(CONF._namespace)
    # register_volue()
    # print( CONF._groups)
    print( CONF._get("normal").__dict__ )
    # print( CONF._get("max_over_subscription_ratio",group="normal") )
    # print( CONF.list_all_sections() )
    conf_group =  Configuration(volume_opts , config_group="normal") 
    r = conf_group.safe_get("max_over_subscription_ratio")
    print(r)
    # register_volume()
    # object.__getattribute__(self, CONF._get("normal") )
    r = getattr(CONF._get("normal") , "max_over_subscription_ratio")
    print(r)
    print( dir( CONF._get("normal") ) )
    print( CONF._get("normal").keys()  ) 
    r = CONF._get("normal").max_over_subscription_ratio
    print(r)
    r = CONF.max_over_subscription_ratio
    print(r)