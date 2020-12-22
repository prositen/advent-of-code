import functools
from collections import deque

from python.src.common import Day, timer, Timer


class Combat(object):
    def __init__(self, my_cards, their_cards, recursive=False):
        self.my_cards = my_cards
        self.their_cards = their_cards
        self.recursive = recursive

    def play(self):
        while self.my_cards and self.their_cards:
            my = self.my_cards.popleft()
            their = self.their_cards.popleft()
            if my > their:
                self.my_cards.extend([my, their])
            else:
                self.their_cards.extend([their, my])
        if self.my_cards:
            return self.score(self.my_cards)
        else:
            return self.score(self.their_cards)

    def score(self, deck):
        return functools.reduce(lambda a, b: a + ((1 + b[0]) * b[1]),
                                enumerate(reversed(deck)),
                                0)


class Dec22(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 22, instructions, filename)
        self.my_cards, self.their_cards = self.instructions

    @staticmethod
    def parse_instructions(instructions):
        g1, g2 = Day.parse_groups(instructions=instructions)
        return deque(map(int, g1[1:])), deque(map(int, g2[1:]))

    @timer(part=1)
    def part_1(self):
        return Combat(self.my_cards, self.their_cards).play()

    @timer(part=2)
    def part_2(self):
        return 2


if __name__ == '__main__':
    with Timer():
        Dec22().run_day()
