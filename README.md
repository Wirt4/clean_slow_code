# clean_slow_code
 credit to YouTube channel "Molly Rocket" for demonstrating these comparisons

The point here is to compare equivalent lists of OOP shapes versus struct-style shapes to evaluate the claims that clean code slows performance, specifically in a scripting language like Python.

There are two summations here, one of the area of geometric shapes, rectangle, ccircle and triangle, and one of an arbitrary corner weighted area.

The struct is more performant than the OOP approach, but by a much slimmer margin than expected.

The objects and structs are unit-tested to ensure they're delivering the same outputs, remember to run `python3 -m unittest tests/*` to run all tests.
