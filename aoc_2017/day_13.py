from aoclib import AOCLib

puzzle = (2017, 13)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list)

# print(puzzle_input)

# puzzle_input = ['0: 3','1: 2', '4: 4', '6: 4']

scanner_range = {}

# Bouncing scanners with range n will catch you iff
# a wrapping scanner with range 2n-2 will catch you.
#
# Condition for being caught at layer L is:
#  'L % R(L) == 0'
#
# where R(L) is the range of the scanner if it wrapped.


for layer in puzzle_input:
    layer_data = layer.split(': ')
    scanner_range[int(layer_data[0])] = int(layer_data[1]) * 2 - 2

number_of_layers = max(scanner_range.keys()) + 1

# Puzzle solution part 1

penalty = 0

for layer in scanner_range:
    if (layer % scanner_range[layer]) == 0:
        penalty += layer * ((scanner_range[layer] + 2) // 2)

print('Part 1 Solution: {}'.format(penalty))

# Puzzle solution part 2

# Condition for being caught at layer L with a delay D is
# '(L + D) % R(L) == 0'
#
# Check each layer, aborting further checks for that delay if caught

delay = 0

while True:
    for layer in scanner_range:
        if ((layer + delay) % scanner_range[layer]) == 0:
            delay += 1
            break
    else:
        break

print('Part 2 Solution: {}'.format(delay))
