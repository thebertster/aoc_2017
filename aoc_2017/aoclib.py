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

    def get_puzzle_input(self, day):
        response = requests.get(
            self._aoc_input_url.format(year=self.aoc_year, day=day),
            cookies=self._aoc_cookie)
        return response.text
