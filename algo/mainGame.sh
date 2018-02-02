#!/bin/bash

par=$2
one=$(($1 / $par))
for i in `seq 1 $par`
do
	screen -AmdS algo$i subGame.sh $((($i-1)*$one+1)) $(($one*$i)) $i
done