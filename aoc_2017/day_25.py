from lib.aoclib import AOCLib

puzzle = (2017, 25)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list)

# print(puzzle_input)

begin_state = puzzle_input[0][-2]
checksum_steps = int(puzzle_input[1].split()[-2])

state_machine = {}

for state in range(3, len(puzzle_input), 10):
    next_state_0 = (int(puzzle_input[state + 2][-2]),
                    1 if puzzle_input[state + 3][-3] == 'h' else -1,
                    puzzle_input[state + 4][-2])
    next_state_1 = (int(puzzle_input[state + 6][-2]),
                    1 if puzzle_input[state + 7][-3] == 'h' else -1,
                    puzzle_input[state + 8][-2])
    state_machine[puzzle_input[state][-2]] = (next_state_0,
                                              next_state_1)

# Puzzle solution

cursor = 0
state = begin_state
tape = {}

while checksum_steps:
    current = tape.setdefault(cursor, 0)
    tape[cursor] = state_machine[state][current][0]
    cursor += state_machine[state][current][1]
    state = state_machine[state][current][2]
    checksum_steps -= 1


aoc.print_solution(1, sum(tape.values()))
