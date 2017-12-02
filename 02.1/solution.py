#!/bin/python3

def solve(input_file):
    with open(input_file) as file:
        input = [ list(map(int, line.split())) for line in file ]

    checksum = sum([ max(line) - min(line) for line in input ])

    return checksum

def _test_solve():
    test_values = [
        ("02.1/test_input_01.txt", 18),
    ]
    for (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("02.1/input.txt"))
