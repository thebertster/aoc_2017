from aoclib import AOCLib

puzzle = (2017, 5)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list_int)

# print(puzzle_input)

# Puzzle solution part 1

offset = 0
steps = 0
jump_list = puzzle_input[:]
jump_list_len = len(jump_list)
while offset < jump_list_len:
    old_offset = offset
    offset += jump_list[old_offset]
    jump_list[old_offset] += 1
    steps += 1

print('Puzzle Output 1: {}'.format(steps))

# Puzzle solution part 1

offset = 0
steps = 0
jump_list = puzzle_input[:]
jump_list_len = len(jump_list)
while offset < jump_list_len:
    offset_inc = jump_list[offset]
    jump_list[offset] += 1 if jump_list[offset] < 3 else -1
    offset += offset_inc
    steps += 1
    
print('Puzzle Output 2: {}'.format(steps))
