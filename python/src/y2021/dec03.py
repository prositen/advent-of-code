from collections import Counter

from python.src.common import Day, timer, Timer


class Dec03(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 3, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return instructions

    @timer(part=1)
    def part_1(self):
        n = len(self.instructions)
        result = Counter()
        for line in self.instructions:
            for i,c in enumerate(line[::-1]):
                result[i] += int(c)
        gamma = 0
        epsilon = 0
        for i,v in result.items():
            if (n-v) < v:
                gamma += 2**i
            else:
                epsilon += 2**i
        print(epsilon, gamma)
        return epsilon * gamma

    @timer(part=2)
    def part_2(self):
        report = [line for line in self.instructions]
        for i in range(self.instructions[0]):
            bits = [line[i] for line in report]


if __name__ == '__main__':
    with Timer('Total'):
        Dec03().run_day()
