#!/bin/python3

def solve(input_file):
    with open(input_file) as file:
        input = file.read()[:-1] # remove new line

    sum = 0

    for i in range(len(input)):
        if input[i] == input[ (i+len(input)//2) % len(input) ]:
            sum += int(input[i])

    return sum

def _test_solve():
    test_values = [
        ("01.2/test_input_01.txt", 6),
        ("01.2/test_input_02.txt", 0),
        ("01.2/test_input_03.txt", 4),
        ("01.2/test_input_04.txt", 12),
        ("01.2/test_input_05.txt", 4),
    ]
    for (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("01.2/input.txt"))
