#!/bin/python3

def solve(input_file):
    with open(input_file) as file:
        input = [ list(map(int, line.split())) for line in file ]

    checksum = 0

    for line in input:
        line = sorted(line)
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                if line[j] % line[i] == 0:
                    checksum += line[j] // line[i]

    return checksum

def _test_solve():
    test_values = [
        ("02.2/test_input_01.txt", 9),
    ]
    for (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("02.2/input.txt"))
