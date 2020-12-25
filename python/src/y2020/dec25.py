from python.src.common import Day, timer, Timer


def transform(public_key=None, loop_size=None, subject_number=7):
    value = 1
    loop = 0
    while True:
        loop += 1
        value = (value * subject_number) % 20201227
        if loop_size == loop:
            return value
        elif value == public_key:
            return loop


class Dec25(Day):
    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 25, instructions, filename)
        self.door, self.card = self.instructions

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_lines(instructions)

    @timer(part=1)
    def part_1(self):
        card_loop = transform(public_key=self.card)
        return transform(subject_number=self.door,
                         loop_size=card_loop)

    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec25().run_day()
