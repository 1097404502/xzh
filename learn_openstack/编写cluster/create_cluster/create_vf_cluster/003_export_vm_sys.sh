
vm_name='zcloud_kk_iso_ex199_5'
qcow_name='zcloud_05_31.qcow2'
pool='nvme'
export_dir='./'

function export_img(){
  volume_id=$( nova show ${vm_name} | grep '/dev/sda' | grep -oE '[a-z0-9-]{20,}' )
  qemu-img convert rbd:${pool}/volume-${volume_id} -c -p -O qcow2 ${export_dir}${qcow_name}
}

export_img

#  --export-format 2
rbd export  nvme/volume-49132db6-136a-4a9d-b55c-27bd439149df -  |  glance image-create --name='test_image_qcow2_instance' --visibility public   --container-format bare --disk-format raw  --os-distro centos  --property image_type=volume   --property os_type=linux


# glance image-create [--architecture <ARCHITECTURE>]
#                            [--protected [True|False]] [--name <NAME>]
#                            [--instance-uuid <INSTANCE_UUID>]
#                            [--min-disk <MIN_DISK>] [--visibility <VISIBILITY>]
#                            [--kernel-id <KERNEL_ID>]
#                            [--tags <TAGS> [<TAGS> ...]]
#                            [--os-version <OS_VERSION>]
#                            [--disk-format <DISK_FORMAT>]
#                            [--os-distro <OS_DISTRO>] [--id <ID>]
#                            [--owner <OWNER>] [--ramdisk-id <RAMDISK_ID>]
#                            [--min-ram <MIN_RAM>]
#                            [--container-format <CONTAINER_FORMAT>]
#                            [--property <key=value>] [--file <FILE>]
#                            [--progress]

glance image-update '60b42d9d-54b3-4b42-b5f5-195c574283ce' --visibility public   

os_distro           | ubuntu                                                                           |
| os_type             | linux

# glance image-create --disk-format qcow2 --is-public True --container-format bare --file cirros-0.3.1-x86_64-disk.img --name cirros


# rbd help export
# usage: rbd export [--pool <pool>] [--namespace <namespace>] [--image <image>]
#                   [--snap <snap>] [--path <path>] [--no-progress]
#                   [--export-format <export-format>]
#                   <source-image-or-snap-spec> <path-name>

#  rbd help export
# usage: rbd export [--pool <pool>] [--namespace <namespace>] [--image <image>]
#                   [--snap <snap>] [--path <path>] [--no-progress]
#                   [--export-format <export-format>[1/2] ]
#                   <source-image-or-snap-spec> <path-name>

# Export image to file.

# Positional arguments
#   <source-image-or-snap-spec>  source image or snapshot specification
#                                (example:
#                                [<pool-name>/[<namespace>/]]<image-name>[@<snap-n
#                                ame>])
#   <path-name>                  export file (or '-' for stdout)

# Optional arguments
#   -p [ --pool ] arg            source pool name
#   --namespace arg              source namespace name
#   --image arg                  source image name
#   --snap arg                   source snapshot name
#   --path arg                   export file (or '-' for stdout)
#   --no-progress                disable progress output
#   --export-format arg          format of image file

rbd list nvme


rbd export nvme/volume-49132db6-136a-4a9d-b55c-27bd439149df -

#   --file <FILE>        Local file that contains disk image to be uploaded.
#  Alternatively, images can be passed to the client via
#  stdin.


 /dev/shm/temp1


rbd export  --export-format qcow2 nvme/volume-49132db6-136a-4a9d-b55c-27bd439149df -  |  glance image-create --name='test_image'  --container-format=bare --disk-format=qcow2 


rbd export nvme/volume-49132db6-136a-4a9d-b55c-27bd439149df - |  glance image-create --name='test image'  --container-format=bare   --disk-format=qcow2 




nvme/7d824977-ee49-4b64-9f0d-27531dbd8b94

