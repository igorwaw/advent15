#!/usr/bin/python3

import re

INPUTFILE="16-input.txt"


aunt_sender= {
"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1
}



# read file into list
aunts=[]
rx=re.compile( r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)" )
with open(INPUTFILE) as inputfile:
    for line in inputfile:
        number, item1, item1value, item2, item2value, item3, item3value  = rx.match(line).groups()
        aunts.append( ( (item1, int(item1value)), (item2, int(item2value)), (item3, int(item3value) )) )

# part 1
for i,aunt in enumerate(aunts):
    itemsmatched=0

    for item in aunt:
        if item[1] == aunt_sender[item[0]]:
            itemsmatched+=1
        else:
            break # no need to check other items
    if itemsmatched==3:
        print(f"Part 1: aunt {i+1} matches") 
        break


# part 2
for i,aunt in enumerate(aunts):
    itemsmatched=0

    for item in aunt:
        if item[0] in ["cats", "trees"]:
            if item[1] > aunt_sender[item[0]]:    
                itemsmatched+=1
        elif item[0] in ["pomeranians", "goldfish"]:
            if item[1] < aunt_sender[item[0]]:    
                itemsmatched+=1
        elif item[1] == aunt_sender[item[0]]:
            itemsmatched+=1
    if itemsmatched==3:
        print(f"Part 2: aunt {i+1} matches") 
        break

