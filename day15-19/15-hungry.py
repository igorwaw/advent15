#!/usr/bin/python3

import re
from itertools import permutations, combinations_with_replacement
from tqdm import tqdm
from dataclasses import dataclass


FILENAME="15-input.txt"
MAXSIZE=100
TARGETCALORIES=500

@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


class Cookie:
    calories: int
    totalscore: int

    def __init__(self, ingr: tuple) -> None:
        global ingredients
        capacity=0
        durability=0
        flavor=0
        texture=0
        self.calories=0
        for num, amount in enumerate(ingr):
            capacity += amount*ingredients[num].capacity
            durability += amount*ingredients[num].durability
            flavor += amount*ingredients[num].flavor
            texture += amount*ingredients[num].texture
            self.calories += amount*ingredients[num].calories
        capacity = max(capacity, 0)
        durability = max(durability, 0)
        flavor = max(flavor, 0)
        texture = max(texture, 0)
        self.totalscore=capacity*durability*flavor*texture


# parse input file
ingredients=[]
rx=re.compile( r"(\w+): capacity (\-?\d+), durability (\-?\d+), flavor (\-?\d+), texture (\-?\d+), calories (\-?\d+)" )
with open(FILENAME) as inputfile:
    for line in inputfile:
        name, capacity, durability, flavor, texture, calories = rx.match(line).groups()
        ingredients.append(Ingredient(name, int(capacity), int(durability), int(flavor), int(texture), int(calories)))

# calculate permutations
num_ingredients=len(ingredients)
ingr_combinations=[ i for i in combinations_with_replacement(range(MAXSIZE), num_ingredients) if sum(i)==MAXSIZE ]
print (f"Got {len(ingr_combinations)} combinations, calculating permutations of combinations")
ingr_permutations=set()
for combination in ingr_combinations:
    for i in permutations(combination):
        ingr_permutations.add(i)
print(f"Got {len(ingr_permutations)} permutations of combinations")

# bake cookies
maxscore=0
maxwithtarget=0
for recipe in tqdm(ingr_permutations):
    cookie=Cookie(recipe)
    maxscore=max(maxscore, cookie.totalscore)
    if cookie.calories == TARGETCALORIES and cookie.totalscore > maxwithtarget:
        maxwithtarget=cookie.totalscore

print("Part 1, max score: ", maxscore)
print("Part 2, max score: ", maxwithtarget)


