from lib.aoclib import AOCLib

def dance(start_position, instructions, instruction_filter='sxp'):
    end_position = start_position[:]
    for instruction in instructions:
        instruction_code = instruction[0]
        if instruction[0] in instruction_filter:
            parameter = instruction[1:]
            if instruction_code == 's':
                spin_count = int(parameter)
                end_position = (end_position[-spin_count:] +
                                end_position[:-spin_count])
            else:
                if instruction_code == 'x':
                    swap_positions = [int(p)
                                      for p in parameter.split('/')]
                else:
                    swap_positions = [end_position.index(p)
                                      for p in parameter.split('/')]
                (end_position[swap_positions[0]],
                end_position[swap_positions[1]]) = \
                    (end_position[swap_positions[1]],
                    end_position[swap_positions[0]])
    return end_position

puzzle = (2017, 16)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.to_list)

# print(puzzle_input)

# Puzzle solution part 1

num_programs = 16
start_programs = [chr(97 + c) for c in range(num_programs)]

programs = dance(start_programs, puzzle_input)

print('Part 1 Solution: {}'.format(''.join(programs)))

# Puzzle solution part 2


# Note that applying all moves N times is the same as
# applying just the positional moves N times followed by
# applying just the letter swap moves N times.
#
# Note also that repeatedly applying the positional moves
# results in some repeating cycle for each position and that
# repeatedly applying just the letter swap moves also results
# in some repeating cycle for each position.
#
# Create cycle lists for the cyclical moves (s and x)
# and the swap moves (p).
#
# Now for each position, use the two cycle lists and a bit
# of modular arithmetic to work out the final value.

positionals = {q:[q] for q in start_programs}
positionals_done = []
swaps = {r:[r] for r in start_programs}
swaps_done = []

positional_programs = start_programs[:]
swap_programs = start_programs[:]

while len(positionals_done) < num_programs and len(swaps_done) < num_programs:
    positional_programs = dance(positional_programs, puzzle_input, 'sx')
    swap_programs = dance(swap_programs, puzzle_input, 'p')
    for p, q, r in zip(start_programs, positional_programs, swap_programs):
        if p not in positionals_done:
            if p == q:
                positionals_done.append(p)
            else:
                positionals[p].append(q)
        if p not in swaps_done:
            if p == r:
                swaps_done.append(p)
            else:
                swaps[p].append(r)

dances = 1000000000

programs = []

for p in start_programs:
    positional = positionals[p][dances % len(positionals[p])]
    swap = swaps[positional][dances % len(swaps[positional])]
    programs.append(swap)

print('Part 2 Solution: {}'.format(''.join(programs)))
