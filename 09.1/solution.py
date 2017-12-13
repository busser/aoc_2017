#!/bin/python3

# reads through a group starting at i
# returns the score of the group and the new value of i
def _parse_group(input, i, depth):
    score = depth
    i += 1 # skip opening curly bracket

    while input[i] != "}":
        if input[i] == "{":
            (score_add, i) = _parse_group(input, i, depth + 1)
            score += score_add
        elif input[i] == "<":
            i = _parse_garbage(input, i)
        elif input[i] == ",":
            i += 1 # skip commas

    i += 1 # skip closing curly bracket

    return (score, i)

# reads through garbage starting at i
# returns the new value of i
def _parse_garbage(input, i):
    i += 1 # skip opening angle bracket

    while input[i] != ">":
        if input[i] == "!":
            i += 2 # skip next character
        else:
            i += 1 # skip random characters

    i += 1 # skip closing angle bracket

    return i

def solve(input_file):
    with open(input_file) as file:
        input = file.read()[:-1] # remove new line

    i, depth = 0, 1

    (score, i) = _parse_group(input, i, depth)

    return score

def _test_solve():
    test_values = [
        ("09.1/test_input_01.txt", 1),
        ("09.1/test_input_02.txt", 6),
        ("09.1/test_input_03.txt", 5),
        ("09.1/test_input_04.txt", 16),
        ("09.1/test_input_05.txt", 1),
        ("09.1/test_input_06.txt", 9),
        ("09.1/test_input_07.txt", 9),
        ("09.1/test_input_08.txt", 3),
    ]
    for (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("09.1/input.txt"))
