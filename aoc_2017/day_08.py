from aoclib import AOCLib

puzzle = (2017, 8)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list)

# print(puzzle_input)

# Puzzle solution parts 1 & 2

registers = {}
python_condition = "registers['{0}'] {1} {2}"
max_value = 0

for instruction in puzzle_input:
    parsed_instruction = instruction.split(' ')

    for register_name in [parsed_instruction[0],
                          parsed_instruction[4]]:
        if register_name not in registers:
            registers[register_name] = 0

    if eval(python_condition.format(
        parsed_instruction[4],
        parsed_instruction[5],
        parsed_instruction[6]
        )):
        increment = int(parsed_instruction[2])
        if parsed_instruction[1] == 'dec':
            increment = -increment

        registers[parsed_instruction[0]] += increment

        if registers[parsed_instruction[0]] > max_value:
            max_value = registers[parsed_instruction[0]]

print('Part 1 Solution: {}'.format(
    max([register_value
         for register_value
         in registers.values()])
    ))

print('Part 2 Solution: {}'.format(max_value))
 