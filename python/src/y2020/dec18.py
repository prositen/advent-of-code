from collections import deque

from python.src.common import Day, timer, Timer


class Calculator(object):

    def __init__(self, expression):
        self.expression = self._tokenize(expression)

    PRIO_LTR = {'*': 1, '+': 1}
    PRIO_PLUS = {'+': 2, '*': 1}

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

    def shunting_yard(self, prio):
        operators = deque()
        output = deque()
        for token in self.expression:
            if token.isdigit():
                output.append((int(token), None, None))
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while (op := operators.pop()) != '(':
                    output.append((op,
                                   output.pop(),
                                   output.pop()))
            elif token in '+*':
                while operators:
                    op = operators[-1]
                    if op == '(' or (prio[op] < prio[token]):
                        break
                    output.append((operators.pop(),
                                   output.pop(),
                                   output.pop()))
                operators.append(token)
        while operators:
            output.append((operators.pop(),
                           output.pop(),
                           output.pop()))

        return output.pop()

    def evaluate(self, node):
        (data, l_child, r_child) = node
        if l_child is None:
            return data
        else:
            l_value = self.evaluate(l_child)
            r_value = self.evaluate(r_child)
            if data == '+':
                return l_value + r_value
            else:
                return l_value * r_value

    def calculate(self, prio):
        root = self.shunting_yard(prio)
        return self.evaluate(root)


class Dec18(Day, year=2020, day=18):

    @timer(part=1)
    def part_1(self):
        return sum(Calculator(line).calculate(Calculator.PRIO_LTR)
                   for line in self.instructions)

    @timer(part=2)
    def part_2(self):
        return sum(Calculator(line).calculate(Calculator.PRIO_PLUS)
                   for line in self.instructions)


if __name__ == '__main__':
    with Timer('Operation Order'):
        Dec18().run_day()
