from lib.aoclib import AOCLib

puzzle = (2017, 6)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1],
                                    lambda x: [int(y) for y in x.split('\t')])

# print(puzzle_input)

# Puzzle solution parts 1 and 2

banks = puzzle_input[:]
number_of_banks = len(banks)
state_history = {}
cycles = 0

while True:
    state_history[tuple(banks)] = cycles

    biggest_bank_size = -1
    for bank_index, check_bank in enumerate(banks):
        if check_bank > biggest_bank_size:
            biggest_bank = bank_index
            biggest_bank_size = check_bank

    banks[biggest_bank] = 0

    banks = [bank + biggest_bank_size//number_of_banks for bank in banks]

    for inc_bank in range(biggest_bank_size % number_of_banks):
        banks[(biggest_bank + inc_bank + 1) % number_of_banks] += 1

    cycles += 1

    if tuple(banks) in state_history:
        break

aoc.print_solution(1, cycles)
aoc.print_solution(2, cycles - state_history[tuple(banks)])
