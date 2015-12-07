from collections import defaultdict
from enum import Enum
import re

__author__ = 'anna'

RE_STORE = re.compile("(\\d+) -> (\\w+)")
RE_AND = re.compile("(\\w+) AND (\\w+) -> (\\w+)")
RE_LSHIFT = re.compile("(\\w+) LSHIFT (\\d+) -> (\\w+)")
RE_NOT = re.compile("NOT (\\w+) -> (\\w+)")
RE_OR = re.compile("(\\w+) OR (\\w+) -> (\\w+)")
RE_RSHIFT = re.compile("(\\w+) RSHIFT (\\d+) -> (\\w+)")


class Tokens(Enum):
    T_REGISTER = 0,
    T_DECIMAL = 1,
    T_STORE = 1,
    T_AND = 2,
    T_LSHIFT = 3,
    T_NOT = 4,
    T_OR = 5,
    T_RSHIFT = 6


class Command(object):
    def run(self, context):
        pass


class OneParamCommand(Command):
    in1 = None
    out = None

    def __init__(self, in1, out):
        self.in1 = in1
        self.out = out


class TwoParamCommand(Command):
    in1 = None
    in2 = None
    out = None

    def __init__(self, in1, in2, out):
        self.in1 = in1
        self.in2 = in2
        self.out = out


class StoreCommand(OneParamCommand):

    def run(self, context):
        context[self.out] = self.in1


class AndCommand(TwoParamCommand):
    def run(self, context):
        context[self.out] = context[self.in1] & context[self.in2]
        print(context[self.out])


class OrCommand(TwoParamCommand):
    def run(self, context):
        context[self.out] = context[self.in1] | context[self.in2]


class NotCommand(OneParamCommand):
    def run(self, context):
        bin_num = format(self.out, '#018b')
        bin_num.replace('1', '2').replace('0','1').replace('2','1')
        int_num = int(bin_num, 2)
        context[self.out] = int_num


class LShiftCommand(TwoParamCommand):
    def run(self, context):
        context[self.out] = context[self.in1] << self.out


class RShiftCommand(TwoParamCommand):
    def run(self, context):
        context[self.out] = context[self.in1] >> self.out


def parse(line):
    pass


def run(instructions):
    registers = defaultdict(int)
    return registers