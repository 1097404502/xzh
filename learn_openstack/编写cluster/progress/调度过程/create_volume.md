
# 相关 调度参数 

/root/zetta_code/cinder/cinder/scheduler/rpcapi.py : create_volume

request_spec_p

```bash

(Pdb) l
 88             msg_args = {'topic': topic, 'volume_id': volume_id,
 89                         'snapshot_id': snapshot_id, 'image_id': image_id,
 90                         'request_spec': request_spec_p,
 91                         'filter_properties': filter_properties}
 92             import pdb;pdb.set_trace()
 93  ->         if self.client.can_send_version('2.0'):
 94                 version = '2.0'
 95                 msg_args['volume'] = volume
 96             elif self.client.can_send_version('1.9'):
 97                 version = '1.9'
 98                 msg_args['volume'] = volume

 
(Pdb) pp msg_args
{'filter_properties': {},
 'image_id': None,
 'request_spec': {'cgsnapshot_id': None,
                  'consistencygroup_id': None,
                  'flatten': False,
                  'image_id': None,
                  'snapshot_id': None,
                  'source_volid': None,
                  'volume': {'_name_id': None,
                             'attach_status': u'detached',
                             'availability_zone': u'zettakit',
                             'bootable': False,
                             'consistencygroup_id': None,
                             'created_at': '2021-06-29T06:26:55.574532',
                             'cur_backup_id': None,
                             'deleted': False,
                             'deleted_at': None,
                             'display_description': u'',
                             'display_name': u'xx',
                             'ec2_id': None,
                             'encryption_key_id': None,
                             'host': None,
                             'id': '39c37f3b-ca7f-433c-8938-a0b6aae26ea9',
                             'is_sys_vol': False,
                             'launched_at': None,
                             'metadata': {},
                             'migration_status': None,
                             'multiattach': False,
                             'name': 'volume-39c37f3b-ca7f-433c-8938-a0b6aae26ea9',
                             'name_id': '39c37f3b-ca7f-433c-8938-a0b6aae26ea9',
                             'previous_status': None,
                             'project_id': '38fc717716e04ba9bbb0e919a496b9ec',
                             'provider_auth': None,
                             'provider_geometry': None,
                             'provider_id': None,
                             'provider_location': None,
                             'replication_driver_data': None,
                             'replication_extended_status': None,
                             'replication_status': u'disabled',
                             'scheduled_at': None,
                             'share': False,
                             'size': 1,
                             'snapshot_id': None,
                             'source_volid': None,
                             'status': u'creating',
                             'terminated_at': None,
                             'updated_at': None,
                             'user_id': 'dd01e9d83a0546228e0bb159369a4624',
                             'volume_admin_metadata': [],
                             'volume_glance_metadata': [],
                             'volume_metadata': [],
                             'volume_type_id': '5e603621-5fb8-47cc-9a56-f3c94d511573'},
                  'volume_id': '39c37f3b-ca7f-433c-8938-a0b6aae26ea9',
                  'volume_properties': {'attach_status': 'detached',
                                        'availability_zone': 'zettakit',
                                        'cgsnapshot_id': None,
                                        'cluster_id': 'default',
                                        'consistencygroup_id': None,
                                        'display_description': u'',
                                        'display_name': u'xx',
                                        'encryption_key_id': None,
                                        'is_sys_vol': False,
                                        'metadata': {},
                                        'multiattach': False,
                                        'project_id': u'38fc717716e04ba9bbb0e919a496b9ec',
                                        'qos_specs': None,
                                        'replication_status': 'disabled',
                                        'reservations': ['51448cf2-3cdd-4785-b0db-a6b111d9cf44',
                                                         'fb5a2a07-60ec-4346-ad12-825d24684780',
                                                         'b18c831e-1914-4973-9633-6518f1a5b19c',
                                                         '84ccef2f-cf2f-43c9-9347-051622b03ca5'],
                                        'share': False,
                                        'size': 1,
                                        'snapshot_id': None,
                                        'source_volid': None,
                                        'status': 'creating',
                                        'user_id': u'dd01e9d83a0546228e0bb159369a4624',
                                        'volume_type_id': u'5e603621-5fb8-47cc-9a56-f3c94d511573'},
                  'volume_type': {'created_at': '2021-06-29T05:34:53.000000',
                                  'deleted': False,
                                  'deleted_at': None,
                                  'description': u'',
                                  'extra_specs': {u'backend_name': u'b10',
                                                  u'volume_backend_name': u'backend-d18530c8-011e'},
                                  'id': u'5e603621-5fb8-47cc-9a56-f3c94d511573',
                                  'is_public': False,
                                  'name': u'b10',
                                  'qos_specs_id': None,
                                  'updated_at': None}},
 'snapshot_id': None,
 'topic': 'cinder-volume',
 'volume_id': '39c37f3b-ca7f-433c-8938-a0b6aae26ea9'}

```