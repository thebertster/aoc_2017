from lib.aoclib import AOCLib

class Registers(dict):
    """Registers class.

    Works like a dict with a default value of 0,
    but only for keys that start with an alpha character.

    Accessing a key that does not start with an alpha returns
    an integer representation of the key.
    """

    def __getitem__(self, key):
        if key[0].isalpha():
            if key in self:
                return super().__getitem__(key)
            return 0

        return int(key)

def process_instruction(program_id,
                        instruction,
                        registers,
                        queues):
    """Process an instruction.

    Args:
        program_id (int): The program ID (0 or 1).
        instruction (list): The instruction to process.
        registers (dict): The registers for this program.
        queues (list): The inter-process queues.
    """

    pc_inc = 0

    if instruction[0] == 'snd':
        queues[1 - program_id].append(registers[instruction[1]])
        if program_id == 1:
            registers['part2'] += 1
    elif instruction[0] == 'set':
        registers[instruction[1]] = registers[instruction[2]]
    elif instruction[0] == 'add':
        registers[instruction[1]] += registers[instruction[2]]
    elif instruction[0] == 'mul':
        registers[instruction[1]] *= registers[instruction[2]]
    elif instruction[0] == 'mod':
        registers[instruction[1]] %= registers[instruction[2]]
    elif instruction[0] == 'rcv':
        if queues[program_id]:
            registers[instruction[1]] = queues[program_id][0]
            if 'part1' not in registers and program_id == 0:
                registers['part1'] = queues[0][0]
            queues[program_id] = queues[program_id][1:]
        else:
            pc_inc = -1
    elif instruction[0] == 'jgz':
        if registers[instruction[1]] > 0:
            pc_inc = (registers[instruction[2]] - 1)

    return pc_inc + 1

puzzle = (2017, 18)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list)

# print(puzzle_input)

# Puzzle solution parts 1 and 2

program_length = len(puzzle_input)
program = [instruction.split(' ') for instruction in puzzle_input]

registers_0 = Registers({'p': 0})
registers_1 = Registers({'p': 1, 'part2': 0})
program_queues = [[], []]
pc = [0, 0]

while True:
    pc_inc_0 = process_instruction(0, program[pc[0]],
                                   registers_0,
                                   program_queues)
    pc_inc_1 = process_instruction(1, program[pc[1]],
                                   registers_1,
                                   program_queues)
    pc[0] += pc_inc_0
    pc[1] += pc_inc_1

    if (pc[0] < 0 or pc[0] >= program_length
        or pc[1] < 0 or pc[1] >= program_length
        or (pc_inc_0 == pc_inc_1 == 0)):
        break

aoc.print_solution(1, registers_0['part1'])
aoc.print_solution(2, registers_1['part2'])
