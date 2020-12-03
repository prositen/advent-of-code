from math import prod

from python.src.common import Day, timer


class Dec03(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 3, instructions, filename)
        self.pos = (0, 0)
        self.height = len(self.instructions)
        self.width = len(self.instructions[0])

    @staticmethod
    def parse_instructions(instructions):
        return [
            r.strip() for r in instructions
        ]

    @timer(part=1)
    def part_1(self):
        return self.try_slope(3, 1)

    def try_slope(self, x, y):
        tree_count = 0
        self.pos = (0, 0)
        while self.pos[1] < self.height:
            row = self.instructions[self.pos[1]]
            tree_count += row[self.pos[0] % self.width] == '#'
            self.pos = self.pos[0] + x, self.pos[1] + y
        return tree_count

    @timer(part=2)
    def part_2(self):
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        return prod(self.try_slope(*s) for s in slopes)


if __name__ == '__main__':
    d = Dec03()
    d.part_1()
    d.part_2()
