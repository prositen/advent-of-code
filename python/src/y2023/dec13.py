from python.src.common import Day, timer, Timer


class MirrorValley(object):
    def __init__(self, patterns, smudge=0):
        self.rows = patterns
        self.columns = [''.join(z) for z in zip(*patterns)]
        self.smudge = smudge

    @classmethod
    def compare_mirrors(cls, left, right):
        return sum(l != r for l, r in zip(left, right))

    def pattern_mirror(self, pattern):
        for i in range(len(pattern) - 1):
            compare_lists = tuple(zip(pattern[:i + 1][::-1], pattern[i + 1:]))
            if self.smudge == sum(self.compare_mirrors(left, right)
                                  for left, right in compare_lists):
                return i + 1
        return 0

    def find_mirrors(self):
        if rows := self.pattern_mirror(self.rows):
            return 100 * rows
        else:
            return self.pattern_mirror(self.columns)


class Dec13(Day, year=2023, day=13):

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_groups(instructions)

    @timer(part=1)
    def part_1(self):
        return sum(MirrorValley(group).find_mirrors()
                   for group in self.instructions)

    @timer(part=2)
    def part_2(self):
        return sum(MirrorValley(group, smudge=1).find_mirrors()
                   for group in self.instructions)


if __name__ == '__main__':
    with Timer('Total'):
        Dec13().run_day()
