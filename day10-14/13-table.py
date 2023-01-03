#!/usr/bin/python3

from itertools import permutations



FILENAME="13-input.txt"


def calculate_happiness():
    global edges, people
    happiness=[]
    for people_permut in permutations(people):
        sitting_arrangement=list(people_permut)
        sitting_arrangement.append(sitting_arrangement[0])
        #print(sitting_arrangement)
        current_happiness=0
        for i in range(len(sitting_arrangement)-1):
            current_happiness+=edges[( sitting_arrangement[i], sitting_arrangement[i+1] )]
            current_happiness+=edges[( sitting_arrangement[i+1], sitting_arrangement[i] )]
        happiness.append(current_happiness)
    return happiness

# parse input
edges={}
people=set()
with open(FILENAME) as inputfile:
    for line in inputfile:
        person, _, direction, howmuch, _, _, _, _, _, _, otherperson = line.strip().split()
        otherperson=otherperson.strip('.')
        if direction=='gain':
            value=int(howmuch)
        elif direction=='lose':
            value=-int(howmuch)
        else:
            raise ValueError
        people.add(person)
        edges[(person, otherperson)]=value

happiness=calculate_happiness()
print("Part 1: ", max(happiness))

# add another person
for person in people:
    edges[person, "me"]=0
    edges["me", person]=0
people.add("me")

happiness=calculate_happiness()
print("Part 2: ", max(happiness))
