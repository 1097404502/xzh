net_id=191


. ~/admin-openrc
neutron net-create  --shared --provider:network_type vlan  --provider:physical_network default  --provider:segmentation_id   ${net_id}  ex${net_id} 
neutron subnet-create --name ex${net_id}sub1 --ip-version 4 --gateway 192.168.${net_id}.254  ex${net_id} 192.168.${net_id}.0/24



flavor_name='zcloud_flavor'
id='100'
ram="$[24*1024]"
disk='100'
vcpus='24'

nova flavor-create  --is-public 1  ${flavor_name} ${id}  ${ram}  ${disk} ${vcpus}


# usage: nova flavor-create [--ephemeral <ephemeral>] [--swap <swap>]
                          # [--rxtx-factor <factor>] [--is-public <is-public>]
                          # <name> <id> <ram> <disk> <vcpus>

