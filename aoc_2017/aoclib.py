import os
import requests

class AOCLib:
    _aoc_input_url = 'http://adventofcode.com/{year}/day/{day}/input'

    def __init__(self, aoc_year):
        self.aoc_year = aoc_year
        user_profile = os.environ['USERPROFILE']

        with open(user_profile + '\\aoc.cookie', 'r') as aoc_cookie_file:
            aoc_cookie_value = aoc_cookie_file.read()

        self._aoc_cookie = dict(session=aoc_cookie_value)

    def get_puzzle_input(self, day, parse_function=lambda x: x):
        response = requests.get(
            self._aoc_input_url.format(year=self.aoc_year, day=day),
            cookies=self._aoc_cookie)

        puzzle_input = response.text.rstrip('\n')

        return parse_function(puzzle_input)

    @staticmethod
    def to_list(puzzle_input):
        return [element.strip() for element in puzzle_input.split(',')]

    @staticmethod
    def lines_to_list(puzzle_input):
        return puzzle_input.split('\n')
