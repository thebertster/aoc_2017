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

# Puzzle solution part 2 (without over-iteration!):

checksum_2_1 = 0

for row in spreadsheet:
    dividend = None
    for col_1 in range(1, len(row)):
        for col_2 in range(col_1):
            numerator = row[col_1]
            denominator = row[col_2]
            if numerator < denominator:
                numerator, denominator = denominator, numerator
            if numerator % denominator == 0:
                dividend = (numerator // denominator)
                break
        if dividend is not None:
            checksum_2_1 += dividend
            break

print('Puzzle Output 2#1: {}'.format(checksum_2_1))

# Alternative list comprehension "one-liner":

checksum_2_2 = sum([numerator//denominator for (numerator, denominator) in
                  [(row[i-1], cell) if row[i-1] > cell
                   else (cell, row[i-1]) for row in
                   spreadsheet for i in
                   range(1, len(row)) for cell in
                   row[i:]] if numerator % denominator == 0])

print('Puzzle Output 2#2: {}'.format(checksum_2_2))
