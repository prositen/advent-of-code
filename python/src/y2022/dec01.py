from python.src.common import Day, timer, Timer


class Dec01(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2022, 1, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return instructions

    @timer(part=1)
    def part_1(self):
        return 0

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec01().run_day()
