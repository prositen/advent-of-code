from typing import List

from python.src.common import Day, timer, Timer


class ReportChecker(object):

    def __init__(self, values: List[int]):
        self.values = values
        self.deltas = [x - y for x, y in zip(values, values[1:])]

    def all_increasing(self):
        return all(d < 0 for d in self.deltas)

    def all_decreasing(self):
        return all(d > 0 for d in self.deltas)

    def gradual_slope(self):
        slopes = [abs(v) for v in self.deltas]
        return max(slopes) < 4 and min(slopes) > 0

    def is_safe(self):
        return (self.all_increasing() or self.all_decreasing()) and self.gradual_slope()

    def can_be_made_safe(self):
        for i in range(len(self.values)):
            levels = self.values[:i] + self.values[i+1:]
            if ReportChecker(levels).is_safe():
                return True
        return False


class Dec02(Day, year=2024, day=2, title='Red-Nosed Reports'):

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_multiple_ints_per_line(instructions, separator=r'\s+')

    @timer(part=1)
    def part_1(self):
        return sum(ReportChecker(report).is_safe()
                   for report in self.instructions)

    @timer(part=2)
    def part_2(self):
        safe_reports = 0
        for report in self.instructions:
            rc = ReportChecker(report)
            if rc.is_safe() or rc.can_be_made_safe():
                safe_reports += 1
        return safe_reports


if __name__ == '__main__':
    with Timer('Total'):
        Dec02().run_day()
