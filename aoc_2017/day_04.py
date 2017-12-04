from aoclib import AOCLib

puzzle = (2017, 4)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list)

# print(puzzle_input)

# Puzzle solution part 1

validPassphrases = 0

for passphrase in puzzle_input:
    words = passphrase.split(' ')
    if len(words) == len(set(words)):
        validPassphrases += 1

print('Puzzle Output 1: {}'.format(validPassphrases))

# Puzzle solution part 2

validPassphrases = 0

for passphrase in puzzle_input:
    words = [''.join(sorted(word))
             for word in passphrase.split(' ')]
    if len(words) == len(set(words)):
        validPassphrases += 1

print('Puzzle Output 2: {}'.format(validPassphrases))
