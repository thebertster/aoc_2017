import re
from lib.aoclib import AOCLib

puzzle = (2017, 7)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1])

# print(puzzle_input)

# Puzzle solution part 1

regex_pattern = r'^([a-z]+) \((\d+)\)(?: -> )?(.*)$'

reg = re.compile(regex_pattern, re.M)

program_info = reg.findall(puzzle_input)

program_table = {}

# Build a table listing all the programs and associated data

for program in program_info:
    program_name = program[0]
    program_weight = int(program[1])
    if program[2] == '':
        program_supporting = []
    else:
        program_supporting = [{'program_name':program_name, 'weight_above':0}
                              for program_name in program[2].split(', ')]

    program_table[program_name] = {'weight':program_weight,
                                   'supporting':program_supporting,
                                   'supported_by':None}

# For each program X, update the programs it supports to identify
# that it is supported by this X

for program_name, program_data in program_table.items():
    for supporting_program in program_data['supporting']:
        supporting_program_name = supporting_program['program_name']
        program_table[supporting_program_name]['supported_by'] = program_name

# The "root" programs are then the ones with empty "supported by"
# lists (there should be only one according to the puzzle text)

root_programs = [program_name
                 for program_name, program_data
                 in program_table.items()
                 if program_data['supported_by'] is None]

print('Part 1 Solution: {}'.format(', '.join(root_programs)))

# Puzzle solution part 2

# Traverse the tree we built previously from its root(s) and
# bubble up the weights of each program to the supporting programs

traverse_tree = root_programs[:]

while traverse_tree:
    program_name = traverse_tree.pop()

    this_program = program_table[program_name]

    traverse_tree.extend(list(supporting['program_name']
                         for supporting
                         in this_program['supporting']))

    weight = this_program['weight']

    parent_program = this_program['supported_by']

    while parent_program:
        for supported_program in program_table[parent_program]['supporting']:
            if supported_program['program_name'] == program_name:
                supported_program['weight_above'] += weight
        program_name = parent_program
        parent_program = program_table[parent_program]['supported_by']

# From the root (assume now there is only one), follow the
# unbalanced path to find the program with an unbalanced tower
# but where the supported programs themselves have balanced towers.
# This must be the program with the incorrect weight.

unbalanced_program = root_programs[0]

while True:
    max_weight = -1
    min_weight = -1
    max_weight_program = None
    for supported_program in program_table[unbalanced_program]['supporting']:
        if max_weight == -1 or supported_program['weight_above'] > max_weight:
            max_weight_program = supported_program
            max_weight = supported_program['weight_above']
        if min_weight == -1 or supported_program['weight_above'] < min_weight:
            min_weight = supported_program['weight_above']

    if max_weight != min_weight:
        unbalanced_program = max_weight_program['program_name']
        current_weight = program_table[unbalanced_program]['weight']
        correct_weight = current_weight - (max_weight - min_weight)
    else:
        break

print('Part 2 Solution: {} should weigh {}'.
      format(unbalanced_program, correct_weight))
