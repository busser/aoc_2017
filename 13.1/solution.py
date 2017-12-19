#!/bin/python3

def solve(input_file):
    with open(input_file) as file:
        input = {
            int(line.split()[0][:-1]):
            int(line.split()[1])
            for line in file
        }

    severity = 0

    for depth, range in input.items():

        # constant-time compute of wether there is a collision
        collided = depth % (2 * (range - 1)) == 0

        if collided:
            severity += depth * range

    return severity

def _test_solve():
    test_values = [
        ("13.1/test_input_01.txt", 24),
    ]
    for  (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("13.1/input.txt"))
