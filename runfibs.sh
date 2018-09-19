#!/bin/bash

if [ -e fibs.cvs ]; then
    for i in $(seq 10); do
        ./fib.py $i
    done
else 
    exit 1
fi
exit 0
