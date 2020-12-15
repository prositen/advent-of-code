from python.src.common import Day, timer, Timer


class Dec15(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 15, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)

    def play(self, rounds):
        numbers = dict()
        for i, n in enumerate(self.instructions[:-1]):
            numbers[n] = i + 1
        next_number = self.instructions[-1]
        for i in range(len(self.instructions), rounds):
            last_turn = numbers.get(next_number, 0)
            numbers[next_number] = i
            if last_turn:
                next_number = i - last_turn
            else:
                next_number = 0
        return next_number

    @timer(part=1)
    def part_1(self):
        return self.play(rounds=2020)

    @timer(part=2)
    def part_2(self):
        return self.play(rounds=30000000)


if __name__ == '__main__':
    with Timer('Total'):
        d = Dec15()
        d.part_1()
        d.part_2()
