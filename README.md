# Advent of Code 2015

Advent of Code is a serious of programming puzzles: https://adventofcode.com/2022/about
Here is my take on the 2015 edition (completed much later)

Feel free to use for inspiration. For some tasks I implemented more than was
required because I felt like it, for others I went straight to the point.

## Technology used

![Python](https://img.shields.io/badge/python-3-blue) ![C](https://img.shields.io/badge/C-C99-green)

Task 1 solved with C. I used C99 standard and only tested with GCC 12.2.0, but it should work with any C compiler.
Task 2 solved with Python. Tested with 3.10.8, should work with any Python3


## Tasks

#### Day 1: Not Quite Lisp

Simple warm-up puzzle. The only operation on the input data was reading one character at a time and all
logic was just increment/decrement/comparison. C seemed a good choice. 

#### Day 2: I Was Told There Would Be No Math

Still simple. Some quick Python and it's done. Could be make faster, shorter etc., could be made in C,
but I didn't bother, more interesting puzzles were waiting.

#### Day 3: Perfectly Spherical Houses in a Vacuum

For part 1 I wrote some quick and dirty code again. Part 2 was interesting: we now got 2 Santas and need to keep
track of location and visited houses for them separately. So I decided to rewrite the code and do a solution more
generic than required: I added class Santa to hold all the data and a list holding arbitrary number of Santas.

#### Day 4: The Ideal Stocking Stuffer

Same as day 2.

#### Day 5: Doesn't He Have Intern-Elves For This?

Bleh. Regex with backreference.
