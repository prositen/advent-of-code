import functools
import itertools
import math
import operator
from collections import deque

from python.src.common import Day, timer, Timer


class Calibrator(object):
    operators = (operator.mul, operator.add)

    def __init__(self, result, operands):
        self.result = result
        self.operands = operands

    def calculate(self):
        """
        Just because you can doesn't mean that you should
        :return:
        """
        for attempt in itertools.product(
                self.operators, repeat=len(self.operands) - 1):
            if self.result == functools.reduce(
                    lambda x, y: y[1](x, y[0]),
                    itertools.zip_longest(self.operands[1:], attempt),
                    self.operands[0]
            ):
                return self.result
        return 0

    def get_value(self):
        todo = deque([(self.operands[0], 1)])
        _len = len(self.operands) - 1
        while todo:
            result, index = todo.popleft()

            for op in self.operators:
                r_op = op(result, self.operands[index])
                if index == _len:
                    if r_op == self.result:
                        return self.result
                elif r_op > self.result:
                    continue
                elif index < _len:
                    todo.append((r_op, index + 1))
        return 0


class Concatenator(Calibrator):
    operators = (lambda x, y: y + x * 10 ** int(math.log10(y) + 1),
                 operator.mul,
                 operator.add)


class Dec07(Day, year=2024, day=7, title='Bridge Repair'):

    @staticmethod
    def parse_instructions(instructions):
        result = list()
        for instruction in instructions:
            first, second = instruction.split(': ')
            result.append((int(first), Day.parse_int_line([second], separator=' ')))
        return result

    @timer(part=1)
    def part_1(self):
        return sum(Calibrator(*i).get_value() for i in self.instructions)

    @timer(part=2)
    def part_2(self):
        return sum((Calibrator(*i).get_value() or Concatenator(*i).get_value()) for i in
                   self.instructions)


if __name__ == '__main__':
    with Timer('Total'):
        Dec07().run_day()
