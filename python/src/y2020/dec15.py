from python.src.common import Day, timer, Timer


class Dec15(Day, year=2020, day=15):

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)

    def play(self, rounds):
        numbers = dict()
        turn = 1
        for n in self.instructions:
            numbers[n] = turn
            turn += 1
        next_number = self.instructions[-1]
        for turn in range(turn - 1, rounds):
            last_turn = numbers.get(next_number, 0)
            numbers[next_number] = turn
            if last_turn:
                next_number = turn - last_turn
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
    with Timer('Rambunctious Recitation'):
        Dec15().run_day()
