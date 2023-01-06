#!/usr/bin/python3

import re

INPUTFILE="19-input.txt"


replacements=[]
with open(INPUTFILE) as inputfile:
    done_replacements=False
    for line in inputfile:
        line=line.strip()
        if line=='':
            done_replacements=True
            continue
        elif done_replacements:
            molecule=line
            break
        else:
            replacements.append( line.split(" => ") )

print("molecule: ", molecule)
#print("replacements: ", replacements)

# part 1
newmolecules=set()
for to_find,to_replace in replacements:
    for m in re.finditer(to_find, molecule): # gives list of positions where to_find string can be found in molecule
        index=m.start()
        #print(f"Replacing {to_find} with {to_replace} on position {index}")
        newmolecule=molecule[:index] + to_replace + molecule[index+len(to_find):]
        newmolecules.add(newmolecule) # need to add to a set, not just count, to skip duplicates
    
print("Part 1, number of molecules: ", len(newmolecules))

# part 2

num_capitals=sum(1 for char in molecule if char.isupper())
rx1=re.compile( r"Y" )
rx2=re.compile( r"Rn" )
rx3=re.compile( r"Ar" )
num_y =len(rx1.findall(molecule))
num_rn=len(rx2.findall(molecule))
num_ar=len(rx3.findall(molecule))
#print(f" atoms {num_capitals} y {num_y}  rn {num_rn} ar {num_ar}"  )
print("Part 2, min number of transforms: ", num_capitals-num_rn-num_ar-2*num_y-1)