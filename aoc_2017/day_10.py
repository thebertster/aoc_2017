from lib.aoclib import AOCLib
from lib.knothash import KnotHash

puzzle = (2017, 10)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1])

# print(puzzle_input)

awful_hash_1 = KnotHash.get_hash(AOCLib.to_list_int(puzzle_input))

aoc.print_solution(1, awful_hash_1[0][0]* awful_hash_1[0][1])

puzzle_lengths = [ord(character) for character in puzzle_input]
puzzle_lengths.extend([17, 31, 73, 47, 23])

awful_hash_2 = KnotHash.get_hash(puzzle_lengths, rounds=64)

aoc.print_solution(2, awful_hash_2[1])
                                   