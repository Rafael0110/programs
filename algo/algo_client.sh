#!/bin/bash

rm -rf /tmp/uscreens/S-rafambp

screen -AmdS client1 python algo_client.py 1
sleep 1
screen -AmdS client2 python algo_client.py 2
sleep 1
screen -AmdS client3 python algo_client.py 3
sleep 1
screen -AmdS client4 python algo_client.py 4

# NAME='client1'
# NUM=`screen -ls | grep $NAME | sed 's/(Detached)//g' | sed 's/.'$NAME'*//g'`
# screen -p 0 -S $NAME -X python algo_client.py
# screen -r $NUM