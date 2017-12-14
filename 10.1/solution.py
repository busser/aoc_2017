#!/bin/python3

def solve(input_file, list_size = 256):
    with open(input_file) as file:
        input = list(map(int, file.read().split(",")))

    numbers = list(range(list_size))
    i, skip = 0, 0

    for length in input:

        if i + length < len(numbers):
            selection = numbers[i:i+length]
            selection.reverse()
            numbers[i:i+length] = selection
        else:
            selection = numbers[i:] + numbers[:i+length-len(numbers)]
            selection.reverse()
            numbers[i:] = selection[:len(numbers)-i]
            numbers[:i+length-len(numbers)] = selection[len(numbers)-i:]

        i = (i + length + skip) % len(numbers)
        skip += 1

    return numbers[0] * numbers[1]

def _test_solve():
    test_values = [
        (("10.1/test_input_01.txt", 5), 12),
    ]
    for ((input, list_size), output) in test_values:
        assert solve(input, list_size) == output

_test_solve()
print(solve("10.1/input.txt"))
