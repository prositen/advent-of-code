import os
from python.src.y2017.common import DATA_DIR


class Instruction(object):

    def __init__(self, line):
        words = line.split()
        self.instr = words[0]
        self.x = words[1]
        self.y = words[2]

    def run(self, context):
        if self.instr == 'set':
            context.set(self.x, context.get(self.y))
        elif self.instr == 'sub':
            context.set(self.x, context.get(self.x) - context.get(self.y))
        elif self.instr == 'mul':
            context.count()
            context.set(self.x, context.get(self.x) * context.get(self.y))
        elif self.instr == 'jnz':
            if context.get(self.x) != 0:
                context.jump(context.get(self.y))
            else:
                context.jump(1)


class Context(object):

    def __init__(self, puzzle_input):
        self.registers = dict(a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0)
        self.pc = 0
        self.instructions = [Instruction(line) for line in puzzle_input]
        self.part1 = 0

    def run(self):
        while 0 <= self.pc < len(self.instructions):
            self.instructions[self.pc].run(self)

    def set(self, reg, value):
        self.registers[reg] = int(value)
        self.pc += 1

    def get(self, reg_or_value):
        v = self.registers.get(reg_or_value, None)
        if v is None:
            v = int(reg_or_value)
        return v

    def jump(self, value):
        self.pc += value

    def count(self):
        self.part1 += 1

    @staticmethod
    def part2():
        h = 0
        for b in range(109300, 126300 + 1, 17):
            for d in range(2, b):
                if b % d == 0:
                    h += 1
                    break
        return h


def main():
    with open(os.path.join(DATA_DIR, 'input.23.txt')) as fh:
        puzzle_input = fh.readlines()

    c = Context(puzzle_input)
    c.run()

    print("Part 1:", c.part1)
    print("Part 2:", c.part2())


if __name__ == '__main__':
    main()
