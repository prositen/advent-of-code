from python.src.common import Day, timer, Timer

class Cafeteria:
    def __init__(self, fresh_ranges, ingredient_ids):
        self.fresh_ranges = fresh_ranges
        self.ingredient_ids = ingredient_ids

    def fresh_count(self):
        return sum(
            any(i in r for r in self.fresh_ranges)
            for i in self.ingredient_ids
        )
class Dec05(Day, year=2025, day=5, 'Cafeteria'):

    @staticmethod
    def parse_instructions(instructions):
        fresh_ranges = []
        for n, line in enumerate(instructions):
            if not len(line):
                break
            r = line.split('-')
            fresh_ranges.append(range(int(r[0]), int(r[1]) + 1))
        ingredient_ids = list(map(int, instructions[n+1:]))
        return fresh_ranges, ingredient_ids

    @timer(part=1)
    def part_1(self):
        c = Cafeteria(self.instructions[0], self.instructions[1])
        return c.fresh_count()

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec05().run_day()
