import re

from python.src.y2016 import dec12


class Assembunny2(dec12.Assembunny):
    class Nop1(dec12.Assembunny.OneArgInstruction):
        def __init__(self, _, params):
            super().__init__(params)

        def run(self, context):
            context.pointer += 1

    class Nop2(dec12.Assembunny.TwoArgInstruction):
        def __init__(self, _, params):
            super().__init__(params)

        def run(self, context):
            context.pointer += 1

    class Tgl(dec12.Assembunny.OneArgInstruction):
        def __init__(self, params):
            super().__init__(params)
            self.step = params[0]

        def run(self, context):

            change_pointer = context.pointer
            if self.step.isnumeric():
                change_pointer += int(self.step)
            else:
                change_pointer += context.registers[self.step]

            if change_pointer >= len(context.instructions):
                context.pointer += 1
                return
            instruction = context.instructions[change_pointer]

            if isinstance(instruction, dec12.Assembunny.Inc):
                # inc becomes dec
                instruction = dec12.Assembunny.Dec(instruction.params)
            elif isinstance(instruction, dec12.Assembunny.Jnz):
                # jnz becomes cpy
                if instruction.params[1].isnumeric():
                    # cpy num num makes no sense => num
                    instruction = Assembunny2.Nop2(instruction.params)
                else:
                    instruction = Assembunny2.Cpy(instruction.params)
            elif isinstance(instruction, dec12.Assembunny.OneArgInstruction):
                # one-argument instructions become inc
                reg = instruction.params[0]
                if reg.isalpha():
                    instruction = dec12.Assembunny.Inc(instruction.params)
                else:
                    instruction = Assembunny2.Nop1(instruction.params)
            elif isinstance(instruction, dec12.Assembunny.TwoArgInstruction):
                # two-argument instructions become jnz
                reg = instruction.params[0]
                instruction = dec12.Assembunny.Jnz(instruction.params)

            context.instructions[change_pointer] = instruction

            context.pointer += 1

        def __repr__(self):
            return "tgl {}".format(self.step)

    class Multiply(dec12.Assembunny.TwoArgInstruction):
        def __init__(self, params):
            super().__init__(params)
            self.target = params[0]
            self.p1 = params[1]
            self.p2 = params[2]

        def run(self, context):
            p1 = context.registers[self.p1] if self.p1.isalpha else int(self.p1)
            p2 = context.registers[self.p2] if self.p2.isalpha else int(self.p2)
            context.registers[self.target] += p1 * p2
            if self.p1.isalpha:
                context.registers[self.p1] = 0
            if self.p2.isalpha:
                context.registers[self.p2] = 0
            context.pointer += 5

        def __repr__(self):
            return "mul {} {} {}".format(self.target, self.p1, self.p2)

    def __init__(self):
        super().__init__()
        self.instructions[re.compile(r"tgl (\w|\d+)")] = Assembunny2.Tgl


class Computer(dec12.Computer):
    def __init__(self, instructions):
        self.instructions = list()
        self.parser = Assembunny2()
        self.parse(instructions)
        self.context = self.Context(self.instructions)

    def optimize(self):
        p = self.context.pointer
        # Check for multiplication
        if p + 5 < len(self.context.instructions):
            mul = self.context.instructions[p:p + 5]
            if all([isinstance(mul[0], Assembunny2.Inc),
                    isinstance(mul[1], Assembunny2.Dec),
                    isinstance(mul[2], Assembunny2.Jnz),
                    isinstance(mul[3], Assembunny2.Dec),
                    isinstance(mul[4], Assembunny2.Jnz)]):
                target = mul[0].params[0]
                m1 = mul[1].params[0]
                m2 = mul[2].params[0]
                m2_steps = int(mul[2].params[1])
                m3 = mul[3].params[0]
                m4 = mul[4].params[0]
                m4_steps = int(mul[4].params[1])

                if target != m1 and target != m3 and m1 == m2 and m3 == m4 and m2_steps == -2 and m4_steps == -5:
                    return Assembunny2.Multiply((target, m1, m3))
        return self.context.instructions[self.context.pointer]

    def run(self):
        self.context.pointer = 0
        while self.context.pointer < len(self.context.instructions):
            instruction = self.optimize()
            # self.dump(instruction)
            instruction.run(self.context)


if __name__ == '__main__':
    with open('../../../data/2016/input.23.txt', 'r') as fh:
        lines = fh.readlines()
    computer = Computer(lines)
    computer.reset({'a': 7})
    computer.run()
    print("Part 1: Register a contains", computer.register('a'))

    computer.reset({'a': 12})
    computer.run()
    print("Part 2: Register a contains", computer.register('a'))
