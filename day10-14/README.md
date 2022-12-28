# Day 10: Elves Look, Elves Say

Now we're checking how fast look-and-say sequence grows (spoiler: fast)
Easy thing in any language with strings that:
* are dynamic length,
* can be treated as an array of characters.

I think the code is self explanatory. We're iterating through the string and
comparing current character to the previous one. If it's the same - the streak continues.
If it's different - construct the part of the result as "streak lenth" and "previous character".
When the loop ends, do the same construction again. Special case: string of length 1.

Not the prettiest code as there's some repetition, but it's readable and resonably fast.