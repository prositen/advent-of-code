from python.src.common import Day, Timer, timer


class Dec10(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 10, instructions, filename)
        self.adapters = [0] + self.instructions + [self.instructions[-1]+3]

    @staticmethod
    def parse_instructions(instructions):
        return sorted(
            int(row) for row in instructions
        )

    @timer(part=1)
    def part_1(self):
        diffs = [self.adapters[c] - self.adapters[c-1] for c in range(1, len(self.adapters))]
        return diffs.count(1)  * diffs.count(3)

    @timer(part=2)
    def part_2(self):
        return 2


if __name__ == '__main__':
    with Timer():
        d = Dec10()
        print("Part 1: ", d.part_1())
        print("Part 2: ", d.part_2())
