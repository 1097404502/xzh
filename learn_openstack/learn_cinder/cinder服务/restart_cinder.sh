#!/bin/bash

for v in 'api' 'valume' 'backup'  'scheduler'
do
systemctl restart openstack-cinder-${v}
done

for v in 'api' 'valume' 'backup'  'scheduler'
do
  echo "${v} status:"
  systemctl status openstack-cinder-${v} 2>&1 | grep 'Active:'
done
