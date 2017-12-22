#!/bin/python3

from string import ascii_letters

def solve(input_file, nb_programs = 16):
    with open(input_file) as file:
        input = file.read()[:-1].split(",") # remove new line

    programs = list(ascii_letters[:nb_programs])

    def move_spin(programs, move):
        size = int(move[1:])
        programs[:] = programs[-size:] + programs[:-size]
    def move_exchange(programs, move):
        posA = int(move[1:].split("/")[0])
        posB = int(move[1:].split("/")[1])
        programs[posA], programs[posB] = programs[posB], programs[posA]
    def move_partner(programs, move):
        nameA = move[1:].split("/")[0]
        nameB = move[1:].split("/")[1]
        for i in range(len(programs)):
            if programs[i] == nameA:
                programs[i] = nameB
            elif programs[i] == nameB:
                programs[i] = nameA

    moves = {
        "s": move_spin,
        "x": move_exchange,
        "p": move_partner,
    }

    for move in input:
        moves[move[0]](programs, move)

    return "".join(programs)

def _test_solve():
    test_values = [
        (("16.1/test_input_01.txt", 5), "baedc"),
    ]
    for  ((input, nb_programs), output) in test_values:
        assert solve(input, nb_programs) == output

_test_solve()
print(solve("16.1/input.txt"))
