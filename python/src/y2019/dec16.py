import itertools

from python.src.common import Day


class Dec16(Day):
    def __init__(self, filename=None, instructions=None):
        super().__init__(2019, 16, filename=filename, instructions=instructions)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_digits(instructions)

    @staticmethod
    def apply_pattern(inputs, patterns):
        return [a * b for a, b in zip(inputs, itertools.cycle(patterns))]

    def phase(self, phases=1):
        base_pattern = [0, 1, 0, -1]
        r = [0] + [c for c in self.instructions]
        result = []

        for _ in range(phases):
            result = []
            for i in range(len(self.instructions)):
                pattern = [c for elem in base_pattern for c in itertools.repeat(elem, i + 1)]
                values = self.apply_pattern(r, pattern)
                result.append(abs(sum(values)) % 10)
            r = [0] + result
        return ''.join(str(c) for c in result)[:8]

    def part_1(self):
        return self.phase(100)

    def part_2(self):
        offset = int(''.join(str(c) for c in self.instructions[:7]))
        r = (self.instructions * 10000)[offset:]
        return self.phase_2(r)

    def phase_2(self, r):
        # The second half of the input don't depend
        # on the first half of the input.
        # The pattern will always be
        # [0,0,0,.... ,1,1,1,1,1]
        for _ in range(100):
            result = []
            t = 0
            for c in r[::-1]:
                t += c
                result.append(t % 10)
            r = result[::-1]
        return ''.join(str(c) for c in r[:8])


if __name__ == '__main__':
    day = Dec16()
    print("Part 1:", day.part_1())
    print("Part 2:", day.part_2())
