import os
import requests

class AOCLib:
    _aoc_input_url = 'http://adventofcode.com/{year}/day/{day}/input'

    # Initialise and fetch the session authentication cookie from
    # the user profile directory to avoid statically coding it here

    def __init__(self, aoc_year):
        self.aoc_year = aoc_year
        user_profile = os.environ['USERPROFILE']

        with open(user_profile + '\\aoc.cookie', 'r') as aoc_cookie_file:
            aoc_cookie_value = aoc_cookie_file.read()

        self._aoc_cookie = dict(session=aoc_cookie_value)

    # Get the puzzle input from the AOC website and apply
    # an optional transform function to it before returning

    def get_puzzle_input(self, day, transform_function=lambda x: x):
        response = requests.get(
            self._aoc_input_url.format(year=self.aoc_year, day=day),
            cookies=self._aoc_cookie)

        puzzle_input = response.text.rstrip('\n')

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
