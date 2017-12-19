#!/bin/python3

from operator import xor
from functools import reduce

def solve(input_file):
    with open(input_file) as file:
        input = file.read()[:-1] # remove new line

    # knot hash constants
    list_size = 256
    round_count = 64
    salt = [17, 31, 73, 47, 23]

    hash_inputs = [ input + "-" + str(i) for i in range(128) ]
    hash_outputs = []

    for hash_input in hash_inputs:

        hash_input = [ ord(c) for c in hash_input ] + salt

        numbers = list(range(list_size))
        i, skip = 0, 0

        for round in range(round_count):

            for length in hash_input:

                if i + length < len(numbers):
                    selection = numbers[i:i+length]
                    selection.reverse()
                    numbers[i:i+length] = selection
                else:
                    selection = numbers[i:] + numbers[:i+length-len(numbers)]
                    selection.reverse()
                    numbers[i:] = selection[:len(numbers)-i]
                    numbers[:i+length-len(numbers)] = selection[len(numbers)-i:]

                i = (i + length + skip) % len(numbers)
                skip += 1

        hash = "".join([
            h if len(h) == 2 else '0'+h
            for h in [
                hex(reduce(xor, numbers[i:i+16]))[2:]
                for i in range(0, len(numbers), 16)
            ]
        ])

        hash_outputs += [ hash ]

    grid = [
        [ int(c) for c in bin(int(hash, 16))[2:].zfill(128) ]
        for hash in hash_outputs
    ]

    group_count = 0
    stack = []

    for i in range(128):
        for j in range(128):

            if grid[i][j] == 0:
                continue

            group_count += 1
            stack.append((i, j))
            grid[i][j] = 0

            while len(stack) > 0:

                (x, y) = stack.pop()

                if x > 0 and grid[x-1][y] == 1:
                    stack.append((x-1, y))
                    grid[x-1][y] = 0
                if y > 0 and grid[x][y-1] == 1:
                    stack.append((x, y-1))
                    grid[x][y-1] = 0
                if x < 127 and grid[x+1][y] == 1:
                    stack.append((x+1, y))
                    grid[x+1][y] = 0
                if y < 127 and grid[x][y+1] == 1:
                    stack.append((x, y+1))
                    grid[x][y+1] = 0

    return group_count

def _test_solve():
    test_values = [
        ("14.2/test_input_01.txt", 1242),
    ]
    for  (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("14.2/input.txt"))
