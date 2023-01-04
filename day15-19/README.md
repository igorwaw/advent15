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