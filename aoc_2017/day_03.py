import math
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

print('Puzzle Output 1#1: {}'.format(abs(x) + abs(y)))

# Puzzle solution part 1 - no loops required!
# Diagonal right & down are perfect squares
# Find odd perfect square >= puzzle_input and count backwards
# Use symmetry to our advantage!

square_size = 2*(math.ceil(math.sqrt(puzzle_input))//2) + 1
top_left = (square_size - 2)*square_size + 2
difference = square_size*square_size - max(puzzle_input,
                                           2*top_left - puzzle_input)
x_diff = min(square_size - 1, difference)
y_diff = max(0, difference - square_size + 1)
x = (square_size - 1)//2 - (x_diff if puzzle_input > top_left else y_diff)
y = (1 - square_size)//2 + (y_diff if puzzle_input > top_left else x_diff)

print('Puzzle Output 1#2: {}'.format(abs(x) + abs(y)))

# Puzzle solution part 1 - without the symmetry thing or min()/max()!

square_size = 2*(math.ceil(math.sqrt(puzzle_input))//2) + 1
difference = square_size*square_size - puzzle_input

if difference < square_size:
    x_diff = -difference
    y_diff = 0
elif difference < 2*(square_size - 1):
    x_diff = 1 - square_size
    y_diff = difference - square_size + 1
elif difference < 3*(square_size - 1):
    x_diff = difference - 3*(square_size - 1)
    y_diff = square_size - 1
else:
    x_diff = 0
    y_diff = 4*(square_size - 1) - difference

x = (square_size - 1)//2 + x_diff
y = (1 - square_size)//2 + y_diff

print('Puzzle Output 1#3: {}'.format(abs(x) + abs(y)))

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
