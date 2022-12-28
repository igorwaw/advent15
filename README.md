# Advent of Code 2015

Advent of Code is a serious of programming puzzles: https://adventofcode.com/2022/about
Here is my take on the 2015 edition (completed much later)

Feel free to use for inspiration. For some tasks I implemented more than was
required because I felt like it, for others I went straight to the point.

## Technology used

![Python](https://img.shields.io/badge/python-3-blue) ![C](https://img.shields.io/badge/C-C99-green)

Tasks 1 and 8 solved with C. I used C99 standard and only tested with GCC 12.2.0, but it should work with any C
compiler and with newer standards. 

Other tasks solved with Python. Tested with 3.6.8 and 3.10.8, should work with any Python3 - except for task 6 which 
requires at least 3.8 (I used the walrus operator).

Extra Python libraries:
* pygame for task 6
* parsimonious for task 7

## Tasks

#### Day 1: Not Quite Lisp

Simple warm-up puzzle. The only operation on the input data was reading one character at a time and all
logic was just increment/decrement/comparison. C seemed a good choice. 

#### Day 2: I Was Told There Would Be No Math

Still simple. Some quick Python and it's done. Could be made faster, shorter etc., could be made in C,
but I didn't bother, more interesting puzzles were waiting.

#### Day 3: Perfectly Spherical Houses in a Vacuum

For part 1 I wrote some quick and dirty code again. Part 2 was interesting: we now got 2 Santas and need to keep
track of location and visited houses for them separately. So I decided to rewrite the code and do a solution more
generic than required: I added class Santa to hold all the data and a list holding arbitrary number of Santas.

#### Day 4: The Ideal Stocking Stuffer

Same as day 2.

#### Day 5: Doesn't He Have Intern-Elves For This?

Bleh. Regex with backreference.

#### Day 6: Probably a Fire Hazard

Now that's more like it! The instruction only said to count how many lights are lit, but I couldn't resist
the temptation to add visualization. It's updated on every iteration for part1, but for part2 it's only
updated once in the end (it would slow the calculations too much).

#### Day 7: Some Assembly Required

We've got a list of wires that feed signals to other wires through logic gates. We need to know the state of the wire a,
but for that we need to know the state of the wire lx first. And lx references 2 other wires and so on, until we get
to the wires that have their state directly in the input file. I chose a simple solution:
* iterate through the whole list of wires,
* at each iteration do all calculations that are possible (the data is already available)
* I thought it would be cool to see how we get to the result, so I used curses to display the state of the wires in columns,
update in place and introduce a configurable delay.

For parsing the input file I borrowed the solution from https://aoc.just2good.co.uk/2015/7 and used the Parsimonious library.
In the simple case like this it would be faster to use string split, list unpacking and maybe a few simple regexps. But I'm
doing a lot of parsing in the Advent of Code and the formats are getting more complicated, so it's a good idea to learn a
proper tool.

#### Day 8: Matchsticks

The next puzzle is about encoding special characters in strings, only for a few special cases. And I didn't even need to
encode anything, just count the difference in length. 

I like to use C for such stuff. I can be sure the language is not doing any processing behind my back. And I don't mind
working with low-level code as there was no need for dynamic memory and data structures other than arrays.


#### Day 9: All in a Single Night

What a gentle introduction to graph theory: Santa needs to visit several cities with the shortest route possible.
Every Computer Science graduate will instantly recognize it as a Travelling Salesman Problem. It's a well known
problem with many real-world applications - not only obvious one of finding a shortest route between cities, but
also about placing data in the compute cluster, and optimal use of pretty much everything, from storage shelves
to industrial robots. It's also deceptively hard. Brute-force approach of trying all possible routes
is O(n!) meaning it scales with the factorial of the number of nodes so it's out of the question for bigger datasets.
Luckily, we only have 7 cities, 7! is only 5040. There's no need to implement any clever algorithm.

So, it's Python again with no special libraries (C++ with the usual STL containers would also work):
* read input file, parse lines (just two strip(), nothing fancy)
* we need 3 data structures: set of cities, dict of distances between cities (both initialized from the input data)
and list of route lengths, initially empty (note that we only need to store the distance, not the route)
* iterate through all permutations of cities (Python has a handy function in the standard library)
* for each permutations, get the distances from the dict, sum them up, store in the list of route lengths
* and just get the smallest number from the list

Possible optimization:
* No need to store the length of every route, we can only store it if it's shorter than the previous ones.
* Every route has the same length in both directions, while the code generates all permutations. So, for
the example data we check Dublin -> London -> Belfast and Belfast -> London -> Dublin. We could cut
the problem size in half by filtering out those.

Those improvements would only save a few kB of RAM and have negligible effect on time (and I'm not even sure which
way - there's less computation but some extra comparisons) so I skipped the premature optimizations.
