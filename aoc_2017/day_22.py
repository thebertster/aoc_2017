from lib.aoclib import AOCLib

puzzle = (2017, 22)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list)

# print(puzzle_input)

c = len(puzzle_input) // 2

start_grid = {(x - c, y - c): col
        for y, row in enumerate(puzzle_input)
        for x, col in enumerate(row)}

directions = ((0, -1), (1, 0), (0, 1), (-1, 0))

# Puzzle solution part 1

grid = start_grid.copy()

direction = 0
position = (0, 0)

bursts = 10000
infected = 0

while bursts:
    if grid.setdefault(position, '.') == '#':
        direction = (direction + 1) % 4
        grid[position] = '.'
    else:
        direction = (direction - 1) % 4
        grid[position] = '#'
        infected += 1
    position = (position[0] + directions[direction][0],
                position[1] + directions[direction][1])

    bursts -= 1

aoc.print_solution(1, infected)

# Puzzle solution part 2

grid = start_grid.copy()

position = (0, 0)
direction = 0
bursts = 10000000
infected = 0

# . = clean, # = infected, F = flagged, W = weakened

while bursts:
    node = grid.setdefault(position, '.')

    if node == '#':
        direction = (direction + 1) % 4
        grid[position] = 'F'
    elif node == '.':
        direction = (direction - 1) % 4
        grid[position] = 'W'
    elif node == 'F':
        direction = (direction + 2) % 4
        grid[position] = '.'
    else:
        grid[position] = '#'
        infected += 1
    position = (position[0] + directions[direction][0],
                position[1] + directions[direction][1])

    bursts -= 1

aoc.print_solution(2, infected)
