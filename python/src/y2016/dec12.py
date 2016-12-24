import re

from collections import defaultdict


class Assembunny(object):
    class Instruction:
        def __init__(self, params):
            self.params = params

        def run(self, context):
            pass

        @staticmethod
        def int_value(param, context):
            return context.registers[param] if param.isalpha() else int(param)

    class OneArgInstruction(Instruction):
        def __init__(self, params):
            super().__init__(params)

    class TwoArgInstruction(Instruction):
        def __init__(self, params):
            super().__init__(params)

    class Cpy(TwoArgInstruction):

        def __init__(self, params):
            super().__init__(params)
            self.cpy_from = params[0]
            self.cpy_to = params[1]

        def run(self, context):
            val = self.int_value(self.cpy_from, context)
            context.registers[self.cpy_to] = val
            context.pointer += 1

        def __repr__(self):
            return "cpy {0} {1}".format(self.cpy_from, self.cpy_to)

    class Inc(OneArgInstruction):
        def __init__(self, params):
            super().__init__(params)
            self.reg = params[0]

        def run(self, context):
            context.registers[self.reg] += 1
            context.pointer += 1

        def __repr__(self):
            return "inc {0}".format(self.reg)

    class Dec(OneArgInstruction):
        def __init__(self, params):
            super().__init__(params)
            self.params = params
            self.reg = params[0]

        def run(self, context):
            context.registers[self.reg] -= 1
            context.pointer += 1

        def __repr__(self):
            return "dec {0}".format(self.reg)

    class Jnz(TwoArgInstruction):
        def __init__(self, params):
            super().__init__(params)
            self.params = params
            self.val = params[0]
            self.steps = params[1]

        def run(self, context):
            val = self.int_value(self.val, context)
            steps = self.int_value(self.steps, context)
            if val != 0:
                context.pointer += steps
            else:
                context.pointer += 1

        def __repr__(self):
            return "jnz {0} {1}".format(self.val, self.steps)

    def __init__(self):
        self.instructions = {
            re.compile(r"cpy ([a-z]|-?\d+) (\w)"): Assembunny.Cpy,
            re.compile(r"inc ([a-z])"): Assembunny.Inc,
            re.compile(r"dec ([a-z])"): Assembunny.Dec,
            re.compile(r"jnz ([a-z]|\d+) ([a-z]|-?\d+)"): Assembunny.Jnz
        }

    def parse(self, line):
        for regex, clazz in self.instructions.items():
            result = regex.match(line)
            if result:
                return clazz(result.groups())
        raise BaseException("Parse error", line)


class Computer:
    class Context:
        def __init__(self, instructions):
            self.registers = defaultdict(int)
            self.pointer = 0
            self.instructions = [i for i in instructions]

    def __init__(self, instructions):
        self.instructions = list()
        self.parser = Assembunny()
        self.parse(instructions)
        self.context = self.Context(self.instructions)

    def parse(self, instructions):
        for i in instructions:
            self.instructions.append(self.parser.parse(i))

    def run(self):
        self.context.pointer = 0
        while self.context.pointer < len(self.context.instructions):
            instruction = self.context.instructions[self.context.pointer]
            self.dump(instruction)
            instruction.run(self.context)

    def register(self, param):
        return self.context.registers[param]

    def dump(self, running_instruction):
        with open('dump.txt', 'a') as fh:
            print('-' * 50, file=fh)
            print(self.context.registers, file=fh)
            print('-' * 20, file=fh)
            for index, instruction in enumerate(self.context.instructions):
                if self.context.pointer == index:
                    print("=>\t{}".format(running_instruction), file=fh)
                else:
                    print("\t{}".format(repr(instruction)), file=fh)

    def reset(self, param):
        self.context = self.Context(self.instructions)
        self.context.registers.update(param)


if __name__ == '__main__':
    with open('../../../data/2016/input.12.txt', 'r') as fh:
        computer = Computer(fh.readlines())
    computer.run()
    print("Register a contains", computer.register('a'))
    computer.reset({'c': 1})
    computer.run()
    print("Register a contains", computer.register('a'))
