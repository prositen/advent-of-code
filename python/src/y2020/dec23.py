from collections import deque

from python.src.common import Day, timer, Timer, stringify


class CrabCups(object):

    def __init__(self, cups):
        self.cups = deque(cups)
        self.len = len(self.cups)

    def play(self, moves):
        for _ in range(moves):
            current, *pick_up = (self.cups.popleft() for _ in range(4))
            destination = current - 1
            while destination in (*pick_up, 0):
                if destination == 0:
                    destination = self.len
                else:
                    destination -= 1
            destination = self.cups.index(destination)
            for i in range(1, 4):
                self.cups.insert(destination + i, pick_up[i - 1])
            self.cups.append(current)
        i1 = self.cups.index(1)
        self.cups.rotate(-i1)

        return list(self.cups)[1:10]


class Dec23(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 23, instructions, filename)
        self.game = CrabCups(self.instructions)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_digits(instructions=instructions)

    @timer(part=1)
    def part_1(self, moves=100):
        cups = self.game.play(moves)
        return stringify(cups, '')

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        d = Dec23()
        d.part_1()
        d.part_2()
