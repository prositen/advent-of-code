from python.src.common import Day, timer, Timer


class Dec03(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 3, instructions, filename)
        self.report, self.flipped, self.bit_length = self.instructions

    @staticmethod
    def parse_instructions(instructions):
        bl = len(instructions[0])
        flipped = [
            [int(instructions[x][y]) for x in range(len(instructions))]
            for y in range(bl)
        ]
        return instructions, flipped, bl

    @staticmethod
    def find_most_common(bits):
        s = sum(int(b) for b in bits)
        return (len(bits) - s) <= s

    @timer(part=1)
    def part_1(self):
        gamma, epsilon = 0, 0
        for index, line in enumerate(self.flipped[::-1]):
            if self.find_most_common(line):
                gamma += 2 ** index
            else:
                epsilon += 2 ** index

        return epsilon * gamma

    def filter_report(self, report, bit_position, method):
        bits = [report[i][bit_position] for i in range(len(report))]
        most_common = int(self.find_most_common(bits))
        if not method:
            most_common = 1-most_common

        return [
            line for line in report if int(line[bit_position]) == most_common
        ]

    @timer(part=2)
    def part_2(self):
        result = list()
        for method in (True, False):
            report = [line for line in self.report]

            for n in range(self.bit_length):
                report = self.filter_report(report, n, method)
                if len(report) == 1:
                    result.append(int(report[0], 2))

        return result[0] * result[1]


if __name__ == '__main__':
    with Timer('Total'):
        Dec03().run_day()
