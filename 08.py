import re


def part1(data):
    instruction_regex = r'^(acc|jmp|nop) (\+\d+|-\d+)$'
    instructions = re.findall(instruction_regex, data, re.MULTILINE)

    accumulator = run_boot_sequence(instructions)

    return accumulator


def part2(data):
    instruction_regex = r'^(acc|jmp|nop) (\+\d+|-\d+)$'
    instructions = re.findall(instruction_regex, data, re.MULTILINE)

    accumulator = run_boot_sequence_modified(instructions)

    return accumulator


def run_boot_sequence(instructions, modify_loop=False):
    called_lines = set()
    current_line = 0
    accumulator = 0
    loop_encountered = False

    while True:
        if current_line >= len(instructions):
            break

        instruction = instructions[current_line][0]
        instruction_value = int(instructions[current_line][1])

        if current_line in called_lines:
            loop_encountered = True
            break
        else:
            called_lines.add(current_line)

        if instruction == 'acc':
            accumulator += instruction_value
            current_line += 1
        elif instruction == 'nop':
            current_line += 1
        elif instruction == 'jmp':
            current_line += instruction_value

    return (accumulator, loop_encountered)


def run_boot_sequence_modified(instructions):

    flippable_instructions_indices = [
        i for i, instr in enumerate(instructions)
        if instr[0] == 'jmp' or instr[0] == 'nop'
    ]

    accumulator = 0

    for i in flippable_instructions_indices:
        instructions_modified = instructions.copy()
        instructions_modified[i] = modify_instruction(instructions_modified[i])

        accumulator, loop_encountered = run_boot_sequence(
            instructions_modified)

        if not loop_encountered:
            break

    return accumulator


def modify_instruction(instruction):
    if instruction[0] == 'jmp':
        modified_instruction = 'nop'
    elif instruction[0] == 'nop':
        modified_instruction = 'jmp'

    modified_instruction = (modified_instruction, instruction[1])

    return modified_instruction
