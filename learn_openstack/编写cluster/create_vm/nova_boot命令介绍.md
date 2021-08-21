# nova help boot
```bash

usage: nova boot [--flavor <flavor>] [--image <image>]
                 [--image-with <key=value>] [--boot-volume <volume_id>]
                 [--snapshot <snapshot_id>] [--min-count <number>]
                 [--max-count <number>] [--meta <key=value>]
                 [--file <dst-path=src-path>] [--key-name <key-name>]
                 [--user-data <user-data>]
                 [--availability-zone <availability-zone>]
                 [--security-groups <security-groups>]
                 [--block-device-mapping <dev-name=mapping>]
                 [--block-device key1=value1[,key2=value2...]]
                 [--swap <swap_size>]
                 [--ephemeral size=<size>[,format=<format>]]
                 [--hint <key=value>]
                 [--nic <net-id=net-uuid,net-name=network-name,v4-fixed-ip=ip-addr,v6-fixed-ip=ip-addr,port-id=port-uuid>]
                 [--config-drive <value>] [--poll] [--admin-pass <value>]
                 [--access-ip-v4 <value>] [--reservation-id <value>]
                 [--access-ip-v6 <value>] [--description <description>]
                 [--volume_type <value>]
                 [--custom_flavor key1=value1[,key2=value2...]]
                 [--ldap_server <ldap_server>]
                 [--license <kms=kms_server,serial=serial_number>]
                 [--hostname <hostname>] [--pool <boolean>]
                 [--pci-device PCI_DEVICE] [--user_id USER_ID]
                 <name>

Boot a new server.

Positional arguments:
  <name>                        Name for the new server.

Optional arguments:
  --flavor <flavor>             Name or ID of flavor (see 'nova flavor-list').
  --image <image>               Name or ID of image (see 'nova image-list').
  --image-with <key=value>      Image metadata property (see 'nova image-
                                show').
  --boot-volume <volume_id>     Volume ID to boot from.
  --snapshot <snapshot_id>      Snapshot ID to boot from (will create a
                                volume).
  --min-count <number>          Boot at least <number> servers (limited by
                                quota).
  --max-count <number>          Boot up to <number> servers (limited by
                                quota).
  --meta <key=value>            Record arbitrary key/value metadata to
                                /meta_data.json on the metadata server. Can be
                                specified multiple times.
  --file <dst-path=src-path>    Store arbitrary files from <src-path> locally
                                to <dst-path> on the new server. Limited by
                                the injected_files quota value.
  --key-name <key-name>         Key name of keypair that should be created
                                earlier with the command keypair-add.
  --user-data <user-data>       user data file to pass to be exposed by the
                                metadata server.
  --availability-zone <availability-zone>
                                The availability zone for server placement.
  --security-groups <security-groups>
                                Comma separated list of security group names.
  --block-device-mapping <dev-name=mapping>
                                Block device mapping in the format <dev-
                                name>=<id>:<type>:<size(GB)>:<delete-on-
                                terminate>.
  --block-device key1=value1[,key2=value2...]
                                Block device mapping with the keys: id=UUID
                                (image_id, snapshot_id or volume_id only if
                                using source image, snapshot or volume)
                                source=source type (image, snapshot, volume or
                                blank), dest=destination type of the block
                                device (volume or local), bus=device's bus
                                (e.g. uml, lxc, virtio, ...; if omitted,
                                hypervisor driver chooses a suitable default,
                                honoured only if device type is supplied)
                                type=device type (e.g. disk, cdrom, ...;
                                defaults to 'disk') device=name of the device
                                (e.g. vda, xda, ...; if omitted, hypervisor
                                driver chooses suitable device depending on
                                selected bus; note the libvirt driver always
                                uses default device names), size=size of the
                                block device in MB(for swap) and in GB(for
                                other formats) (if omitted, hypervisor driver
                                calculates size), format=device will be
                                formatted (e.g. swap, ntfs, ...; optional),
                                bootindex=integer used for ordering the boot
                                disks (for image backed instances it is equal
                                to 0, for others need to be specified) and
                                shutdown=shutdown behaviour (either preserve
                                or remove, for local destination set to
                                remove).
  --swap <swap_size>            Create and attach a local swap block device of
                                <swap_size> MB.
  --ephemeral size=<size>[,format=<format>]
                                Create and attach a local ephemeral block
                                device of <size> GB and format it to <format>.
  --hint <key=value>            Send arbitrary key/value pairs to the
                                scheduler for custom use.
  --nic <net-id=net-uuid,net-name=network-name,v4-fixed-ip=ip-addr,v6-fixed-ip=ip-addr,port-id=port-uuid>
                                Create a NIC on the server. Specify option
                                multiple times to create multiple NICs. net-
                                id: attach NIC to network with this UUID net-
                                name: attach NIC to network with this name
                                (either port-id or net-id or net-name must be
                                provided), v4-fixed-ip: IPv4 fixed address for
                                NIC (optional), v6-fixed-ip: IPv6 fixed
                                address for NIC (optional), port-id: attach
                                NIC to port with this UUID (either port-id or
                                net-id must be provided).
  --config-drive <value>        Enable config drive.
  --poll                        Report the new server boot progress until it
                                completes.
  --admin-pass <value>          Admin password for the instance.
  --access-ip-v4 <value>        Alternative access IPv4 of the instance.
  --reservation-id <value>      request that a reservation ID be returned
                                instead ofthe newly created instance
                                information.
  --access-ip-v6 <value>        Alternative access IPv6 of the instance.
  --description <description>   Description for the server. (Supported by API
                                versions '2.19' - '2.latest')
  --volume_type <value>         Defined which pool the volume will be created.
  --custom_flavor key1=value1[,key2=value2...]
                                Custom flavor in the format
                                <ram>:<vcpus>:<disk>
  --ldap_server <ldap_server>   Active Directory server address.
  --license <kms=kms_server,serial=serial_number>
                                KMS Server and serial number in windows
                                server.
  --hostname <hostname>         Host name for instance.
  --pool <boolean>              Set to dynamic instance or not.
  --pci-device PCI_DEVICE       PCI device id and count that want attach to
                                instance.Format is
                                vendorid_proeuctid:number.e.g. 10de_13bb:1
  --user_id USER_ID             Boot server for a specific user.

```
