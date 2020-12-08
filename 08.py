import re


def part1(data):
    instruction_regex = r'^(acc|jmp|nop) (\+\d+|-\d+)$'

    instructions = re.findall(instruction_regex, data, re.MULTILINE)

    entered_loop = False
    called_lines = set()
    i = 0
    accumulator = 0

    while True:
        instruction = instructions[i][0]
        instruction_value = int(instructions[i][1])

        if i in called_lines:
            break
        else:
            called_lines.add(i)

        if instruction == 'acc':
            accumulator += instruction_value
            i += 1
        elif instruction == 'nop':
            i += 1
        elif instruction == 'jmp':
            i += instruction_value

    return accumulator
