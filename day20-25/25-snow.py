#!/usr/bin/python3

TARGETROW=2981
TARGETCOL=3075

FIRSTCODE=20151125
MULTIPLIER=252533
DIVIDER=33554393

row=col=1
newcode=FIRSTCODE
while True:
    if (row>1):
        row-=1
        col+=1
    else:
        row=col+1
        col=1

    newcode=(newcode*MULTIPLIER)%DIVIDER
    if row==TARGETROW and col==TARGETCOL:
        break

print(f"Part 1: code {newcode}")
