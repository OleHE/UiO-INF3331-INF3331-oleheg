#!/bin/bash

case $1 in
	-a)
		echo "$2 $PWD" >> my_bookmarks
		;;
	-r)
		sed -i /$2/d  my_bookmarks
		
		eval unset $2
		;;
	*)
		;;
esac

while read line
do
  vars=( $line )
  eval ${vars[0]}="${vars[1]}"
done < my_bookmarks