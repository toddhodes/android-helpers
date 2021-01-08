#!/bin/bash


case "$1" in
"on")
  adb shell settings put global window_animation_scale 1.0
  adb shell settings put global transition_animation_scale 1.0
  adb shell settings put global animator_duration_scale 1.0
;;
"off")
  adb shell settings put global window_animation_scale 0
  adb shell settings put global transition_animation_scale 0
  adb shell settings put global animator_duration_scale 0
;;
"show")
  adb shell settings get global window_animation_scale
  adb shell settings get global transition_animation_scale
  adb shell settings get global animator_duration_scale
;;
*) echo "Usage: $0 on|off|show"
;;
esac
