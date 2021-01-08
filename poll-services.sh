#!/bin/bash
#
# poll the device for our runing services
#

while true
do
  adb shell dumpsys activity services \
     | grep locationlabs | grep -A1 ServiceR
  sleep 1
  echo -------------
done


