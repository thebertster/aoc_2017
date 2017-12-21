from lib.aoclib import AOCLib
from lib.pixelgrid import PixelGrid

puzzle = (2017, 21)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list)

# print(puzzle_input)

pixel_grid = PixelGrid(puzzle_input)

# Puzzle solution parts 1 and 2

iterations = 0

while iterations < 18:
    pixel_grid.expand_grid()
    iterations += 1

    if iterations == 5:
        aoc.print_solution(1, pixel_grid.count_pixels())

aoc.print_solution(2, pixel_grid.count_pixels())
