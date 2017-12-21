#!/bin/python3

def solve(input_file, iterations = int(5e6),
          factorA = 16807, factorB = 48271, dividor = 2147483647):
    with open(input_file) as file:
        input = [ int(line.split()[4]) for line in file ]

    [valueA, valueB] = input
    match_count = 0

    mask = 2 ** 16 - 1

    for i in range(iterations):

        valueA = valueA * factorA % dividor
        while (valueA % 4 != 0):
            valueA = valueA * factorA % dividor

        valueB = valueB * factorB % dividor
        while (valueB % 8 != 0):
            valueB = valueB * factorB % dividor

        if (valueA ^ valueB) & mask == 0:
            match_count += 1

    return match_count

def _test_solve():
    test_values = [
        ("15.2/test_input_01.txt", 309),
    ]
    for  (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("15.2/input.txt"))
