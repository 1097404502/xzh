#!/bin/bash
/root/script/sync_cinder.sh &
wait $!
echo -e 'wait 3s sync code to 2 3 node!\n'
sleep 3
pids=()
i=0
for ip0 in '1' '2' '3'
do
  ssh root@192.168.41.${ip0} 'chmod +x -R /root/script ;/root/script/restart_cinder.sh' &
  pids[${i}]=$!
  let i=i+1
done
for p in ${pids[@]}
do
  echo "wait pid ${p} end"
done

wait
