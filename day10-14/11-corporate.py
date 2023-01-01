#!/usr/bin/python3

import re

FORBIDDEN=['i', 'o', 'l']
rx1=re.compile(r"(\w)\1.*(\w)\2")


password="cqjxjnds"

def increment(text: str) ->str:
    char_array=list(text)
    for i in range(7,-1,-1):
        char_array[i]=chr(ord( char_array[i] ) + 1)
        if char_array[i]>'z':
            char_array[i]='a'
        else:
            break
    return "".join(char_array)

def rule1(text: str) -> bool: # 3 characters in a sequence
    for ch1, ch2, ch3 in zip (text, text[1:], text[2:]):
        if (ord(ch3)-ord(ch2)==1) and (ord(ch2)-ord(ch1)==1):
            return True
    return False

def rule2(text: str) -> bool:  # does not contain forbidden characters
    for char in text:
        if char in FORBIDDEN:
            return False
    return True

def rule3(text: str) -> bool:  # contains at least 2 different pairs
    pairsearch=rx1.search(text)
    if pairsearch: # found 2 pairs
        pair1, pair2= pairsearch.groups()
        if pair1 != pair2: # and they are different
                return True
    return False


print ("Old password: ", password)

while(True):
    password=increment(password)
    if rule1(password) and rule2(password) and rule3(password):
        break
print("Part 1: ", password)
while(True):
    password=increment(password)
    if rule1(password) and rule2(password) and rule3(password):
        break
print("Part 2: ", password)

