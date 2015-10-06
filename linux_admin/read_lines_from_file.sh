#!/bin/bash

if [ $# != 1 ]; then
    echo "Error: usage $0 filename"
    exit 1
fi

filename=$1

old_ifs=$IFS
IFS=''
for line in $(cat $filename); do
    echo $line
done
IFS=$old_ifs
