#!/bin/bash
count="one two three"

##showing if we irate count varibale it will split value by default space delemeter 

for element in ${count};do
	echo ${element}
done

## using "" in veribale treat count as single veribale 

for element in "${count}";do
	echo "${element}"
done
