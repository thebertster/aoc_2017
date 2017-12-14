from lib.aoclib import AOCLib

def process_jump_list(jump_list, offset_function=lambda x: x + 1):
    offset = 0
    steps = 0
    jump_list = jump_list[:]
    jump_list_len = len(jump_list)
    while offset < jump_list_len:
        offset_inc = jump_list[offset]
        jump_list[offset] = offset_function(jump_list[offset])
        offset += offset_inc
        steps += 1

    return steps

puzzle = (2017, 5)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list_int)

# print(puzzle_input)

# Puzzle solution part 1

puzzle_output = process_jump_list(puzzle_input)

print('Puzzle Output 1: {}'.format(puzzle_output))

# Puzzle solution part 2

puzzle_output = process_jump_list(puzzle_input, lambda x: x+1 if x < 3 else x-1)

print('Puzzle Output 2: {}'.format(puzzle_output))
