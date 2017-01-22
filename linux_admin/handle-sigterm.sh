#!/bin/bash

trap 'kill -TERM $PID' TERM INT
#$JAVA_EXECUTABLE $JAVA_ARGS &
sleep 1000 &
PID=$!
echo "PID: $PID"
wait $PID
trap - TERM INT
wait $PID
EXIT_STATUS=$?
echo "DONE"
