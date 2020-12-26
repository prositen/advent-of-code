from python.src.common import Day, timer, Timer


class Dec09(Day, year=2020, day=9):

    def __init__(self, instructions=None, filename=None):
        super().__init__(instructions=instructions, filename=filename)
        self.weakness = 0

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_lines(instructions)

    def find_invalid_number(self, preamble=25):
        sums = list()
        for i, num in enumerate(self.instructions):
            if i > preamble:
                if num not in sums:
                    return num
                sums = sums[preamble:]
            new_sums = [(num + n) for n in self.instructions[i:preamble + i]]
            sums += new_sums

    def find_encryption_weakness(self, weakness):
        sums = dict()
        for i, num in enumerate(self.instructions):
            for k, v in list(sums.items()):
                v += num
                if v == weakness:
                    mi = min(self.instructions[k:i])
                    ma = max(self.instructions[k:i])
                    return mi, ma
                elif v > weakness:
                    del sums[k]
                else:
                    sums[k] = v

            sums[i] = num

    @timer(part=1)
    def part_1(self):
        self.weakness = self.find_invalid_number(preamble=25)
        return self.weakness

    @timer(part=2)
    def part_2(self):
        return sum(self.find_encryption_weakness(self.weakness))


if __name__ == '__main__':
    with Timer('Encoding Error'):
        Dec09().run_day()
