from lib.aoclib import AOCLib

puzzle = (2017, 4)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list)

# print(puzzle_input)

# Puzzle solution part 1

valid_passphrases = 0

for passphrase in puzzle_input:
    words = passphrase.split(' ')
    if len(words) == len(set(words)):
        valid_passphrases += 1

aoc.print_solution(1, valid_passphrases)

# Puzzle solution part 2

valid_passphrases = 0

for passphrase in puzzle_input:
    words = [''.join(sorted(word))
             for word in passphrase.split(' ')]
    if len(words) == len(set(words)):
        valid_passphrases += 1

aoc.print_solution(2, valid_passphrases)
