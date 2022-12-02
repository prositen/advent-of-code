from python.src.common import Day, timer, Timer


class Dec02(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2022, 2, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return instructions

    SCORES_PART_1 = {
        'A X': 3 + 1,
        'A Y': 6 + 2,
        'A Z': 0 + 3,
        'B X': 0 + 1,
        'B Y': 3 + 2,
        'B Z': 6 + 3,
        'C X': 6 + 1,
        'C Y': 0 + 2,
        'C Z': 3 + 3
    }

    @timer(part=1)
    def part_1(self):
        return sum(self.SCORES_PART_1[s] for s in self.instructions)

    SCORES_PART_2 = {
        'A X': 0 + 3,
        'A Y': 3 + 1,
        'A Z': 6 + 2,
        'B X': 0 + 1,
        'B Y': 3 + 2,
        'B Z': 6 + 3,
        'C X': 0 + 2,
        'C Y': 3 + 3,
        'C Z': 6 + 1
    }

    @timer(part=2)
    def part_2(self):
        return sum(self.SCORES_PART_2[s] for s in self.instructions)


if __name__ == '__main__':
    with Timer('Total'):
        Dec02().run_day()
