from lib.aoclib import AOCLib

def generate(quantity, start, factor, divisor, multiple=1):
    """The generator function.

    Args:
        quantity (int): The number of numbers to generate.
        start (int): The initial value.
        factor (int): The multiplicative factor.
        divisor (int): The divisor to use.
        multiple (int): The multiple to check for.
    Yields:
        The next value
    """
    value = start

    while quantity:
        if (value % multiple) == 0:
            yield value
            quantity -= 1
        value = (value * factor) % divisor

puzzle = (2017, 15)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list)

generator_divisor = 2147483647

generator_a_start = int(puzzle_input[0].split(' starts with ')[1])
generator_b_start = int(puzzle_input[1].split(' starts with ')[1])

# Puzzle solution part 1

generator_a_factor = 16807
generator_b_factor = 48271
number = 40000000

judge_count = 0

for a, b in zip(generate(number,
                         generator_a_start,
                         generator_a_factor,
                         generator_divisor),
                generate(number,
                         generator_b_start,
                         generator_b_factor,
                         generator_divisor)):
    if (a & 0xffff) == (b & 0xffff):
        judge_count += 1

aoc.print_solution(1, judge_count)

# Puzzle solution part 2

generator_a_multiple = 4
generator_b_multiple = 8
number = 5000000

judge_count = 0

for a, b in zip(generate(number,
                         generator_a_start,
                         generator_a_factor,
                         generator_divisor,
                         generator_a_multiple),
                generate(number,
                         generator_b_start,
                         generator_b_factor,
                         generator_divisor,
                         generator_b_multiple)):
    if (a & 0xffff) == (b & 0xffff):
        judge_count += 1

aoc.print_solution(2, judge_count)
