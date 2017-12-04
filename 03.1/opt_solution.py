#!/bin/python3

# this solution uses math to skip many steps.
# because of this, it has better performance but can not be used
# as a basis for the day's second problem.
# see below for details on how this solution works.

import math

def solve(input_file):
    with open(input_file) as file:
        input = int(file.read()[:-1]) # remove new line

    v = int(math.floor((math.sqrt(input - 1) - 1) / 2))
    x, y, n = v+1, -v, (2*v+1)**2+1

    if n == input:
        return abs(x) + abs(y)

    # move up (increment y)
    if x - y > input - n:
        y += input - n
        return abs(x) + abs(y)
    else:
        n += x - y
        y = x

    # move left (decrement x)
    if x + y > input - n:
        x -= input - n
        return abs(x) + abs(y)
    else:
        n += x + y
        x = -y

    # move down (decrement y)
    if y - x > input - n:
        y -= input - n
        return abs(x) + abs(y)
    else:
        n += y - x
        y = x

    # move right (increment x)
    if -x - y > input - n:
        x += input - n
        return abs(x) + abs(y)
    else:
        n += -x - y
        x = -y

    return abs(x) + abs(y)

def _test_solve():
    test_values = [
        ("03.1/test_input_01.txt", 0),
        ("03.1/test_input_02.txt", 3),
        ("03.1/test_input_03.txt", 2),
        ("03.1/test_input_04.txt", 31),
    ]
    for (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("03.1/input.txt"))

# solution explaination
# =====================
# let x and y be the coordinates at which number n ends up in the spiral,
# with x = 0 and y = 0 when n = 1
#
# x and y start at 0; n starts at 1.
# x and y fluctuate according to the following pattern (each incrementation
# or decrementation of x or y means an incrementation of n):
# repeat these steps:
#   x increments until at -y+1 (y is negative here)
#   y increments until at x
#   x decrements until at -y
#   y decrements until at x
#
# let v be any positive of null integer
# if n = (2v+1)^2+1 then x = v+1 and y = -v
# the largest value of v so that (2v+1)^2+1 <= n is floor((sqrt(n-1)-1)/2)
# this formula allows skipping whole "loops" made in the spiral
# the solution works around the final (incomplete) "loop" to find the
# values of x and y for given n
