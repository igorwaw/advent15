#!/bin/sh




case "$1" in
	25)
	    gcc -O2 -Wall -o 25-snow 25-snow.c
	    ;;
	*) # surely I mean the newest one
	    gcc -O2 -Wall -o 25-snow 25-snow.c
	    ;;
esac
