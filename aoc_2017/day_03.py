from aoclib import AOCLib

puzzle = (2017, 3)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1], int)

# print(puzzle_input)

# Puzzle solution part 1:

# Traverse the corners of the spiral...
# Every two turns, increment the number of steps to the
# next corner.

x = 0
y = 0
d = 3
number = 1

steps = 1
increment = True
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

while number < puzzle_input:
    d = (d + 1) % 4
    number += steps
    x += steps * directions[d][0]
    y += steps * directions[d][1]
    increment = not increment
    if increment:
        steps += 1

# Backtrack if the target number is not on a corner

if number > puzzle_input:
    x -= (number-puzzle_input) * directions[d][0]
    y -= (number-puzzle_input) * directions[d][1]

print('Puzzle Output 1: {}'.format(abs(x) + abs(y)))

# Puzzle solution part 2:

directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
surrounding = tuple([(x, y) for x in (-1, 0, 1)
                     for y in (-1, 0, 1) if not x == y == 0])
position = (0, 0)
number = 1
d = 0
steps = 1
step_count = steps
increment = True
visited = {position: number}

while number < puzzle_input:
    position = (position[0] + directions[d][0],
                position[1] + directions[d][1])

    number = sum([visited.get((position[0] + check_direction[0],
                                position[1] + check_direction[1]), 0)
                   for check_direction in surrounding])

    visited[position] = number


    step_count -= 1
    if step_count == 0:
        d = (d + 1) % 4
        increment = not increment
        if increment:
            steps += 1
        step_count = steps

print('Puzzle Output 2: {}'.format(number))
