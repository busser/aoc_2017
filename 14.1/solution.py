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

    return sum([ sum(line) for line in grid ])

def _test_solve():
    test_values = [
        ("14.1/test_input_01.txt", 8108),
    ]
    for  (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("14.1/input.txt"))
