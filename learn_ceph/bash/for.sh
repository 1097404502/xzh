for i in `seq 1 10`
do
echo $i
done


for i in `seq 1 10` ;do echo $i ;done;

for i in `seq 1 10` ;do echo $i  ; echo $[$i+1] ;done;
