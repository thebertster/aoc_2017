from aoclib import AOCLib

class CircularList(list):
    """Represents a circular list."""

    def __init__(self, *args):
        """Initialise the circular list.

        Args:
            initial_list (list): An initial individual value or a list.
        """
        list.__init__(self, *args)

    def __getitem__(self, given):
        """Return a circular slice.

        Args:
            given: A slice or single value to return.
        Returns:
            The slice, wrapping as appropriate.
        """

        if isinstance(given, slice):
            start = given.start if given.start else 0
            stop = given.stop if given.stop else start + len(self)
            step = given.step if given.step else 1
            return_slice = [list.__getitem__(self, i % len(self))
                            for i in range(start, stop, step)]
            return return_slice

        return list.__getitem__(self, given)

    def replace(self, start, replacement):
        """Replace part of the list with another list.

        Args:
            start: Index from which to replace.
            replacement: List or value to replace.
        """
        if isinstance(replacement, list):
            for i, element in enumerate(replacement):
                self[(start + i) % len(self)] = element
        else:
            self[start] = replacement

def hash_it_up(lengths,
               hash_size=256,
               rounds=1,
               dense_hash_length=16):
    """Generate the hash using the supplied lengths.

    Args:
        lengths (list): List of lengths.
        hash_size (int): Size of the hash table.
        rounds (int): Number of rounds.
        dense_hash_length (int): Length of the dense hash
    Returns:
        The a tuple of (sparse_hash, dense_hash)
    """

    hash_list = CircularList([i for i in range(hash_size)])

    current_position = 0
    skip_size = 0

    for i in range(rounds):
        for length in lengths:
            if length > 1:
                section = hash_list[current_position:current_position + length]
                section.reverse()
                hash_list.replace(current_position, section)
            current_position = (current_position
                                + length
                                + skip_size) % hash_size
            skip_size += 1

    dense_hash = []

    for dense_start in range(0, hash_size, dense_hash_length):
        dense_hash_part = 0
        for jigger in hash_list[dense_start:dense_start + dense_hash_length]:
            dense_hash_part ^= jigger
        dense_hash.append(dense_hash_part)

    dense_hash_hex = ''

    for hash_byte in dense_hash:
        dense_hash_hex += '{:02x}'.format(hash_byte)

    return hash_list, dense_hash_hex

puzzle = (2017, 10)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1])

# print(puzzle_input)

awful_hash_1 = hash_it_up(AOCLib.to_list_int(puzzle_input))

print('Part 1 Solution: {}'.format(awful_hash_1[0][0]
                                   * awful_hash_1[0][1]))

puzzle_lengths = [ord(character) for character in puzzle_input]
puzzle_lengths.extend([17, 31, 73, 47, 23])

awful_hash_2 = hash_it_up(puzzle_lengths, rounds=64)

print('Part 2 Solution: {}'.format(awful_hash_2[1]))
                                   