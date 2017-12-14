from lib.aoclib import AOCLib
from lib.knothash import KnotHash

def count_bits(number):
    """Counts the number of 1 bits in 'number'"""

    ones = 0

    while number:
        ones += (number & 1)
        number >>= 1

    return ones

puzzle = (2017, 14)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1])

# print(puzzle_input)

# Puzzle solution part 1

num_cols = 128
num_rows = 128

hash_inputs = ['{}-{}'.format(puzzle_input, row)
               for row in range(num_rows)]

# Use a cache of part 1's answer as it takes a moderately
# long time to calculate.

hash_outputs = aoc.retrieve_some_data(puzzle[1], 'part1')

if hash_outputs is None:
    hash_outputs = [int(KnotHash.get_hash(hash_input,
                                          rounds=64)[1], 16)
                    for hash_input in hash_inputs]
    aoc.cache_some_data(puzzle[1], 'part1', hash_outputs)

used_block_count = sum([count_bits(row_hash)
                        for row_hash in hash_outputs])

print('Part 1 Solution: {}'.format(used_block_count))

# Puzzle solution part 2

grid = {}

for y in range(num_rows):
    for x in range(num_cols):
        grid[(x, y)] = -1 if (hash_outputs[y] & (1<<x)) else 0

neighbour_offsets = ((1, 0), (0, 1), (-1, 0), (0, -1))
contiguous_area = 0

for start_position in range(num_rows * num_cols):
    x = start_position % num_cols
    y = start_position // num_cols
    if grid[(x, y)] == -1:
        contiguous_area += 1
        positions_to_check = [(x, y)]
        while positions_to_check:
            check_position = positions_to_check.pop()
            grid[check_position] = contiguous_area
            neighbours = [(check_position[0] + offset[0],
                           check_position[1] + offset[1])
                          for offset in neighbour_offsets]
            positions_to_check.extend([neighbour
                               for neighbour in neighbours
                               if grid.get(neighbour, 0) == -1])

print('Part 2 Solution: {}'.format(contiguous_area))
