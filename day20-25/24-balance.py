#!/usr/bin/python3

import math
from itertools import combinations

INPUTFILE="24-input.txt"


def calculate_min_qe(num_containers: int):
    target_weight=sum(packages)//num_containers
    has_right_weight=[]

    for i in range(1,len(packages)):
        has_right_weight.extend(  x for x in combinations(packages,i) if sum(x)==target_weight )
        if has_right_weight:
            break

    qe= [ math.prod(x) for x in has_right_weight ]
    return min(qe)


packages=[]
with open(INPUTFILE) as f:
    packages.extend(int(line) for line in f)

print(f"Part 1: {calculate_min_qe(3)}")
print(f"Part 2: {calculate_min_qe(4)}")