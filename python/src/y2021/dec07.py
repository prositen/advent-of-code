from python.src.common import Day, timer, Timer


class Dec07(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 7, instructions=instructions, filename=filename)
        self.crabs = sorted(self.instructions)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)

    @timer(part=1)
    def part_1(self):
        return min(sum(abs(crab - x) for crab in self.crabs)
                   for x in range(self.crabs[0], self.crabs[-1]))

    @timer(part=2)
    def part_2(self):
        return min(
            sum(
                (steps := abs(crab - x)) * (steps+1) // 2 for crab in self.crabs
            )
            for x in range(self.crabs[0], self.crabs[-1]))


if __name__ == '__main__':
    with Timer('The Treachery of Whales'):
        Dec07().run_day()
