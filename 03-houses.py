#!/usr/bin/python3

INPUTFILE="03-input.txt"

house_x, house_y=0,0
visited=set()
visited.add( (house_x, house_y) )

with open(INPUTFILE) as inputfile:
    while True:
        c=inputfile.read(1)
        if not c:
            break
        if   c=='<': house_x-=1
        elif c=='>': house_x+=1
        elif c=='^': house_y+=1
        elif c=='v': house_y-=1
        else:
            print("Error: unkown direction ",c)
        visited.add( (house_x, house_y) )

print("Visited houses: ",len(visited))
#print(visited)
