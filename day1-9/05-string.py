#!/usr/bin/python3

from collections import Counter
import re

INPUTFILE="05-input.txt"


NAUGHTYPAIRS=("ab", "cd", "pq", "xy")
VOWELS=("a", "e", "i", "o", "u")
rx1=re.compile(r"(\w)\1")
rx2=re.compile(r'(\w)\w\1')
rx3=re.compile(r'(\w\w)\w*\1')

def is_nice_1(chstring: str) -> bool:
    for pair in NAUGHTYPAIRS:
        # condition: doesn't contain naughty pair
        if pair in chstring: 
            #print ("naughty pair: ",chstring)
            return False
        # condition: at least 3 vowels
        vowelcounter=Counter(chstring)
        vowelcount = sum(vowelcounter[letter] for letter in VOWELS)
        if vowelcount<3:
            #print (f"less than 3 vowels ({vowelcount}): {chstring}")
            return False
        # condition: letter appears 2 times in a row
        if not rx1.search(chstring):
            #print ("no repeated character: ", chstring)
            return False
    #print("nice: ", chstring)
    return True

def is_nice_2(chstring: str) ->bool:
    # condition: contains a letter which repeats with another letter between (xyx)
    if not rx2.search(chstring):
        print ("no (xyx): ", chstring)
        return False
    if not rx3.search(chstring):
        print ("no repeated 2-char group: ", chstring)
        return False
    print("nice: ", chstring)
    return True


nice_1=0
nice_2=0
with open(INPUTFILE) as inputfile:
    for line in inputfile:
        if is_nice_1(line.rstrip()):  nice_1+=1
        if is_nice_2(line.rstrip()):  nice_2+=1

print("Number of nice lines (version 1): ", nice_1)
print("Number of nice lines (version 2): ", nice_2)