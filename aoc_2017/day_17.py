from lib.aoclib import AOCLib

puzzle = (2017, 17)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1])

# print(puzzle_input)

# Puzzle solution part 1

circular_buffer = [0]
steps = int(puzzle_input)
position = 0
new_value = 1
spins = 2017

while new_value <= spins:
    position = 1 + (position + steps) % new_value
    circular_buffer.insert(position, new_value)
    new_value += 1

print('Puzzle Output 1: {}'.format(circular_buffer[(position + 1)
                                                   % len(circular_buffer)]))

# Puzzle solution part 2

spins = 50000000

while new_value <= spins:
    position = 1 + (position + steps) % new_value
    if position == 1:
        last_insert = new_value
    new_value += 1

print('Puzzle Output 2: {}'.format(last_insert))
