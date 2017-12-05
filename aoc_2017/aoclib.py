import os
import requests

class AOCLib:
    _aoc_input_url = 'http://adventofcode.com/{year}/day/{day}/input'

    # Initialise and fetch the session authentication cookie from
    # the user profile directory to avoid statically coding it here

    def __init__(self, aoc_year):
        self.aoc_year = aoc_year
        user_profile = os.environ['USERPROFILE']
        self.aoc_path = '{}\\aoc'.format(user_profile)

        with open('{}\\aoc.cookie'.format(self.aoc_path),
                  'r') as aoc_cookie_file:
            aoc_cookie_value = aoc_cookie_file.read()

        self._aoc_cookie = dict(session=aoc_cookie_value)

    # Get the puzzle input from the AOC website and apply
    # an optional transform function to it before returning
    # Cache the puzzle input locally for next time

    def get_puzzle_input(self, day, transform_function=lambda x: x):
        cache_filename = '{}\\{}_{}.txt'.format(self.aoc_path,
                                                self.aoc_year, day)

        try:
            with open(cache_filename, 'r') as cache_file:
                puzzle_input = cache_file.read()
        except FileNotFoundError:
            puzzle_input = None

        if puzzle_input is None:
            response = requests.get(
                self._aoc_input_url.format(year=self.aoc_year, day=day),
                cookies=self._aoc_cookie)

            if response.status_code != 200:
                raise AssertionError('Unable to obtain puzzle input!')

            puzzle_input = response.text.rstrip('\n')

            with open(cache_filename, 'w') as cache_file:
                cache_file.write(puzzle_input)

        return transform_function(puzzle_input)

    # Various static methods for manipulating the puzzle input:

    # Transform a comma-separated string to a list

    @staticmethod
    def to_list(puzzle_input):
        return [element.strip() for element in puzzle_input.split(',')]

    # Transform multi-line input to a list

    @staticmethod
    def lines_to_list(puzzle_input):
        return puzzle_input.split('\n')

    @staticmethod
    def lines_to_list_int(puzzle_input):
        return [int(x) for x in puzzle_input.split('\n')]

    # Transform a sequence of digits to a list of integers

    @staticmethod
    def sequence_to_int(puzzle_input):
        return [int(digit) for digit in puzzle_input]
