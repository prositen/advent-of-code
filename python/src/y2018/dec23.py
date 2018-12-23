import re

from python.src.common import Day


class Dec23(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 23, instructions, filename)
        self.nanobots = [((i[0],i[1],i[2]),i[3]) for i in self.instructions]

    @staticmethod
    def parse_instructions(instructions):
        re_int = re.compile(r'(-?\d+)')
        return [
            list(map(int, re_int.findall(line)))
            for line in instructions
        ]

    def part_1(self):
        strongest = max(self.nanobots, key=lambda nb: nb[1])
        within_radius = [nb for nb in self.nanobots if md(nb[0], strongest[0]) <= strongest[1]]
        return len(within_radius)


def md(p1, p2):
    return sum(abs(x1 - x2) for x1, x2 in zip(p1, p2))


if __name__ == '__main__':
    d = Dec23()
    print('Nanobots in range of the strongest:', d.part_1())
