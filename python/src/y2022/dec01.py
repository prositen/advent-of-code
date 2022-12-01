from python.src.common import Day, timer, Timer


class Dec01(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2022, 1, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return [
          [int(r) for r in g]
          for g in Day.parse_groups(instructions=instructions)
        ]

    @timer(part=1)
    def part_1(self):
        return max(sum(g) for g in self.instructions)

    @timer(part=2)
    def part_2(self):
        elves = [sum(g) for g in self.instructions]
        return sum(sorted(elves, reverse=True)[:3])


if __name__ == '__main__':
    with Timer('Total'):
        Dec01().run_day()
