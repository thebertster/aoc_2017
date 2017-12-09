from aoclib import AOCLib

puzzle = (2017, 9)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1])

# print(puzzle_input)

# Puzzle solution part 1 & 2

# As a by-product, also getting the cleaned stream
# and the positions of all the groups - expected
# part 2 to be more complicated!

inside_garbage = False
garbage_count = 0
skip_next = False
group_positions = []
unclosed_positions = []

clean_stream = ''

score = 0

for i, c in enumerate(puzzle_input):
    if skip_next:
        skip_next = False
    else:
        if c == '!':
            skip_next = True
        elif inside_garbage:
            if c == '>':
                inside_garbage = False
            else:
                garbage_count += 1
        elif c == '<':
            inside_garbage = True
        else:
            if c == '{':
                unclosed_positions.append(i)
            elif c == '}':
                nesting_level = len(unclosed_positions)
                group_start = unclosed_positions.pop()
                group_positions.append((group_start, i, nesting_level))
                score += nesting_level
            clean_stream += c

print('Part 1 Solution: {}'.format(score))
print('Part 2 Solution: {}'.format(garbage_count))
