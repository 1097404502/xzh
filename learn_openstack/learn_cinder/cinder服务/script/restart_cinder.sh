#!/bin/bash

for v in 'api' 'volume' 'backup'  'scheduler'
do
  systemctl restart openstack-cinder-${v}
done

echo -e "\n hostname: `hostname`"
for v in 'api' 'volume' 'backup'  'scheduler'
do
  echo "${v} status:"
  systemctl status openstack-cinder-${v} 2>&1 | grep 'Active:'
done
