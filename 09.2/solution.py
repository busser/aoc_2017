#!/bin/python3

# reads through a group starting at i
# returns the amount of garbage and the new value of i
def _parse_group(input, i, depth):
    garbage_count = 0
    i += 1 # skip opening curly bracket

    while input[i] != "}":
        if input[i] == "{":
            (garbage_count_add, i) = _parse_group(input, i, depth + 1)
            garbage_count += garbage_count_add
        elif input[i] == "<":
            (garbage_count_add, i) = _parse_garbage(input, i)
            garbage_count += garbage_count_add
        elif input[i] == ",":
            i += 1 # skip commas

    i += 1 # skip closing curly bracket

    return (garbage_count, i)

# reads through garbage starting at i
# returns the amount of garbage and the new value of i
def _parse_garbage(input, i):
    count = 0
    i += 1 # skip opening angle bracket

    while input[i] != ">":
        if input[i] == "!":
            i += 2 # skip next character
        else:
            count += 1
            i += 1 # skip random characters

    i += 1 # skip closing angle bracket

    return (count, i)

def solve(input_file):
    with open(input_file) as file:
        input = file.read()[:-1] # remove new line

    i, depth = 0, 1

    (score, i) = _parse_group(input, i, depth)

    return score

def _test_solve():
    test_values = [
        ("09.2/test_input_01.txt", 0),
        ("09.2/test_input_02.txt", 0),
        ("09.2/test_input_03.txt", 0),
        ("09.2/test_input_04.txt", 0),
        ("09.2/test_input_05.txt", 4),
        ("09.2/test_input_06.txt", 8),
        ("09.2/test_input_07.txt", 0),
        ("09.2/test_input_08.txt", 17),
    ]
    for (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("09.2/input.txt"))
