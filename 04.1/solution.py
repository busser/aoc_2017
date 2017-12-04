#!/bin/python3

def solve(input_file):
    with open(input_file) as file:
        input = [ line.split() for line in file ]

    valid = [ len(passphrase) == len(set(passphrase)) for passphrase in input]

    return sum(valid)

def _test_solve():
    test_values = [
        ("04.1/test_input_01.txt", 1),
        ("04.1/test_input_02.txt", 0),
        ("04.1/test_input_03.txt", 1),
    ]
    for (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("04.1/input.txt"))
