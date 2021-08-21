#!/bin/bash

for v in '2' '3'
do
  rsync -a -v -e ssh  --exclude='*.pyc'  /root/script root@192.168.41.${v}:/root/
  rsync -a -v -e ssh  --exclude='*.pyc'  /etc/cinder/rootwrap.d/ root@192.168.41.${v}:/etc/cinder/rootwrap.d/
  rsync -a -v -e ssh  --exclude='*.pyc'  /usr/lib/python2.7/site-packages/cinder  root@192.168.41.${v}:/usr/lib/python2.7/site-packages/
done

