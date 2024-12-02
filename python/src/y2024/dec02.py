from python.src.common import Day, timer, Timer, sgn


class Dec02(Day, year=2024, day=2, title='Red-Nosed Reports'):

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_multiple_ints_per_line(instructions, separator=r'\s+')

    @staticmethod
    def is_safe(report, part=1):
        d1 = [x - y for x, y in zip(report, report[1:])]
        tolerated_errors = 0 if part==1 else 1

        not_increasing = sum(d <= 0 for d in d1)

        not_decreasing = sum(d >= 0 for d in d1)
        if min(not_increasing, not_decreasing) > tolerated_errors:
            return False
        d3 = [abs(x) for x in d1]
        return max(d3) < 4 and min(d3) > 0

    @timer(part=1)
    def part_1(self):
        return sum(self.is_safe(report)
                for report in self.instructions)


    @timer(part=2)
    def part_2(self):
        return sum(self.is_safe(report, part=2)
                   for report in self.instructions)


if __name__ == '__main__':
    with Timer('Total'):
        Dec02().run_day()
