from aoclib import AOCLib

puzzle = (2017, 12)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list)

# print(puzzle_input)

# Solution to parts 1 & 2

pipes = {}

for data in puzzle_input:
    data_split = data.split('<->')
    program_1 = int(data_split[0])
    program_2 = tuple([int(program)
                       for program in data_split[1].split(',')])

    pipes[program_1] = program_2

# Don't really need to keep track of group membership for the puzzle
# but it seemed obvious to do so!
#
# Group membership in "groups" dictionary keyed on first element in group



groups = {}
all_groups = []

for program_check in pipes:
    if program_check not in all_groups:
        group = []
        stack = [program_check]

        while stack:
            program_1 = stack.pop()
            group.append(program_1)

            stack.extend([program_2
                          for program_2 in pipes[program_1]
                          if program_2 not in group])
        groups[program_check] = group

        all_groups.extend(group)

print('Part 1 Solution: {}'.format(len(groups[0])))
print('Part 2 Solution: {}'.format(len(groups)))
