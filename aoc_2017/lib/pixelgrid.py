class PixelGrid:
    """Class for manipulating a grid of pixels as per
       puzzle for day 21."""

    _initial_state = ['.#.', '..#', '###']

    def __init__(self, enhancements):
        """Initialise the pixel grid.

        The list of enhancements will be pre-processed
        to create every symmetrical permutation.

        Args:
            enhancements (list): Original puzzle list.
        """

        self._state = self._initial_state
        self._enhancements = {}

        for enhancement in enhancements:
            enhancement_split = enhancement.split(' => ')
            transformed = enhancement_split[1].split('/')
            identity = tuple(enhancement_split[0].split('/'))

            flip_x = self.__flip_x(identity)
            flip_y = self.__flip_y(identity)
            flip_diag_1 = self.__flip_diag(identity)
            rotate_180 = self.__flip_y(flip_x)
            rotate_anticlockwise = self.__flip_y(flip_diag_1)
            rotate_clockwise = self.__flip_x(flip_diag_1)
            flip_diag_2 = self.__flip_y(rotate_clockwise)

            for pattern in {identity,
                            rotate_clockwise,
                            rotate_anticlockwise,
                            rotate_180,
                            flip_x,
                            flip_y,
                            flip_diag_1,
                            flip_diag_2}:
                self._enhancements[tuple(pattern)] = transformed

    def expand_grid(self):
        """Perform one pass of the pixel expansion algorithm."""
        if len(self._state) % 2 == 0:
            square_size = 2
        else:
            square_size = 3

        output_grid = []

        for sub_grid_y in range(0, len(self._state), square_size):
            for sub_grid_x in range(0, len(self._state), square_size):
                sub_grid = tuple([self._state[sub_grid_y + y]
                            [sub_grid_x:sub_grid_x + square_size]
                            for y in range(square_size)])

                expanded = self._enhancements[sub_grid]

                if sub_grid_x == 0:
                    output_grid.extend(expanded)
                else:
                    expanded_size = len(expanded)
                    for y, row in enumerate(expanded):
                        output_grid[sub_grid_y*
                                    expanded_size//
                                    square_size + y] += row

        self._state = output_grid

    def count_pixels(self):
        """Count the number of lit pixels."""
        return sum([row.count('#') for row in self._state])

    def __str__(self):
        """String representation of current state."""
        return '\n'.join(self._state)

    @staticmethod
    def __flip_diag(grid):
        """Flip a grid along the diagonal."""
        flipped_grid = [list(row) for row in grid]
        for y, row in enumerate(grid):
            for x in range(len(grid)):
                flipped_grid[x][y] = row[x]

        return tuple([''.join(line) for line in flipped_grid])

    @staticmethod
    def __flip_x(grid):
        """Flip a grid horizontally."""
        return tuple([''.join(reversed(part)) for part in grid])

    @staticmethod
    def __flip_y(grid):
        """Flip a grid vertically."""
        return tuple(reversed(grid))
