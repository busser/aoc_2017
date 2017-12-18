#!/bin/python3

def solve(input_file):
    with open(input_file) as file:
        input = {
            int(line.split()[0][:-1]):
            int(line.split()[1])
            for line in file
        }

    delay = 0

    while True:

        severity = 0

        for depth, range in input.items():

            # constant-time compute of wether there is a collision
            collided = (
                range - 1 - abs((depth + delay) % (2 * (range - 1)) - (range - 1))
            ) == 0

            if collided:
                break

        if collided:
            delay += 1
        else:
            break

    return delay

def _test_solve():
    test_values = [
        ("13.2/test_input_01.txt", 10),
    ]
    for  (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("13.2/input.txt"))
