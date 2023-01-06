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
* pygame for task 6 and 18
* parsimonious for task 7
* tqdm for task 15 and 20 (progress bar, can be removed)

## Tasks

See subdirectories.