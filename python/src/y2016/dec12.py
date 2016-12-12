import re

from collections import defaultdict


class Assembunny:
    class Instruction:
        def run(self, context):
            pass

    class CpyReg(Instruction):
        def __init__(self, params):
            self.reg_from = params[0]
            self.reg_to = params[1]

        def run(self, context):
            context.registers[self.reg_to] = context.registers[self.reg_from]
            context.pointer += 1

        def __repr__(self):
            return "cpy {0} {1}".format(self.reg_from, self.reg_to)

    class CpyVal(Instruction):
        def __init__(self, params):
            self.value = int(params[0])
            self.reg_to = params[1]

        def run(self, context):
            context.registers[self.reg_to] = self.value
            context.pointer += 1

        def __repr__(self):
            return "cpy {0} {1}".format(self.value, self.reg_to)

    class Inc(Instruction):
        def __init__(self, params):
            self.reg = params[0]

        def run(self, context):
            context.registers[self.reg] += 1
            context.pointer += 1

        def __repr__(self):
            return "inc {0}".format(self.reg)

    class Dec(Instruction):
        def __init__(self, params):
            self.reg = params[0]

        def run(self, context):
            context.registers[self.reg] -= 1
            context.pointer += 1

        def __repr__(self):
            return "dec {0}".format(self.reg)

    class JnzVal(Instruction):
        def __init__(self, params):
            self.val = int(params[0])
            self.steps = int(params[1])

        def run(self, context):
            if self.val != 0:
                context.pointer += self.steps
            else:
                context.pointer += 1

        def __repr__(self):
            return "jnz {0} {1}".format(self.val, self.steps)

    class JnzReg(Instruction):
        def __init__(self, params):
            self.reg = params[0]
            self.steps = int(params[1])

        def run(self, context):
            if context.registers[self.reg] != 0:
                context.pointer += self.steps
            else:
                context.pointer += 1

        def __repr__(self):
            return "jnz {0} {1}".format(self.reg, self.steps)

    instructions = {
        re.compile(r"cpy ([a-z]) (\w)"): CpyReg,
        re.compile(r"cpy (\d+) (\w)"): CpyVal,
        re.compile(r"inc ([a-z])"): Inc,
        re.compile(r"dec ([a-z])"): Dec,
        re.compile(r"jnz (\d+) (-?\d+)"): JnzVal,
        re.compile(r"jnz ([a-z]) (-?\d+)"): JnzReg
    }

    @staticmethod
    def parse(line):
        for regex, clazz in Assembunny.instructions.items():
            result = regex.match(line)
            if result:
                return clazz(result.groups())
        raise BaseException("Parse error", line)


class Computer:
    class Context:
        def __init__(self):
            self.registers = defaultdict(int)
            self.pointer = 0

    def __init__(self, instructions):
        self.instructions = list()
        self.context = self.Context()
        self.parse(instructions)

    def parse(self, instructions):
        for i in instructions:
            self.instructions.append(Assembunny.parse(i))

    def run(self):
        self.context.pointer = 0
        while self.context.pointer < len(self.instructions):
            # self.dump()
            instruction = self.instructions[self.context.pointer]
            instruction.run(self.context)

    def register(self, param):
        return self.context.registers[param]

    def dump(self):
        with open('dump.txt', 'a') as fh:
            print('-' * 50, file=fh)
            print(self.context.registers, file=fh)
            print('-' * 20, file=fh)
            for index, instruction in enumerate(self.instructions):
                print("{0}\t{1}".format("=>" if self.context.pointer == index else "", repr(instruction)), file=fh)

    def reset(self, param):
        self.context.registers = defaultdict(int)
        self.context.registers.update(param)


if __name__ == '__main__':
    with open('../../../data/2016/input.12.txt', 'r') as fh:
        computer = Computer(fh.readlines())
    computer.run()
    print("Register a contains", computer.register('a'))
    computer.reset({'c': 1})
    computer.run()
    print("Register a contains", computer.register('a'))
