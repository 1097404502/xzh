#!/bin/bash
for v in 'api' 'volume' 'backup'  'scheduler'
do
  echo "${v} status:"
  systemctl status openstack-cinder-${v} 2>&1 | grep 'Active:'
done
