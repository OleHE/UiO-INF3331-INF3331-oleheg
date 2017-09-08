#!/bin/bash
timezone=$1
case $1 in
  no)
    timezone="UTC-02:00"
    ;;
  sk)
    timezone="UTC-09:00"
    ;;
  us)
    timezone="UTC+04:00"
    ;;
esac

while [ true ]
do
  clear
  echo $(TZ=$timezone date +"%T")
  sleep 1
done
