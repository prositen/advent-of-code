import itertools

from python.src.common import Day, timer, Timer


class Dec01(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 1, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return sorted(
            int(row) for row in instructions
        )

    @timer(part=1)
    def part_1(self):
        for pair in itertools.permutations(self.instructions, 2):
            if sum(pair) == 2020:
                return pair[0] * pair[1]

    @timer(part=2)
    def part_2(self):
        for pair in itertools.permutations(self.instructions, 3):
            if sum(pair) == 2020:
                return pair[0] * pair[1] * pair[2]


if __name__ == '__main__':
    with Timer():
        d = Dec01()
        d.part_1()
        d.part_2()
