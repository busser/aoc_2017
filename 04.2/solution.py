#!/bin/python3

def solve(input_file):
    with open(input_file) as file:
        input = [ line.split() for line in file ]

    # sort characters in each word so anagrams become duplicates
    sorted_letters = [
        [ ''.join(sorted(word)) for word in passphrase ]
        for passphrase in input
    ]

    valid = [
        len(passphrase) == len(set(passphrase))
        for passphrase in sorted_letters
    ]

    return sum(valid)

def _test_solve():
    test_values = [
        ("04.2/test_input_01.txt", 1),
        ("04.2/test_input_02.txt", 0),
        ("04.2/test_input_03.txt", 1),
        ("04.2/test_input_04.txt", 1),
        ("04.2/test_input_05.txt", 0),
    ]
    for (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("04.2/input.txt"))
