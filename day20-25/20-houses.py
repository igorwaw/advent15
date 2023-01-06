#!/usr/bin/python3

from tqdm import tqdm

TARGETNUMBER=33100000
LIMIT=TARGETNUMBER//10

houses = [ 0 for x in range(LIMIT) ]
houses2 = [ 0 for x in range(LIMIT) ]


for elfnumber in tqdm(range(1, LIMIT)):
    numvisit=0
    for housenumber in range(elfnumber, LIMIT, elfnumber):
        houses[housenumber]+=10*elfnumber
        if numvisit<50:
            numvisit+=1
            houses2[housenumber]+=11*elfnumber
    


# find the smallest house number with the specified number of presents:
for i in range(2, LIMIT):
    if houses[i]>=TARGETNUMBER:
        part1result=i
        break
for i in range(2, LIMIT):
    if houses2[i]>=TARGETNUMBER:
        part2result=i
        break


print(f"Part 1: house number {part1result} got {houses[part1result]} presents")
print(f"Part 2: house number {part2result} got {houses[part2result]} presents")
