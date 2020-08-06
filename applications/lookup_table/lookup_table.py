# Your code here
import math
import random

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


# instantitate lookup table
lookup_table = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # if the tuple is not in the lookup
    if (x, y) not in lookup_table:
        # add the outcome (v) of the equation to the lookup
        lookup_table[(x, y)] = slowfun_too_slow(x, y)
    # return the value
    return lookup_table[(x, y)]



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
