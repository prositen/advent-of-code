import string

from python.src.common import Day, timer, Timer


class Dec03(Day, year=2022, day=3):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2022, 3, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return instructions

    lookup = ' ' + string.ascii_lowercase + string.ascii_uppercase

    @timer(part=1)
    def part_1(self):
        rucksacks = [(i[:len(i) // 2], i[len(i) // 2:]) for i in self.instructions]
        overlaps = [''.join(set(i[0]).intersection(i[1])) for i in rucksacks]
        return sum(self.lookup.index(c) for group in overlaps for c in group)

    @timer(part=2)
    def part_2(self):
        groups = [
            (self.instructions[i], self.instructions[i + 1], self.instructions[i + 2])
            for i in range(0, len(self.instructions), 3)
        ]
        overlaps = [
            ''.join(set(g[0]).intersection(g[1]).intersection(g[2]))
            for g in groups
        ]
        return sum(self.lookup.index(c) for c in overlaps)


if __name__ == '__main__':
    with Timer():
        Dec03().run_day()
