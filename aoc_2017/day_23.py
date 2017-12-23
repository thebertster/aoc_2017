from lib.aoclib import AOCLib
from lib.registers import Registers

def process_instruction(instruction, registers):
    """Process an instruction.

    Args:
        instruction (list): The instruction to process.
        registers (dict): The registers for this program.
        queues (list): The inter-process queues.
    """

    pc_inc = 0

    if instruction[0] == 'set':
        registers[instruction[1]] = registers[instruction[2]]
    elif instruction[0] == 'sub':
        registers[instruction[1]] -= registers[instruction[2]]
    elif instruction[0] == 'mul':
        registers[instruction[1]] *= registers[instruction[2]]
    elif instruction[0] == 'jnz':
        if registers[instruction[1]]:
            pc_inc = (registers[instruction[2]] - 1)

    return pc_inc + 1

puzzle = (2017, 23)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list)

# print(puzzle_input)

# Puzzle solution part 1

program_length = len(puzzle_input)
program = [instruction.split(' ') for instruction in puzzle_input]

program_registers = Registers()
pc = 0
mul_count = 0

while True:
    if program[pc][0] == 'mul':
        mul_count += 1

    pc += process_instruction(program[pc],
                              program_registers)

    if pc < 0 or pc >= program_length:
        break

aoc.print_solution(1, mul_count)

# Puzzle solution part 2

# It's a debugging problem!

program_registers = Registers({'a':1})
pc = 0

while True:
    print(program_registers)
    print('{}: {}'.format(pc, ' '.join(program[pc])))
    print()

    while True:
        debug_command = input('r, p, b or ENTER?')
        if debug_command == '':
            break
        elif debug_command == 'r':
            while True:
                r = input('Register?')
                if r == '':
                    break
                v = input('Value for {}?'.format(r))
                program_registers[r] = program_registers[v]
                print(program_registers)
                print()
        elif debug_command == 'p':
            p = input('PC?')
            if p != '':
                pc = int(p)
                print('{}: {}'.format(pc, ' '.join(program[pc])))
                print()
        elif debug_command == 'b':
            pc = -1
            break

    if pc == -1:
        break

    pc += process_instruction(program[pc],
                              program_registers)

    if pc < 0 or pc >= program_length:
        break

# After a bit of debugging, we can work out what the program is doing.
#
# The program counts the number of non-primes in the sequence
# 106700, 106717, 106734, ... , 123700
#
# Let's just do a lazy primality test - won't take too long to run!
# No need for Miller-Rabin here!!

non_primes = 0

for test in range(106700, 123701, 17):
    prime = True
    for i in range(2, test//2 + 1):
        if (test % i) == 0:
            prime = False
            break
    if not prime:
        non_primes += 1

aoc.print_solution(2, non_primes)
