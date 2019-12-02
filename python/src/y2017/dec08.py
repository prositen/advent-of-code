import os
from collections import defaultdict
import operator

from python.src.y2017.common import DATA_DIR


class Instruction(object):
    def __init__(self, line):
        words = line.split()
        self.reg = words[0]
        self.instruction = words[1]
        self.value = int(words[2])
        self.if_reg = words[4]
        self.if_instr = self.OPERATOR.get(words[5])
        self.if_value = int(words[6])

    OPERATOR = {
        '<': operator.lt,
        '<=': operator.le,
        '==': operator.eq,
        '>': operator.gt,
        '>=': operator.ge,
        '!=': operator.ne
    }

    def __str__(self):
        return "{} {} {} if {} {} {}".format(self.reg, self.instruction,
                                             self.value, self.if_reg, self.if_instr,
                                             self.if_value)

    def run(self, context):
        lookup_reg = context.get(self.if_reg)
        if self.test(lookup_reg):
            self.apply(context)

    def test(self, reg):
        return self.if_instr(reg, self.if_value)

    def apply(self, context):
        if self.instruction == 'inc':
            context.increase(self.reg, self.value)
        elif self.instruction == 'dec':
            context.decrease(self.reg, self.value)


class Context(object):
    def __init__(self, instructions):
        self.registers = defaultdict(int)
        self.program = [Instruction(line) for line in instructions]
        self.all_time_max = 0

    def get(self, reg):
        return self.registers.get(reg, 0)

    def increase(self, reg, value):
        self.registers[reg] += value

    def decrease(self, reg, value):
        self.registers[reg] -= value

    def reset(self):
        self.registers = defaultdict(int)

    def run(self):
        for i in self.program:
            i.run(self)
            self.all_time_max = max(self.max(), self.all_time_max)

    def max(self):
        if len(self.registers):
            return max(self.registers.values())
        return 0

    def pp(self):
        for n, v in self.registers.items():
            print("{} = {}".format(n, v))
        print('---')


def main():
    with open(os.path.join(DATA_DIR, 'input.8.txt')) as fh:
        puzzle_input = fh.readlines()

    context = Context(puzzle_input)
    context.run()
    print("Max value after program run:", context.max())
    print("All time max:", context.all_time_max)


if __name__ == '__main__':
    main()
