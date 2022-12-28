#!/bin/sh




case "$1" in
    1)
	    gcc -O2 -Wall -o 01-notlisp 01-notlisp.c
	    ;;
	8)
	    gcc -O2 -Wall -o 08-matchsticks 08-matchsticks.c
	    ;;
	*) # surely I mean the newest one
	    gcc -O2 -Wall -o 08-matchsticks 08-matchsticks.c
	    ;;
esac
