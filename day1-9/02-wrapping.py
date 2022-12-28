#!/usr/bin/python3

INPUTFILE="02-input.txt"

totalpaper=0
totalribbon=0

with open(INPUTFILE) as inputfile:
    for line in inputfile:
        x,y,z=line.rstrip().split('x')
        dimensions=[int(x), int(y), int(z)]
        dimensions.sort()
        #print(dimensions[0], dimensions[1], dimensions[2])
        totalpaper += 3*dimensions[0]*dimensions[1] + 2*dimensions[1]*dimensions[2] + 2*dimensions[2]*dimensions[0]
        totalribbon+= 2*dimensions[0]+2*dimensions[1] + dimensions[0]*dimensions[1]*dimensions[2]

print("Total paper needed:  ",totalpaper)
print("Total ribbon needed: ",totalribbon)