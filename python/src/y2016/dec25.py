import re

from python.src.y2016 import dec23


class Assembunny3(dec23.Assembunny2):
    class Out(dec23.Assembunny2.OneArgInstruction):
        def __init__(self, params):
            super().__init__(params)

        def run(self, context):
            context.out = self.int_value(self.params[0], context)
            context.pointer += 1

    def __init__(self):
        super().__init__()
        self.instructions[re.compile(r"out (\w|\d+)")] = Assembunny3.Out


class Computer(dec23.Computer):
    class Context(dec23.Computer.Context):
        def __init__(self, instructions):
            super().__init__(instructions)
            self.out = None

    def __init__(self, instructions, output_length):
        self.instructions = list()
        self.parser = Assembunny3()
        self.parse(instructions)
        self.context = self.Context(self.instructions)
        self.output = list()
        self.output_length = output_length

    def run(self):
        self.context.pointer = 0
        while self.context.pointer < len(self.context.instructions):
            instruction = self.optimize()
            # self.dump(instruction)
            instruction.run(self.context)
            self.handle_output()

    def reset(self, param):
        super().reset(param)
        self.output = list()

    def handle_output(self):
        """
         When we have self.output_length chars of output, quit.
        """
        if self.context.out is not None:
            self.output.append(self.context.out)
            self.context.out = None
            if len(self.output) == self.output_length:
                self.context.pointer = len(self.context.instructions)


if __name__ == '__main__':

    with open('../../../data/2016/input.25.txt', 'r') as fh:
        lines = fh.readlines()
    computer = Computer(lines, 50)
    a = 0
    expected_output = [0, 1] * 50
    while True:
        computer.reset({'a': a})
        computer.run()
        if all(a == b for a, b in zip(computer.output, expected_output)):
            break
        a += 1
    print("Lowest positive integer is", a)
