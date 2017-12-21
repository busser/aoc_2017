#!/bin/python3

# while it would make sense to use generators for this solution, the overhead
# makes the solution ~1.5x slower so I chose not to use them.

def solve(input_file, iterations = int(4e7),
          factorA = 16807, factorB = 48271, divider = 2147483647):
    with open(input_file) as file:
        input = [ int(line.split()[4]) for line in file ]

    [valueA, valueB] = input
    match_count = 0

    mask16 = 2 ** 16 - 1

    for i in range(iterations):

        valueA = valueA * factorA % divider
        valueB = valueB * factorB % divider

        if (valueA ^ valueB) & mask16 == 0:
            match_count += 1

    return match_count

def _test_solve():
    test_values = [
        ("15.1/test_input_01.txt", 588),
    ]
    for  (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("15.1/input.txt"))
