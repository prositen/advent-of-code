from collections import deque

from python.src.common import Day, timer, Timer


class LTRCalculator(object):

    def __init__(self, expression):
        self.memory = deque()
        self.expression = '(' + expression.replace(' ', '') + ')'

    def calculate(self):
        current_number = 0
        operand = 0
        operator = ''
        for char in self.expression:
            if str.isnumeric(char):
                current_number = (current_number * 10) + int(char)
            else:
                if current_number and operator and operand:
                    if operator == '+':
                        current_number += operand
                    elif operator == '*':
                        current_number *= operand
                    operand = 0
                    operator = ''

                if char == '(':
                    self.memory.append((operand, operator))
                    operator = ''
                    operand = 0
                elif char == ')':
                    operand, operator = self.memory.pop()
                elif char in ('+', '*'):
                    operand, current_number = current_number, 0
                    operator = char

        return current_number


class Dec18(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 18, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return instructions

    @timer(part=1)
    def part_1(self):
        return sum(LTRCalculator(line).calculate()
                   for line in self.instructions)

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        d = Dec18()
        d.part_1()
        d.part_2()
