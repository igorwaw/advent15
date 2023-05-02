#!/usr/bin/python3
from dataclasses import dataclass

@dataclass
class GameItem:
    name: str
    cost: int
    damage: int
    armor: int

@dataclass
class Boss:
    totaldamage: int
    totalarmor: int
    hitpoints: int

class Player:
    totalcost: int
    totaldamage: int
    totalarmor: int
    hitpoints: int
    won: bool

    def __init__(self, equip) -> None:
        self.hitpoints=100
        self.totalarmor=self.totaldamage=self.totalcost=0
        for i in equip:
            self.totalcost+=i.cost
            self.totaldamage+=i.damage
            self.totalarmor+=i.armor

    def __repr__(self) -> str:
        return f"Player:  hp: {self.hitpoints}  cost: {self.totalcost} armor: {self.totalarmor} damage: {self.totaldamage}"

    def fight(self, boss):
        while True:
            # player attacks
            damage_done=self.totaldamage-boss.totalarmor
            damage_done = max(damage_done, 1)
            boss.hitpoints-=damage_done
            if boss.hitpoints<=0:
                self.won=True
                print("+",end="")
                break
            # boss attacks
            damage_done=boss.totaldamage-self.totalarmor
            damage_done = max(damage_done, 1)
            self.hitpoints-=damage_done
            if self.hitpoints<=0:
                self.won=False
                print("-",end="")
                break


weapons=(
       GameItem("Dagger", 8, 4, 0),
       GameItem("Shortsword", 10, 5, 0),
       GameItem("Warhammer", 25, 6, 0),
       GameItem("Longsword", 40, 7, 0),
       GameItem("Greataxe ", 74, 8,0)
)

armors=(
       GameItem("None", 0, 0, 0),
       GameItem("Leather", 13, 0, 1),
       GameItem("Chainmail", 31, 0, 2),
       GameItem("Splintmail", 53, 0, 3),
       GameItem("Bandedmail", 75, 0, 4),
       GameItem("Platemail", 102, 0, 5)
)

rings=(
       GameItem("None", 0, 0, 0),
       GameItem("Damage +1", 25, 1, 0),
       GameItem("Damage +2", 50, 2, 0),
       GameItem("Damage +3", 100, 3, 0),
       GameItem("Defense +1", 20, 0, 1),
       GameItem("Defense +2", 40,0, 2),
       GameItem("Defense +3", 80, 0, 3)
)



players=[]
for w in weapons:
    for a in armors:
        for l in rings:
            for r in rings:
                if (l.name==r.name) and (l.name!="None" and r.name!="None"): # you can't have 2 of the same rings
                    continue
                players.append(Player( (w,a,l,r) ))


for p in players:
    boss=Boss(totaldamage=9, totalarmor=2, hitpoints=103)
    p.fight(boss)
 

winning=[ p.totalcost for p in players if p.won ]
losing=[ p.totalcost for p in players if not p.won ]
print(f"\n\nGenerated {len(players)} players of which {len(winning)} won.")
print("Part 1, lowest cost of winning: ", min(winning))
print("Part 2, highest cost of losing: ", max(losing))
