from aoclib import AOCLib

def hex_distance(hex_point_1, hex_point_2=(0, 0, 0)):
    return (abs(hex_point_2[0] - hex_point_1[0])
           + abs(hex_point_2[1] - hex_point_1[1])
           + abs(hex_point_2[2] - hex_point_1[2])) // 2

puzzle = (2017, 11)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.to_list)

# print(puzzle_input)

# Tri-axis representation:
# x-axis = e->w
# y-axis = se->nw
# z-axis = ne->sw
#
# A step in any direction increases two of the co-ordinates by 1
# therefore each step increases the absolute values of the sum
# of the co-ordinates by 2. And so:
#
# Distance metric = (|x2-x1| + |y2-y1| + |z2-z1|) / 2

directions = {'n':(0, 1, -1),
              's':(0, -1, 1),
              'ne':(1, 0, -1),
              'nw':(-1, 1, 0),
              'se':(1, -1, 0),
              'sw':(-1, 0, 1)}

#puzzle_input = ['ne','se','s']

position = (0, 0, 0)

max_steps_from_origin = 0

for step in puzzle_input:
    position = (position[0] + directions[step][0],
                position[1] + directions[step][1],
                position[2] + directions[step][2])

    steps_from_origin = hex_distance(position)

    if steps_from_origin > max_steps_from_origin:
        max_steps_from_origin = steps_from_origin

print('Part 1 Solution: {}'.format(steps_from_origin))
print('Part 2 Solution: {}'.format(max_steps_from_origin))
