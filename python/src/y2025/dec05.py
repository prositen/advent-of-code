from python.src.common import Day, timer, Timer

def combine_ranges(ranges: list[range]):
    updated_ranges = list()
    non_matching_ranges = list()
    p = ranges[0]
    for r in ranges[1:]:
        if r.start <= p.stop and p.start <= r.stop:
            updated_ranges.append(range(min(r.start, p.start), max(r.stop, p.stop)))
        else:
            non_matching_ranges.append(r)
    if updated_ranges:
        return combine_ranges(updated_ranges + non_matching_ranges)
    elif non_matching_ranges:
        return [p] + combine_ranges(non_matching_ranges)
    else:
        return [p]

class Cafeteria:
    def __init__(self, fresh_ranges: list[range], ingredient_ids):
        ranges = sorted(fresh_ranges, key=lambda r: (r.start, len(r)))
        self.fresh_ranges = combine_ranges(ranges)
        self.ingredient_ids = ingredient_ids

    def count_my_fresh_ingredients(self):
        return sum(
            any(i in r for r in self.fresh_ranges)
            for i in self.ingredient_ids
        )

    def all_fresh_ingredients(self):
        return sum(len(r) for r in self.fresh_ranges)


class Dec05(Day, year=2025, day=5, title='Cafeteria'):

    @staticmethod
    def parse_instructions(instructions):
        fresh_ranges = []
        for n, line in enumerate(instructions):
            if not len(line):
                break
            r = line.split('-')
            fresh_ranges.append(range(int(r[0]), int(r[1]) + 1))
        ingredient_ids = list(map(int, instructions[n + 1:]))
        return fresh_ranges, ingredient_ids

    @timer(part=1)
    def part_1(self):
        c = Cafeteria(self.instructions[0], self.instructions[1])
        return c.count_my_fresh_ingredients()

    @timer(part=2)
    def part_2(self):
        c = Cafeteria(self.instructions[0], self.instructions[1])
        return c.all_fresh_ingredients()


if __name__ == '__main__':
    with Timer('Total'):
        Dec05().run_day()
