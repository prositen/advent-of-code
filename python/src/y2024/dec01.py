from collections import Counter

from python.src.common import Day, timer, Timer


class Dec01(Day, year=2024, day=1, title='Historian Hysteria'):

    @classmethod
    def parse_instructions(cls, instructions):
        lines = cls.parse_multiple_ints_per_line(instructions, separator=r'\s+')
        return [line[0] for line in lines], [line[1] for line in lines]

    @timer(part=1)
    def part_1(self):
        sorted_left = sorted(self.instructions[0])
        sorted_right = sorted(self.instructions[1])
        return sum(abs(x - y) for x, y in zip(sorted_left, sorted_right))

    @timer(part=2)
    def part_2(self):
        left = self.instructions[0]
        right = Counter(self.instructions[1])
        return sum(item * right[item] for item in left)


if __name__ == '__main__':
    with Timer('Total'):
        Dec01().run_day()
