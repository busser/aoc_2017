#!/bin/python3

def solve(input_file):
    with open(input_file) as file:
        input = [ line.split() for line in file ]

    def _op_gt(a, b):
        return a > b
    def _op_lt(a, b):
        return a < b
    def _op_ge(a, b):
        return a >= b
    def _op_le(a, b):
        return a <= b
    def _op_eq(a, b):
        return a == b
    def _op_ne(a, b):
        return a != b
    def _op_inc(a, b):
        return a + b
    def _op_dec(a, b):
        return a - b

    ops = {
        ">": _op_gt,
        "<": _op_lt,
        ">=": _op_ge,
        "<=": _op_le,
        "==": _op_eq,
        "!=": _op_ne,
        "inc": _op_inc,
        "dec": _op_dec,
    }

    registers = {}

    for line in input:
        cond_reg = line[4]
        cond_op = line[5]
        cond_val = int(line[6])

        if cond_reg not in registers:
            registers[cond_reg] = 0

        if ops[cond_op](registers[cond_reg], cond_val):
            inst_reg = line[0]
            inst_op = line[1]
            inst_val = int(line[2])

            if inst_reg not in registers:
                registers[inst_reg] = 0

            registers[inst_reg] = ops[inst_op](registers[inst_reg], inst_val)

    return max(registers.values())

def _test_solve():
    test_values = [
        ("08.1/test_input_01.txt", 1),
    ]
    for (input, output) in test_values:
        assert solve(input) == output

_test_solve()
print(solve("08.1/input.txt"))
