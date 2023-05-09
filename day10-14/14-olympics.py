#!/usr/bin/python3

from collections import defaultdict
from dataclasses import dataclass

FILENAME="14-input.txt"
TIMELIMIT=2503

@dataclass
class Reindeer:
    # initial data
    name: str
    speed: int
    maxflighttime: int
    resttime: int
    # data that will change
    distance: int = 0
    cycletime: int = 0
    flying: bool = True
    score: int = 0
    
    
    def do_round(self):
        self.cycletime+=1
        if self.flying:
            self.distance+=self.speed
            if self.cycletime>=self.maxflighttime:
                self.flying=False
                self.cycletime=0
        elif self.cycletime>=self.resttime:
            self.flying=True
            self.cycletime=0




# parse input
reindeers=[]
maxdistances=defaultdict()
with open(FILENAME) as inputfile:
    for line in inputfile:
        name, _, _, speed, _, _, maxflighttime, _, _, _, _, _, _, resttime, _= line.split()
        reindeers.append(Reindeer(name, int(speed), int(maxflighttime), int(resttime)))

# do rounds
for _ in range(TIMELIMIT):
    for r in reindeers:
        r.do_round()
        maxdistances[r.name]=r.distance
    for r in reindeers:
        if r.distance==max(maxdistances.values()):
            r.score+=1

# find score
maxscore=0
for r in reindeers:
    print(r.name, r.score)
    if r.score > maxscore:
        maxscore=r.score

print("Part 1, max distance: ", max(maxdistances.values()))
print("Part 2, max score: ", maxscore)