while true
do
   adb-set-device 1 adb shell dumpsys activity services | grep locationlabs | grep ServiceR
   sleep 1
   echo -------------
done

