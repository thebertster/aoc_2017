from lib.aoclib import AOCLib

def solve_puzzle(circular_list, offset):
    """Solves the puzzle based on a particular offset.

    Args:
        circular_list (list): The circular list to work with.
        offset (int): The offset into the list to use.

    Returns:
        The solution.
    """
    circle_size = len(circular_list)

    running_total = 0

    for index in range(circle_size):
        index2 = (index + offset) % circle_size
        if circular_list[index] == circular_list[index2]:
            running_total += circular_list[index]

    return running_total

puzzle = (2017, 1)

# Initialise the helper library

aoc = AOCLib(puzzle[0])


# Get the puzzle input as a list of integers

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.sequence_to_int)

# print(puzzle_input)

# Puzzle solution part 1:

print('Part 1 Solution: {}'.
      format(solve_puzzle(puzzle_input, 1)))

# Puzzle solution part 2

print('Part 2 Solution: {}'.
      format(solve_puzzle(puzzle_input, len(puzzle_input)//2)))
