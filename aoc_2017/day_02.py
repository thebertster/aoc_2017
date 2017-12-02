from itertools import combinations
from aoclib import AOCLib

puzzle = (2017, 2)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1],
                                    AOCLib.lines_to_list)

# print(puzzle_input)

spreadsheet = [[int(cell) for cell in row.split('\t')]
               for row in puzzle_input]

# Puzzle solution part 1:

checksum_1 = sum([max(row) - min(row) for row in spreadsheet])

print('Puzzle Output 1: {}'.format(checksum_1))

# Puzzle solution part 2
# Nested loops
# Stop after match
# No max() or min()

checksum_2_1 = 0

for row in spreadsheet:
    dividend = None
    for col_1 in range(1, len(row)):
        cell_1 = row[col_1-1]
        for cell_2 in row[col_1:]:
            if cell_1 > cell_2:
                numerator, denominator = cell_1, cell_2
            else:
                numerator, denominator = cell_2, cell_1
            if numerator % denominator == 0:
                dividend = (numerator // denominator)
                break
        if dividend is not None:
            checksum_2_1 += dividend
            break

print('Puzzle Output 2#1: {}'.format(checksum_2_1))

# Alternative list comprehension "one-liner":

checksum_2_2 = sum([max(pair)//min(pair) for pair in
                  [(row[i-1], cell) for row in
                   spreadsheet for i in
                   range(1, len(row)) for cell in
                   row[i:]] if max(pair) % min(pair) == 0])

print('Puzzle Output 2#2: {}'.format(checksum_2_2))

# Alternative itertools version:

checksum_2_3 = sum([max(pair)//min(pair) for row in
                    spreadsheet for pair in
                    combinations(row, 2)
                    if max(pair) % min(pair) == 0])

print('Puzzle Output 2#3: {}'.format(checksum_2_3))
