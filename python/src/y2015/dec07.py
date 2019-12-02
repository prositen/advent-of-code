import re

__author__ = 'anna'


class Param(object):
    value = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def val(self, context):
        pass

    @classmethod
    def parse(cls, param):
        if re.match(r'\d+', param):
            return ValParam(param)
        elif re.match(r'\w+', param):
            return VarParam(param)


class ValParam(Param):
    def val(self, context):
        return int(self.value)


class VarParam(Param):
    def val(self, context):
        if self.value in context:
            return int(context[self.value])
        else:
            return None


class Command(object):
    def run(self, context):
        pass


class OneParamCommand(Command):
    in1 = None
    out = None

    def __init__(self, in1, out):
        self.in1 = Param.parse(in1)
        self.out = out

    def can_run(self, context):
        return self.in1.val(context) is not None


class TwoParamCommand(Command):
    in1 = None
    in2 = None
    out = None

    def __init__(self, in1, in2, out):
        self.in1 = Param.parse(in1)
        self.in2 = Param.parse(in2)
        self.out = out

    def can_run(self, context):
        return self.in1.val(context) is not None and self.in2.val(context) is not None


class StoreCommand(OneParamCommand):
    def run(self, context):
        context[self.out] = int(self.in1.val(context))

    def __str__(self):
        return "{0} -> {1}".format(self.in1, self.out)


class AndCommand(TwoParamCommand):
    def run(self, context):
        context[self.out] = self.in1.val(context) & self.in2.val(context)

    def __str__(self):
        return "{0} AND {1} -> {2}".format(self.in1, self.in2, self.out)


class OrCommand(TwoParamCommand):
    def run(self, context):
        context[self.out] = self.in1.val(context) | self.in2.val(context)

    def __str__(self):
        return "{0} OR {1} -> {2}".format(self.in1, self.in2, self.out)


class NotCommand(OneParamCommand):
    """ Home-brewed two's complement. The built-in one works on infinite number of bytes,
    which doesn't help me.
    """

    def run(self, context):
        bin_num = format(self.in1.val(context), '016b')
        bin_num = bin_num.replace('1', '2').replace('0', '1').replace('2', '0')
        int_num = int(bin_num, 2)
        context[self.out] = int_num

    def __str__(self):
        return "NOT {0} -> {1}".format(self.in1, self.out)


class LShiftCommand(TwoParamCommand):
    def run(self, context):
        context[self.out] = self.in1.val(context) << self.in2.val(context)

    def input(self):
        return [self.in1]

    def __str__(self):
        return "{0} LSHIFT {1} -> {2}".format(self.in1, self.in2, self.out)


class RShiftCommand(TwoParamCommand):
    def run(self, context):
        context[self.out] = self.in1.val(context) >> self.in2.val(context)

    def input(self):
        return [self.in1]

    def __str__(self):
        return "{0} RSHIFT {1} -> {2}".format(self.in1, self.in2, self.out)


RE_STORE = re.compile(r'(\w+) -> (\w+)')
RE_AND = re.compile(r'(\w+) AND (\w+) -> (\w+)')
RE_LSHIFT = re.compile(r'(\w+) LSHIFT (\w+) -> (\w+)')
RE_NOT = re.compile(r'NOT (\w+) -> (\w+)')
RE_OR = re.compile(r'(\w+) OR (\w+) -> (\w+)')
RE_RSHIFT = re.compile(r'(\w+) RSHIFT (\w+) -> (\w+)')

Commands = {
    RE_STORE: StoreCommand,
    RE_AND: AndCommand,
    RE_LSHIFT: LShiftCommand,
    RE_NOT: NotCommand,
    RE_OR: OrCommand,
    RE_RSHIFT: RShiftCommand
}


def parse(line):
    for cmdRe, cmdClass in Commands.items():
        result = re.match(cmdRe, line)
        if result:
            return cmdClass(*result.groups())


def run(instructions, preset=None):
    registers = dict()
    if preset is not None:
        registers.update(preset)
        print("preset: ", preset, "registers:", registers)
    circuits = list()
    for no, line in enumerate(instructions):
        command = parse(line)
        if preset and str(command.out) in preset.keys():
            print("Skipping instruction {line}".format(line=line))
        else:
            circuits.append((no, command))

    while circuits:
        (line, command) = circuits.pop(0)
        if command.can_run(registers):
            command.run(registers)
        else:
            circuits.append((line, command))

    return registers


if __name__ == '__main__':
    with open('../../../data/2015/input.7.txt', 'r') as fh:
        regs = run(fh.readlines())
        print("Register A contains:", regs['a'])

        fh.seek(0)
        task_2 = {'b': regs['a']}
        regs_2 = run(fh.readlines(), task_2)
        print("Register A contains:", regs_2['a'])
