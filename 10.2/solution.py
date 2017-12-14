#!/bin/python3

from operator import xor
from functools import reduce

def solve(input_file, list_size = 256, round_count = 64, salt = [17, 31, 73, 47, 23]):
    with open(input_file) as file:
        input = [ ord(c) for c in file.read()[:-1] ] # remove new line

    input += salt

    numbers = list(range(list_size))
    i, skip = 0, 0

    for round in range(round_count):

        for length in input:

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

    return hash

def _test_solve():
    test_values = [
        ("10.2/test_input_01.txt", "a2582a3a0e66e6e86e3812dcb672a272"),
        ("10.2/test_input_02.txt", "33efeb34ea91902bb2f59c9920caa6cd"),
        ("10.2/test_input_03.txt", "3efbe78a8d82f29979031a4aa0b16a9d"),
        ("10.2/test_input_04.txt", "63960835bcdc130f0b66d7ff4f6a5a8e"),
    ]
    for  (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("10.2/input.txt"))
