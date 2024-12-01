from python.src.common import Day, timer, Timer


class Dec09(Day, year=2023, day=9):

    @staticmethod
    def parse_instructions(instructions):
        return [
            list(map(int, line.split())) for line in instructions
        ]

    @staticmethod
    def extrapolate(numbers, forwards=True):
        if all(n == 0 for n in numbers):
            return 0
        else:
            next_numbers = [j - i for i, j in zip(numbers, numbers[1:])]
            if forwards:
                next_value = numbers[-1] + Dec09.extrapolate(next_numbers, forwards=forwards)
            else:
                next_value = numbers[0] - Dec09.extrapolate(next_numbers, forwards=forwards)
            return next_value

    @timer(part=1)
    def part_1(self):
        return sum(self.extrapolate(series) for series in self.instructions)

    @timer(part=2)
    def part_2(self):
        return sum(self.extrapolate(series, forwards=False) for series in self.instructions)


if __name__ == '__main__':
    with Timer('Total'):
        Dec09().run_day()
