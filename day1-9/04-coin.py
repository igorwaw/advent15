#!/usr/bin/python3

import hashlib


puzzleinput="iwrupvqb"

i=0
foundfirst=False
foundsecond=False
while not (foundfirst and foundsecond):
    nextval=puzzleinput+str(i)
    nexthash=hashlib.md5(nextval.encode()).hexdigest()
    if not foundfirst and nexthash.startswith("00000"):
        print("Found first hash for value ",i)
        foundfirst=True
    if not foundsecond and nexthash.startswith("000000"):
        print("Found second hash for value ",i)
        foundsecond=True
    i+=1

