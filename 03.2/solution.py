#!/bin/python3

# this solution uses math to skip many steps.
# see below for details on how this solution works.

import math

def solve(input_file):
    with open(input_file) as file:
        input = int(file.read()[:-1]) # remove new line

    x, y, n = 0, 0, 1
    dx, dy = 1, 0

    grid_size = int(math.ceil(math.sqrt(input)))
    grid = [ [ 0 for i in range(grid_size) ] for j in range(grid_size) ]
    grid[x][y] = n

    while n <= input:
        x, y = x+dx, y+dy
        n = grid[x][y-1] + grid[x][y+1] \
          + grid[x-1][y] + grid[x+1][y] \
          + grid[x-1][y-1] + grid[x-1][y+1] \
          + grid[x+1][y-1] + grid[x+1][y+1]

        grid[x][y] = n

        if dx == 1 and x == -y + 1:
            dx, dy = 0, 1
        elif dx == -1 and x == -y:
            dx, dy = 0, -1
        elif dy == 1 and y == x:
            dx, dy = -1, 0
        elif dy == -1 and y == x:
            dx, dy = 1, 0

    return n

def _test_solve():
    test_values = [
        ("03.2/test_input_01.txt", 11),
        ("03.2/test_input_02.txt", 54),
        ("03.2/test_input_03.txt", 122),
        ("03.2/test_input_04.txt", 747),
    ]
    for (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("03.2/input.txt"))

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
