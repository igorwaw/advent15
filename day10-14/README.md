# Day 10: Elves Look, Elves Say

Now we're checking how fast look-and-say sequence grows (spoiler: fast)
Easy thing in any language with strings that:
* are dynamic length,
* can be treated as an array of characters.

I think the code is self explanatory. We're iterating through the string and
comparing current character to the previous one. If it's the same - the streak continues.
If it's different - construct the part of the result as "streak length" and "previous character".
When the loop ends, do the same construction again. Special case: string of length 1.
Remember to convert integers to strings when needed. And that's it.

Not the prettiest code as there's some repetition, but it's readable and resonably fast.

# Day 11: Corporate Policy

Similar to day 5: Python, regular expressions with backreferences. Bored now.

Huge possibility for optimization. I have 4 very short functions: 1 for incrementing
and 3 for testing each rule. The code can be made much faster - but slightly less readable -
by inlining.

# Day 12: JSAbacusFramework.io

For part 1, we need to sum all numbers in the JSON file. We don't really need to parse JSON,
just extract all the numbers and sum them. A simple regular expression will do for
extracting and classing map/reduce for the sum. I usually prefer a longer code for
redability's sake, but this just asks for putting all the contents of the main loop in
one line:
        result+=sum( map(int, rx.findall(line) ) )

For part 2, we need to ignore JSON objects (but not lists) that contain a value "red".
So now we actually have to parse the JSON. I used a recursive function that iterates
through the data, checks types, adds integers, skips dictionaries if any value is "read",
recurse into lists and dictionaries.

Note that explicit type checking is usually frowned upon by Python programmers, but I
believe it's the right tool for this job.
