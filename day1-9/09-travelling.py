#!/usr/bin/python3

from itertools import permutations


FILENAME="09-input.txt"

def read_input(filename):
    distances={}
    cityset=set()
    with open(filename) as inputfile:
        for line in inputfile:
            cities, distance=line.split('=')
            distance=int(distance)
            city1, city2 = cities.split("to")
            city1=city1.strip()
            city2=city2.strip()
            cityset.add(city1)
            cityset.add(city2)
            distances[(city1,city2)] = distance
            distances[(city2,city1)] = distance
    return distances, cityset


distances, cities=read_input(FILENAME)


routelengths=[]
for route in permutations(cities):
    current_dist = sum(
        distances[(route[i], route[i + 1])] for i in range(len(route) - 1)
    )
    routelengths.append(current_dist)

print("Shortest route: ", min(routelengths))
print("Longest route: ", max(routelengths))
