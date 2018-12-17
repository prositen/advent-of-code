import re

from python.src.common import Day


class Device(object):
    def __init__(self):
        self.reg = [0, 0, 0, 0]
        self.instructions = {
            'addr': lambda a, b: self.reg[a] + self.reg[b],
            'addi': lambda a, b: self.reg[a] + b,
            'mulr': lambda a, b: self.reg[a] * self.reg[b],
            'muli': lambda a, b: self.reg[a] * b,
            'banr': lambda a, b: self.reg[a] & self.reg[b],
            'bani': lambda a, b: self.reg[a] & b,
            'borr': lambda a, b: self.reg[a] | self.reg[b],
            'bori': lambda a, b: self.reg[a] | b,
            'setr': lambda a, b: self.reg[a],
            'seti': lambda a, b: a,
            'gtir': lambda a, b: int(a > self.reg[b]),
            'gtri': lambda a, b: int(self.reg[a] > b),
            'gtrr': lambda a, b: int(self.reg[a] > self.reg[b]),
            'eqir': lambda a, b: int(a == self.reg[b]),
            'eqri': lambda a, b: int(self.reg[a] == b),
            'eqrr': lambda a, b: int(self.reg[a] == self.reg[b])
        }

    def sample(self, before, instruction, after):
        matches = []
        opcode, a, b, c = instruction
        for k, v in self.instructions.items():
            self.reg = [reg for reg in before]
            self.reg[c] = v(a, b)
            if self.reg == after:
                matches.append(k)
        return matches

    def run(self, program, opcode_translation):
        self.reg = [0, 0, 0, 0]
        for opcode, a, b, c in program:
            instruction = opcode_translation.get(opcode)
            if instruction:
                self.reg[c] = self.instructions[instruction](a, b)


class Dec16(Day):
    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 16, instructions, filename)
        self.samples, self.program = self.instructions
        self.device = Device()

    @staticmethod
    def parse_instructions(instructions):
        re_ints = re.compile(r'(\d+)')
        state = 0
        samples = list()
        program = list()
        before = instruction = None
        for line in instructions:
            if len(line.strip()) == 0:
                continue
            numbers = list(map(int, re_ints.findall(line)))
            if state == 0:
                if line.startswith('Before'):
                    state = 1
                    before = numbers
                else:
                    program.append(numbers)
            elif state == 1:
                state = 2
                instruction = numbers
            elif state == 2 and line.startswith('After'):
                state = 0
                after = numbers
                samples.append((before, instruction, after))

        return samples, program

    def part_1(self):
        matching_opcodes = [
            self.device.sample(s[0], s[1], s[2]) for s in self.samples
        ]
        three_or_more = [mo for mo in matching_opcodes if len(mo) >= 3]
        return len(three_or_more)

    def part_2(self):
        lookup = dict()
        samples_per_opcode = dict()
        for sample in self.samples:
            matching_ops = self.device.sample(sample[0], sample[1], sample[2])
            opcode = sample[1][0]
            samples_per_opcode[opcode] = samples_per_opcode.get(opcode, set()).union(matching_ops)
        while len(lookup) < len(self.device.instructions):
            one_entry = {opcode: list(opname)[0] for opcode, opname in samples_per_opcode.items() if len(opname) == 1}
            for code, name in one_entry.items():
                lookup[code] = name
                for k in samples_per_opcode:
                    samples_per_opcode[k].discard(name)
        self.device.run(program=self.program, opcode_translation=lookup)
        return self.device.reg[0]


if __name__ == '__main__':
    d = Dec16()
    print("Samples with 3 or more opcodes:", d.part_1())
    print("Reg[0] value after execution:", d.part_2())
