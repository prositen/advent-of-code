from functools import cache

from python.src.common import Day, timer, Timer


class Onsen(object):
    def __init__(self, towel_patterns):
        self.towel_patterns = towel_patterns

    @cache
    def count_designs(self, design):
        if not design:
            return 1
        return sum(
            self.count_designs(design[len(pattern):])
            for pattern in self.towel_patterns
            if design.startswith(pattern)
        )


class Dec19(Day, year=2024, day=19, title='Linen Layout'):

    def __init__(self, year=None, day=None, instructions=None, filename=None):
        super().__init__(year, day, instructions, filename)
        self.onsen = Onsen(self.instructions[0])

    @staticmethod
    def parse_instructions(instructions):
        groups = Day.parse_groups(instructions)
        towels = [t.strip() for t in groups[0][0].split(',')]
        return towels, groups[1]

    @timer(part=1)
    def part_1(self):
        return sum(1 if self.onsen.count_designs(pattern) else 0
                   for pattern in self.instructions[1])

    @timer(part=2)
    def part_2(self):
        return sum(self.onsen.count_designs(pattern)
                   for pattern in self.instructions[1])


if __name__ == '__main__':
    with Timer('Total'):
        Dec19().run_day()
