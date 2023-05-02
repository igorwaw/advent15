# Day 20: Infinite Elves and Infinite Houses

Infinite number of elves deliver presents to infinite number of houses - that looks a lot like
[Hilbert's Hotel](https://en.wikipedia.org/wiki/Hilbert's_paradox_of_the_Grand_Hotel). Luckily,
we don't really have to deal with infinities, we need to find a first house that gets more than
a specified number of presents. And there are several ways.


### Use brute force

* Iterate through all house numbers starting from 1. For each house:
* Iterate through elves - numbers from 1 to house number, let's call that value i
* Calculate: house number modulo i, if it's equal to 0, that house get 10*i presents
    
        housenumber=0
        while True:
            numpresents=0
            housenumber+=1
            for i in range(1,housenumber+1):
                if housenumber%i==0:
                    numpresents+=10*i
            if numpresents>=TARGETNUMBER:
                break

Easy to think of, easy to code. The only problem: it would take a long time (my input is an 8-digit number).

There are some possible improvements. We don't have to start from house number 1. Obviously
we need to be somewhere closer to the target number of present, we can start eg. from that
number divided by 100. Much faster than starting from 1, but still slow. And, if we start
too high we might miss the smallest number.

I actually don't know how much time it would take. After several minutes I hit Ctrl-C
and tried another approach.

### Use RAM and smarter force

The brute force solution has 2 loops: external iterates through houses, internal through
elves. That means the internal loop runs many times doing the same calculations all over
again. And, with each iteration of the external loop, internal loop needs one more iteration,
running slower and slower.

Let's reverse the logic:
* Allocate a data structure (eg. in Python list of ints) holding numbers of presents for each
house, initial value 0 (that's a few dozen MB, no problem for a PC)
* Iterate through elves, starting from number 1
* Iterate through houses, notice that elf number n puts presents in every nth house, starting with house
number n (eg. elf number ten starts with house 10, than goes to 20, 30 etc.) - which means we don't need
to start with house 1, increment by 1 and do a modulo operation, instead we can use a proper initial value
and step in the loop, massively speeding up the calculation
* For every visited house, increase the number of presents by 10*elf number
* Finally, iterate through the list of houses and find index of the first one that meets our criteria.

### Use maths

Not the solution I would find by myself, since I'm more into loops and data structures than divisors and such
stuff. Just for completeness: each house gets 10 presents if it's number is divisible by the elf's number.
So, total number of presents equals to 10 times sum of all house number's divisors (including trivial divisors).

# Day 21: RPG Simulator 20XX

Easy one for a change: a part of a very simple RPG game. I used Python and some basic OOP to encapsulate
data. The player has to use a weapon, can use an armor and up to 2 rings. My design decisions:
- weapon, armor and rings are all objects of the same class - GameItem
- all 4 equipment slots are obligatory to simplify the design, I just added armor and ring of type "none"

We need to find the lowest cost of equipment that would win the fight. Easy, there's only 1290 combinations
so we can just use brute force: generate 1290 players, make them all fight with the boss, create a list of
cost for the winning players and find a minimum of that list. These are all very fast operations (integer addition,
subtraction and comparison) so it all runs in just some miliseconds.

# Day 22: Wizard Simulator 20XX

That was a nightmare! While it seemed so similar to the previous puzzle, the code was vastly different.
And it wasn't that hard to come up with an initial design - I quickly decided I need to check all possible
games - but debugging took days! I added a lot of additional code to record and visualize (in text mode,
with curses) possible games. Most of the time I ended up with several winning solutions, including the right
one, but also with a slightly lower cost. Other times it was the other way around, I missed the right one and
only got some more expensive.

I used dataclasses heavily. I feel that OOP is the right choice for that kind of problems and dataclass decorator
allows to skip a lot of boilerplate code. That's defnitely my favourite addition to modern Python.

# Day 23: Opening the Turing Lock

That was fun, except for one trick in the instruction. We're emulating a simple computer (yay!), there's an
instruction jie - "jump if even", and next one is jio, which I automatically read as "jump if odd", although
the instruction explained it's "jump if one". Either I'm dumb or that trick is dumb, you decide.

Other than that, it's simple. Match/case to run the right command and some string parsing. Initial version had
6 more methods, one for each command, but since they were 2-6 lines and even that could be shortened, I moved all
of that directly into match/case.