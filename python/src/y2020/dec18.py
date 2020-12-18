from collections import deque

from python.src.common import Day, timer, Timer


class LTRCalculator(object):

    def __init__(self, expression):
        self.expression = self._tokenize(expression)
        self.ast = self.calc_ast()

    def _tokenize(self, expression):
        prev_char = ''
        stack = deque()
        for char in expression:
            if char.isdigit() and prev_char.isdigit():
                stack.append(stack.pop() + char)
            elif char != ' ':
                stack.append(char)
            prev_char = char
        return stack

    def calc_ast(self):
        stack = deque()
        for token in self.expression:
            if token.isdigit():
                stack.append(int(token))
            elif token == ')':
                right = stack.pop()
                op = stack.pop()
                left = stack.pop()
                if op == '+':
                    stack.append(left + right)
                else:
                    stack.append(left * right)
            elif token in ('+', '*'):
                stack.append(token)
        return stack


    def calculate(self):
        print(self.ast)
        current_number = 0
        operand = 0
        operator = ''
        memory = deque()
        for token in self.expression:
            if current_number and operator and operand:
                if operator == '+':
                    current_number += operand
                elif operator == '*':
                    current_number *= operand
                operand = 0
                operator = ''

            if token == '(':
                memory.append((operand, operator))
                operator = ''
                operand = 0
            elif token == ')':
                operand, operator = memory.pop()
            elif token in ('+', '*'):
                operand, current_number = current_number, 0
                operator = token
            else:
                current_number = int(token)

        if current_number and operator and operand:
            if operator == '+':
                current_number += operand
            elif operator == '*':
                current_number *= operand
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
