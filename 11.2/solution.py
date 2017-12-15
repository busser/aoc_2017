#!/bin/python3

def solve(input_file):
    with open(input_file) as file:
        input = file.read()[:-1].split(",") # remove new line

    moves = {}
    for move in ("n", "ne", "nw", "s", "se", "sw"):
        moves[move] = 0

    max_distance = 0

    for direction in input:
        moves[direction] += 1

        for opposites in (("n", "s"), ("nw", "se"), ("ne", "sw"),
                          ("n", "se", "sw"), ("s", "ne", "nw")):
            canceled = min([ moves[key] for key in opposites ])
            for key in opposites:
                moves[key] -= canceled

        while True:
            no_change = True

            for additions in (("n", "se", "ne"), ("n", "sw", "nw"),
                              ("ne", "nw", "n"), ("s", "ne", "se"),
                              ("s", "nw", "sw"), ("se", "sw", "s")):

                added = min([ moves[key] for key in additions[:2] ])

                for key in additions[:2]:
                    moves[key] -= added
                for key in additions[2:]:
                    moves[key] += added

                if added > 0:
                    no_change = False

            if no_change:
                break;

        max_distance = max(max_distance, sum(moves.values()))

    return max_distance

def _test_solve():
    test_values = [
        ("11.2/test_input_01.txt", 3),
        ("11.2/test_input_02.txt", 2),
        ("11.2/test_input_03.txt", 2),
        ("11.2/test_input_04.txt", 3),
    ]
    for  (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("11.2/input.txt"))
