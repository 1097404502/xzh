# 变更日志
[root@localhost cinder]# git log --pretty=oneline ./cinder/volume/drivers/rbd.py
af96a4f85335322d0f3a90691f5b1ed5c3e4bdc8 RBD: Don't query Ceph on stats for exclusive pools
6d30da900158f80a10a7325501b06adf8485a62b RBD: Handle ImageNotFound exception in _get_usage_info correctly
f466a87faa39432c61d531687d40088fa99e7f8e RBD: get provisioned capacity using same connection
90907100b5e6255678c2bc2e3d51d7d2996ff4f1 RBD: Fix stats reporting
4d7c4b37efe786ae818fece71bbdf266ea85693d Add ability for ceph driver to report discard
2be5e613a2a18cf91b1a35c5b87a176f35286fcf RBD Thin Provisioning stats
d6f0ff39ffea85afd5f2c8adbff2ec636177f29d Merge "Separate snapshot size fields"
706e649b6620eb5d6a6cdf3bdebf1ee4d401300b Separate snapshot size fields
0c30eaf3e1174240a678159517fffffbea4b42a1 Fix bug ZCLOUD-1111
cc0201b6abc12cf46983fd144b7e03a83ebca56a snapshots tree
009572950a8d7cbcf5597bc898c097c2319ae48b Create a volume based on snapshots to set whether to persist or not
95e7b73ef76f7332f61e0b6ce46398c2b4e9db0c Add audit notifications.
d08ca6fd7cb9d3d44c013e25acbc341cd3707e49 Collate the error information of API interface
6b825ab7ff4725cb001097c3630385613d5f5203 (tag: 2.2.0-20171120) Safe decode pool_name when uploading image
cea76ae902c621fa3cffbd703597a351b0507cfb Correct unicode rbd pool
a79ca5e60ca814e35245955297d5553c822d7aef Support chinese for storage backend and pool name
19df6d1b5377554200ceca4f34867242f04271bd Improve reset data of volume
23204446dbfa4baac43988babc6a79a448bf10a7 rbd: disable fast-diff feature when volume is shared
85ad8ed7588103e286033a787d3d5ba9be01b4af Merge branch '2.1.0'
f74a0c17d7ab77435f50a8ea871b4d8a0ae6a5eb Fix AttributeError when obtaining 'name' attribute from 'snap'
74b84a20a65e0dc7f87c79bc9c47ec2dadde6c75 Merge branch '2.1.0'
6e2f8f944676e2a648717a00941ba65fddd3b9b6 (tag: 2.1.0-20170412) Pass location in upload api
20970de7c699dfcdd83349aa7fd3c3fe984e33b3 rbd: Create multi-attached volume with --image-shared
62a7a4990287bc14ac8d8a01d75b58bc299955ca Improve incremental backup for ceph
d3c756e4b6b5f07af4ac1f5b6966c6372ee1f8ae Create volume backends dynamically
92d0b4d9ca9f4167f5701d2b681f9e5fdab784f5 snapshot support rollback
63ffc759a66e278f49c3349197f83ba782f187c1 Declare multiattach is True in RBD driver
e1a59b18e6c0cc673470ac0b6e509e1b6f3f6dc7 rebase http://github.com/openstack/cinder, branch stable/mitaka, commit id 7ac220