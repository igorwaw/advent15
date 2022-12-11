#!/usr/bin/python3

from dataclasses import dataclass
INPUTFILE="03-input.txt"



numsantas=2 # how many Santas
counter=0 # instruction counter

@dataclass
class Santa:
    x: int
    y: int
    visited: set[int,int]
    
    def __init__(self, x=0, y=0):
        self.x=0
        self.y=0
        self.visited=set()
        self.record_visit()

    def record_visit(self):
        #print("Recording visit in ", self.x, self.y)
        self.visited.add( (self.x, self.y) )




santas: list[Santa] = []
for i in range(0, numsantas):
    santas.append( Santa() )


with open(INPUTFILE) as inputfile:
    while True:
        s=counter%numsantas
        c=inputfile.read(1)
        #print(f"Counter {counter} instruction {c} santa {s}")
        if not c:
            break
        if   c=='<': santas[s].x-=1
        elif c=='>': santas[s].x+=1
        elif c=='^': santas[s].y+=1
        elif c=='v': santas[s].y-=1
        else:
            print("Error: unkown direction ",c)
        santas[s].record_visit()
        counter+=1


print ("Houses visited by each Santa")
totalvisitsnum=0
totalvisited=set()
for i in range(0, numsantas):
    visits=len(santas[i].visited)
    totalvisited=totalvisited|santas[i].visited
    print(f"  Santa {i}  houses {visits}")
    #print(santas[i])
print("Total: ", len(totalvisited))
