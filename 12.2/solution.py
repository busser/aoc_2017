#!/bin/python3

def solve(input_file):
    with open(input_file) as file:
        input = {
            int(line.split()[0]):
            list(map(int, line.translate({ord(","): None}).split()[2:]))
        for line in file }

    stack = []
    visited = set()
    unvisited = set(input)

    group_count = 0

    while len(unvisited) > 0:

        root_node = next(iter(unvisited))

        stack.append(root_node)

        visited.add(root_node)
        unvisited.remove(root_node)

        while len(stack) > 0:

            node = stack.pop()

            for neighbor in input[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
                    unvisited.remove(neighbor)

        group_count += 1

    return group_count

def _test_solve():
    test_values = [
        ("12.2/test_input_01.txt", 2),
    ]
    for  (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("12.2/input.txt"))
