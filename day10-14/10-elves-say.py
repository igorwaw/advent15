#!/usr/bin/python3

SEED=1113222113
PART1_ROUNDS=40
PART2_ROUNDS=50

def look_and_say(number: str) -> str:
    prev_char=number[0]
    streaklen=1
    if len(number)==1: # special case for 1-digit number
        newnumber='1'+prev_char
        return newnumber
    newnumber=""
    for i in range(1, len(number)):
        next_char=number[i]
        if next_char==prev_char: # streak continues
            streaklen+=1
        else: # streak ended, change character and create new string
            newnumber+=str(streaklen)+prev_char
            prev_char=next_char
            streaklen=1
    newnumber+=str(streaklen)+prev_char
    return newnumber



number=str(SEED)
for i in range(PART2_ROUNDS):
    #print(f"Round {i+1}  {number} becomes ", end="")
    number=look_and_say(number)
    #print(number)
    if i==PART1_ROUNDS-1:
        print("Part 1 result: ", len(number))        

print("Part 2 result: ", len(number))