from lib.circularlist import CircularList

class KnotHash:
    @staticmethod
    def get_hash(hash_input,
               hash_size=256,
               rounds=1,
               dense_hash_length=16):
        """Generate the hash using the supplied lengths.

        Args:
            hash_input (list or string): Input to the hash function.
            hash_size (int): Size of the hash table.
            rounds (int): Number of rounds.
            dense_hash_length (int): Length of the dense hash
        Returns:
            A tuple of (sparse_hash, dense_hash)
        """

        if isinstance(hash_input, str):
            hash_input = [ord(hash_char) for hash_char in hash_input]
            hash_input.extend([17, 31, 73, 47, 23])

        hash_list = CircularList([i for i in range(hash_size)])

        current_position = 0
        skip_size = 0

        for i in range(rounds):
            for hash_element in hash_input:
                if hash_element > 1:
                    section = hash_list[current_position + hash_element - 1:
                                        current_position - 1:
                                        -1]
                    hash_list.replace(current_position, section)
                current_position = (current_position
                                    + hash_element
                                    + skip_size) % hash_size
                skip_size += 1

        dense_hash = []

        for dense_start in range(0, hash_size, dense_hash_length):
            dense_hash_part = 0
            for jigger in hash_list[dense_start:dense_start
                                    + dense_hash_length]:
                dense_hash_part ^= jigger
            dense_hash.append(dense_hash_part)

        dense_hash_hex = ''

        for hash_byte in dense_hash:
            dense_hash_hex += '{:02x}'.format(hash_byte)

        return hash_list, dense_hash_hex
