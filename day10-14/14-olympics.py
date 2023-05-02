#!/usr/bin/python3

from collections import defaultdict

FILENAME="14-input.txt"
TIMELIMIT=2503

class Reindeer:
    # initial data
    name: str
    speed: int
    maxflighttime: int
    resttime: int
    # data that will change
    distance: int
    cycletime: int
    flying: bool
    score: int
    
    def __init__(self, name: str, speed: int, maxflighttime: int, resttime: int) -> None:
        self.name=name
        self.speed=speed
        self.maxflighttime=maxflighttime
        self.resttime=resttime
        self.distance=0
        self.flying=True
        self.cycletime=0
        self.score=0
    
    def do_round(self):
        self.cycletime+=1
        if self.flying:
            self.distance+=self.speed
            if self.cycletime>=self.maxflighttime:
                self.flying=False
                self.cycletime=0
        else:
            if self.cycletime>=self.resttime:
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