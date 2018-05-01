#!/bin/bash
result=`ps aux | grep -i "main.py" | grep -v "grep" | wc -l`
if [ $result -ge 1 ]
   then
        echo "script is running"
   else
        echo "start the script"
	dir=`dirname $0`
	nohup python $dir/main.py > ~/output 2>&1 &
fi
