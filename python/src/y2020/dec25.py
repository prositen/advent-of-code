from python.src.common import Day, timer, Timer


def find_loop(public_key=None):
    value = 1
    loop = 0
    while value != public_key:
        loop += 1
        value = (value * 7) % 20201227
    return loop


class Dec25(Day, year=2020, day=25):
    def __init__(self, instructions=None, filename=None):
        super().__init__(instructions=instructions, filename=filename)
        self.door, self.card = self.instructions

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_lines(instructions)

    @timer(part=1)
    def part_1(self):
        card_loop = find_loop(public_key=self.card)
        return pow(self.door, card_loop, 20201227)

    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Combo breaker'):
        Dec25().run_day()
