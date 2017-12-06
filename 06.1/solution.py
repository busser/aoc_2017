#!/bin/python3

def solve(input_file):
    with open(input_file) as file:
        input = list(map(int, file.read().split()))

    seen_states = set()

    while tuple(input) not in seen_states:
        seen_states.add(tuple(input))
        max_value = max(input)
        max_index = input.index(max_value)
        input[max_index] = 0
        while max_value > 0:
            max_index = (max_index + 1) % len(input)
            input[max_index] += 1
            max_value -= 1

    return len(seen_states)

def _test_solve():
    test_values = [
        ("06.1/test_input_01.txt", 5),
    ]
    for (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("06.1/input.txt"))
