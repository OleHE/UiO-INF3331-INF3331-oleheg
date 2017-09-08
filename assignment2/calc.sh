#!/bin/bash

case $1 in
  S)
    shift
    declare -i sum=0
    for var in $@
    do
      (( sum += var ))
    done
    echo $sum
    ;;
  P)
    shift
    declare -i product=1
    for var in $@
    do
      (( product *= var ))
    done
    echo $product
    ;;
  M)
    shift
    declare -i max=$1
    for var in $@
    do
      if (( max < var ))
      then
        (( max = var ))
      fi
    done
    echo $max
    ;;
  m)
    shift
    declare -i min=$1
    for var in $@
    do
      if (( min > var ))
      then
        (( min = var ))
      fi
    done
    echo $min
    ;;
  *)
    echo "$0: invalid option \"$1\""; exit ;;
esac
