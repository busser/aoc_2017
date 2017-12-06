#!/bin/python3

def solve(input_file):
    with open(input_file) as file:
        input = [ int(line) for line in file ]

    i, count = 0, 0

    while i >= 0 and i < len(input):
        offset = input[i]
        input[i] += 1 if offset < 3 else -1
        i += offset
        count += 1

    return count

def _test_solve():
    test_values = [
        ("05.2/test_input_01.txt", 10),
    ]
    for (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("05.2/input.txt"))
