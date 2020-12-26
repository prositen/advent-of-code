from collections import defaultdict

from python.src.common import Day, Timer, timer


class Dec10(Day, year=2020, day=10):

    def __init__(self, instructions=None, filename=None):
        super().__init__(instructions=instructions, filename=filename)
        self.adapters = [0] + self.instructions + [self.instructions[-1] + 3]

    @staticmethod
    def parse_instructions(instructions):
        return sorted(
            int(row) for row in instructions
        )

    @timer(part=1)
    def part_1(self):
        diffs = [self.adapters[c] - self.adapters[c - 1] for c in range(1, len(self.adapters))]
        return diffs.count(1) * diffs.count(3)

    @timer(part=2)
    def part_2(self):
        """ Calculate how many possible ways you can reach the adapter
        with joltage X by summing up the ways to reach adapters with
        joltage X-1,2 and 3.
        :return: Number of adapter arrangements
        """
        ways = defaultdict(int)
        for adapter in self.adapters:
            if adapter == 0:
                c = 1
            else:
                c = sum(ways[adapter - x] for x in (1, 2, 3))
            ways[adapter] = c
        return ways[self.adapters[-1]]


if __name__ == '__main__':
    with Timer('Adapter Array'):
        Dec10().run_day()
