#!/bin/bash

for i in `seq $1 $2`
do
	python gamestart.py $i
	screen -AmdS server$i python multiserver.py
	screen -ls

	for j in `seq 1 4`
	do
		sleep 0.1
		screen -AmdS client$j-$i python algo_client.py $j
	done

	screen -S server$i -X quit
	for j in `seq 1 4`
	do
		screen -S client$j-$i -X quit
	done

done

screen -S algo$3 -X quit