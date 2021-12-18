import json
from collections import deque

from python.src.common import Day, timer, Timer


class SnailFish(object):

    def __init__(self, left, right, level):
        self.left = left
        self.right = right
        self.level = level

    @staticmethod
    def from_string(sf_string):
        return SnailFish.from_list(json.loads(sf_string))

    @staticmethod
    def from_list(sf_list, level=0):
        left, right = sf_list
        if isinstance(left, list):
            left = SnailFish.from_list(left, level + 1)
        if isinstance(right, list):
            right = SnailFish.from_list(right, level + 1)
        return SnailFish(left, right, level)

    def __str__(self):
        left = str(self.left)
        right = str(self.right)
        return f'[{left},{right}]'

    def explode(self):
        if self.level == 4:
            return self.left, self.right, True
        else:
            if isinstance(self.left, SnailFish):
                left, right, exploded = self.left.explode()


class Dec18(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 18, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return [
            SnailFish.from_string(row) for row in instructions
        ]

    @timer(part=1)
    def part_1(self):
        return 1

    @timer(part=2)
    def part_2(self):
        return 2


if __name__ == '__main__':
    with Timer():
        Dec18().run_day()
