#!/bin/python3

def solve(input_file):
    with open(input_file) as file:
        input = file.read()[:-1] # remove new line

    sum = 0

    for i in range(len(input)):
        if input[i] == input[ (i+1) % len(input) ]:
            sum += int(input[i])

    return sum

def _test_solve():
    test_values = [
        ("01.1/test_input_01.txt", 3),
        ("01.1/test_input_02.txt", 4),
        ("01.1/test_input_03.txt", 0),
        ("01.1/test_input_04.txt", 9),
    ]
    for (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("01.1/input.txt"))
