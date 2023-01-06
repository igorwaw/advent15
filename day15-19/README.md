# Day 15: Science for Hungry People

Another combinatorics, who would expect that? We're baking cookies, we only have 4 ingredients
and we need 100 units in total. There are many ways to achieve this, from (100, 0, 0, 0) to
(0, 0, 0, 100). Specificaly, there are 176847 ways, so some basic optimization makes a lot of sense.
I added a progress bar with tqdm because an early version took minutes and I wanted to see if
it's progressing at all. Turned out that an improved version only needs a second so it's not
really necessary. I made sure I'm filtering the list of combinations before generating
permutations and that I'm not storing more data than needed.

# Day 16: Aunt Sue

Appareantly, I have 500 aunts names Sue, some of which have a small herd of pomeranians and samoyeds.
I like the story. The puzzle itself is not that interesting, just some basic input file processing
with regexps (split() would also work) and few comparisons.

# Day 17: No Such Thing as Too Much

Another combinatorics? There's so much I might even finally memorize which one is permutation
and combination! Some copy-paste from day 15 and it's done.

# Day 18: Like a GIF For Your Yard

Animated lights, or Conway's Game of Life. As usual, we only need to provide a number for an
answer, but I couldn't resist making a visualization with Pygame.

![screenshot](https://github.com/igorwaw/advent15/blob/master/img/day18.png)

State of each light depends on the state of it's neighbours. But we can't just go through an
array calculating and changing a state of each light, because that would affect the outcome for
the neighbouring lights. My solution is to have 2 arrays of lights, one source and the other target,
alternate them every other step. How does it affect the problem size? We have 10 thousands cells and
Python's bool is really an integer, a whopping 8 bytes on a 64-bit system, so we have 2 arrays of 80 kB.
It would be a huge concern on a microcontroller with eg. 64KB of RAM, but on a PC that's nothing.

# Day 19: Medicine for Rudolph

I hated this one.

We've got a molecule and a least of possible replacements. First part was too easy: calculate how many
molecules can be made with a single replacements. I had to use a tricky way to replace first, second..., nth
occurence, but that was it.

Then the second part: how many steps we need to reach the target molecule from a single electron? I admit I
had to check how other people did it. It was obvious for me I should check the other way around: from the
molecule to the electron. And a proper parser should help. I could write them when I was at the uni, but I 
happily forgot them and hope to never need them again. I'm OK with regexps and such, but I run away screaming
when I hear about CNF, context-free grammar and so on.

Some people had luck with a randomized brute-force search: try to apply all the replacement rules, if a dead-end
was reached, shuffle the rules and try again. They said they reached a single electron in only a few shuffles.
I allowed for 200 thousands and only got some short molecules that couldn't be reduced any further. 

I also tried some order in my replacements. I noticed there are different types of rules: some duplicate the
element, some generate a group containing Rn, Ar and something in between. Some generate an element from
an electron. I tried running them in different orders, trying to eliminate longer pieces first. Reached a dead
end every time.

In desperation, I based my solution on the analisys by CdiTheKing: https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4h7ji/?utm_source=share&utm_medium=web2x&context=3
It feels like cheating because I barely understand the reasoning and couldn't reach it myself. But I don't want
to spend more time on the puzzle that's no fun.