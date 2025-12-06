import functools
import operator

from python.src.common import Day, timer, Timer


class Worksheet:
    def __init__(self, numbers, operators):
        _numbers = [[int(c) for c in line.split()] for line in numbers]
        # Transpose the number columns to rows
        self.operands = [[row[i] for row in _numbers] for i in range(len(_numbers[0]))]

        self.operators = operators

    def grand_total(self):
        return sum(
            functools.reduce(self.operators[i], self.operands[i])
            for i in range(len(self.operands))
        )


class CephalopodWorksheet(Worksheet):

    def __init__(self, numbers, operators):
        super().__init__(numbers, operators)
        # Transpose the entire input (sans the operands)
        data = [[row[i] for row in numbers] for i in range(len(numbers[0]))][::-1]
        self.operands = []
        current_group = []
        for row in data:
            number = ''.join(row).strip()
            if number:
                current_group.append(int(number))
            else:
                self.operands.append(current_group)
                current_group = []
        self.operands.append(current_group)

        self.operators = self.operators[::-1]


class Dec06(Day, year=2025, day=6, title='Trash Compactor'):

    @staticmethod
    def parse_instructions(instructions):
        numbers = instructions[:-1]
        operators = [
            operator.add if c == '+' else operator.mul for c in instructions[-1].split()
        ]
        return numbers, operators

    @timer(part=1)
    def part_1(self):
        return Worksheet(self.instructions[0], self.instructions[1]).grand_total()

    @timer(part=2)
    def part_2(self):
        return CephalopodWorksheet(self.instructions[0], self.instructions[1]).grand_total()


if __name__ == '__main__':
    with Timer('Total'):
        Dec06().run_day()
