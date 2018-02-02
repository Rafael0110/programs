#!/bin/bash

rm log.txt
for i in `seq 1 $1`
do
	echo $i
	screen -AmdS server$i python multiserver.py $i
	for j in `seq 1 4`
	do
		sleep 0.1
		screen -AmdS client$j-$i python algo_client.py $j
	done
	sleep 1

	screen -S server$i -X quit >& /dev/null
	for j in `seq 1 4`
	do
		sleep 0.1
		screen -S client$j-$i -X quit >& /dev/null
	done

done

./allKill.sh