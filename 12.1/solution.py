#!/bin/python3

def solve(input_file):
    with open(input_file) as file:
        input = {
            int(line.split()[0]):
            list(map(int, line.translate({ord(","): None}).split()[2:]))
        for line in file }

    stack = [0]
    visited = set(stack)

    while len(stack) > 0:

        node = stack.pop()
        
        visited.add(node)

        for neighbor in input[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    return len(visited)

def _test_solve():
    test_values = [
        ("12.1/test_input_01.txt", 6),
    ]
    for  (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("12.1/input.txt"))
