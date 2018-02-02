#!/bin/bash

rm log.txt
for i in `seq 1 $1`
do
	echo $i
	screen -AmdS server  python multiserver.py $i
	sleep 0.1
	screen -AmdS client1 python algo_client.py 1
	sleep 0.1
	screen -AmdS client2 python algo_client.py 2
	sleep 0.1
	screen -AmdS client3 python algo_client.py 3
	sleep 0.1
	screen -AmdS client4 python algo_client.py 4
	sleep 1

	./kill.sh multiserver.py
	screen -S server -X quit >& /dev/null
	screen -wipe >& /dev/null
	for j in `seq 1 4`
	do
		sleep 0.1
		screen -S client$j -X quit >& /dev/null
	done
done

cat log.txt | grep -c win
cat log.txt | grep -c gamestart