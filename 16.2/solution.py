#!/bin/python3

# despite my efforts to optimise this code, it runs in ~116 days (estimation).
# i suspect that python is not at all suited for this type of exercise.
# perhaps i will try to implement a solution in a lower-level language like rust.

from string import ascii_letters

def solve(input_file, nb_programs = 16, iterations = int(1e9)):
    with open(input_file) as file:
        input = file.read()[:-1].split(",") # remove new line

    id2pos = list(range(nb_programs)) # index: program ID
    pos2id = list(range(nb_programs)) # index: program position

    def move_spin(id2pos, pos2id, size):
        nb_programs = len(id2pos)
        id2pos = [ (pos + size) % nb_programs for pos in id2pos ]
        for i in range(nb_programs):
            pos2id[id2pos[i]] = i
        return (id2pos, pos2id,)
    
    def move_exchange(id2pos, pos2id, posA, posB):
        pos2id[posA], pos2id[posB] = pos2id[posB], pos2id[posA]
        id2pos[pos2id[posA]], id2pos[pos2id[posB]] = \
            id2pos[pos2id[posB]], id2pos[pos2id[posA]]
        return (id2pos, pos2id,)
    
    def move_partner(id2pos, pos2id, idA, idB):
        id2pos[idA], id2pos[idB] = id2pos[idB], id2pos[idA]
        pos2id[id2pos[idA]], pos2id[id2pos[idB]] = \
            pos2id[id2pos[idB]], pos2id[id2pos[idA]]
        return (id2pos, pos2id,)

    moves = {
        "s": move_spin,
        "x": move_exchange,
        "p": move_partner,
    }

    def parse_spin(move):
        size = int(move[1:])
        return (size,)
    
    def parse_exchange(move):
        split_move = move[1:].split("/")
        posA = int(split_move[0])
        posB = int(split_move[1])
        return (posA, posB,)
    
    def parse_partner(move):
        split_move = move[1:].split("/")
        idA = ord(split_move[0]) - ord("a")
        idB = ord(split_move[1]) - ord("a")
        return (idA, idB,)

    argument_parsers = {
        "s": parse_spin,
        "x": parse_exchange,
        "p": parse_partner,
    }

    function_calls = [ moves[move[0]] for move in input ]
    function_arguments = [ argument_parsers[move[0]](move) for move in input ]

    for i in range(iterations):
        for j in range(len(function_calls)):
            (id2pos, pos2id) = function_calls[j](
                id2pos, pos2id, *(function_arguments[j])
            )

    return "".join([ chr(id + ord("a")) for id in pos2id ])

def _test_solve():
    test_values = [
        (("16.2/test_input_01.txt", 5, 2), "ceadb"),
    ]
    for ((input, nb_programs, iterations), output) in test_values:
        assert solve(input, nb_programs, iterations) == output

_test_solve()
print(solve("16.2/input.txt", 16, int(1e9)))
