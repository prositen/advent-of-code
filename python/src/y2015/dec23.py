__author__ = 'anna'
import re


class Instruction(object):
    regexp = re.compile('')

    def __init__(self, text):
        result = self.regexp.match(text)
        if result:
            self.group = result.group
            self.instruction = self.group('i')
        else:
            raise ValueError

    def run(self, registers):
        pass

    def __str__(self):
        return self.instruction


class RegistryInstruction(Instruction):
    registry = None

    def __init__(self, text):
        super(RegistryInstruction, self).__init__(text)
        self.registry = self.group('reg')

    def __str__(self):
        return "{0} {1}".format(super(RegistryInstruction, self).__str__(), self.registry)


class OffsetInstruction(Instruction):
    offset = 0

    def __init__(self, text):
        super(OffsetInstruction, self).__init__(text)
        self.offset = int(self.group('offset'))

    def __str__(self):
        return "{0} {1}".format(super(OffsetInstruction, self).__str__(), self.offset)


class HlfInstruction(RegistryInstruction):
    """hlf r sets register r to half its current value, then continues with the next instruction."""
    regexp = re.compile(r'(?P<i>hlf) (?P<reg>\w)')

    def run(self, registers):
        registers[self.registry] = int(registers[self.registry] / 2)
        return registers, 1


class TplInstruction(RegistryInstruction):
    """tpl r sets register r to triple its current value, then continues with the next instruction."""
    regexp = re.compile(r'(?P<i>tpl) (?P<reg>\w)')

    def run(self, registers):
        registers[self.registry] *= 3
        return registers, 1


class IncInstruction(RegistryInstruction):
    """inc r increments register r, adding 1 to it, then continues with the next instruction."""
    regexp = re.compile(r'(?P<i>inc) (?P<reg>\w)')

    def run(self, registers):
        registers[self.registry] += 1
        return registers, 1


class JmpInstruction(OffsetInstruction):
    """jmp offset is a jump; it continues with the instruction offset away relative to itself."""
    regexp = re.compile(r'(?P<i>jmp) (?P<offset>[+-]\d+)')

    def run(self, registers):
        return registers, self.offset


class JieInstruction(RegistryInstruction, OffsetInstruction):
    """jie r, offset is like jmp, but only jumps if register r is even ("jump if even")."""
    regexp = re.compile(r'(?P<i>jie) (?P<reg>\w), (?P<offset>[+-]\d+)')

    def __str__(self):
        return "{0} {1} {2}".format(self.instruction, self.registry, self.offset)

    def run(self, registers):
        if registers[self.registry] % 2 == 0:
            return registers, self.offset
        else:
            return registers, 1


class JioInstruction(RegistryInstruction, OffsetInstruction):
    """jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd)."""
    regexp = re.compile(r'(?P<i>jio) (?P<reg>\w), (?P<offset>[+-]\d+)')

    def __str__(self):
        return "{0} {1} {2}".format(self.instruction, self.registry, self.offset)

    def run(self, registers):
        if registers[self.registry] == 1:
            return registers, self.offset
        else:
            return registers, 1


class IllegalInstruction(Instruction):
    def __init__(self, text):
        super(IllegalInstruction, self).__init__(text)
        self.instruction = 'Illegal'

    def run(self, registers):
        return registers, None


class Program(object):
    Instructions = [
        HlfInstruction,
        TplInstruction,
        IncInstruction,
        JmpInstruction,
        JieInstruction,
        JioInstruction
    ]

    def __init__(self, lines):
        self.instructions = [self.parse(line) for line in lines]

    def parse(self, line):
        for InstructionClass in self.Instructions:
            try:
                return InstructionClass(line)
            except ValueError:
                pass
        else:
            return IllegalInstruction(line)

    def run(self, registers):
        address = 0
        offset = 0
        try:
            while offset is not None:
                address += offset
                instruction = self.instructions[address]
                registers, offset = instruction.run(registers)
                # print('{0}: {1}  ({2})'.format(address, instruction, registers))
        except IndexError:
            pass

        return registers


def main():
    with open('../../,,/data/2015/input.23.txt', 'r') as fh:
        program = Program(fh.readlines())

    print(program.run({'a': 0, 'b': 0}))

    print(program.run({'a': 1, 'b': 0}))


if __name__ == '__main__':
    main()
