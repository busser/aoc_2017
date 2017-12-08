#!/bin/python3

def solve(input_file):
    with open(input_file) as file:
        input = [ line.split() for line in file ]
        input = {
            line[0]:
            (
                int(line[1].strip("()")),
                [ child.strip(",") for child in line[3:] ]
            )
            for line in input
        }

    nodes = set(input)
    for node in input:
        for child in input[node][1]:
            nodes.remove(child)

    return next(iter(nodes)) # should only be one node left

def _test_solve():
    test_values = [
        ("07.1/test_input_01.txt", "tknk"),
    ]
    for (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("07.1/input.txt"))
