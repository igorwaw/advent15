#!/usr/bin/python3

import re
import json

INPUTFILE="12-input.txt"

def parse_data(dict_or_list):
    retval=0
    if isinstance(dict_or_list, dict):
        for v in dict_or_list.values():
            if v=="red":
                return 0
            if isinstance(v, int):
                retval+=v
            elif isinstance(v, (dict, list)):
                retval+=parse_data(v)
    if isinstance(dict_or_list, list):
        for v in dict_or_list:
            if isinstance(v, int):
                retval+=v
            elif isinstance(v, (dict, list)):
                retval+=parse_data(v)
    return retval



# part 1

result=0
rx=re.compile( r'(\-?\d+)' )
with open(INPUTFILE) as inputfile:
    for line in inputfile:
        result+=sum( map(int, rx.findall(line) ) )
print("Part 1, sum: ", result)


# part 2

with open(INPUTFILE) as inputfile:
    data=json.load(inputfile)

result2=parse_data(data)
print("Part 2, sum: ", result2)

