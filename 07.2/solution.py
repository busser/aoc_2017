#!/bin/python3

from collections import Counter

# returns whether node and its children are balanced
# if balanced, also returns total weight
# if inbalanced, also returns tuple(faulty node, desired weight)
def _check_balanced(nodes, node):
    (weight, children) = nodes[node]
    child_weights = []

    for child in children:
        (balanced, details) = _check_balanced(nodes, child)
        if balanced:
            child_weights.append(details)
        else:
            return (False, details)

    if len(set(child_weights)) <= 1: # if all child weights equal
        return (True, weight + sum(child_weights))

    weight_count = Counter(child_weights)

    for weight in weight_count.keys():
        if weight_count[weight] == 1:
            wrong_weight = weight
        else:
            correct_weight = weight

    wrong_child_index = child_weights.index(wrong_weight)
    faulty_node = children[wrong_child_index]
    desired_weight = nodes[faulty_node][0] - wrong_weight + correct_weight

    return (False, (faulty_node, desired_weight))

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

    root_node = next(iter(nodes))

    (balanced, details) = _check_balanced(input, root_node)

    return details[1]

def _test_solve():
    test_values = [
        ("07.2/test_input_01.txt", 60),
    ]
    for (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("07.2/input.txt"))
