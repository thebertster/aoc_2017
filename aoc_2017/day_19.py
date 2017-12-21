from lib.aoclib import AOCLib

puzzle = (2017, 19)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list)

# print(puzzle_input)

# Puzzle solution parts 1 & 2

start_x = puzzle_input[0].index('|')

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

direction = 0

x = start_x
y = 0

path = []

steps = 0

while direction >= 0:
    directions_to_check = (direction, (direction + 1) % 4, (direction -1) % 4)
    for direction_to_check in directions_to_check:
        sniff_x = x + directions[direction_to_check][0]
        sniff_y = y + directions[direction_to_check][1]
        sniffed_char = puzzle_input[sniff_y][sniff_x]
        if sniffed_char != ' ':
            break
    else:
        direction_to_check = -1

    direction = direction_to_check

    if puzzle_input[y][x].isalpha():
        path.append(puzzle_input[y][x])

    steps += 1

    x = sniff_x
    y = sniff_y

aoc.print_solution(1, ''.join(path))

# Puzzle solution part 2

aoc.print_solution(2, steps)
