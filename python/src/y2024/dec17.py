import re
from collections import deque
from enum import IntEnum

from python.src.common import Day, timer, Timer


class OpCode(IntEnum):
    ADV = 0
    BXL = 1
    BST = 2
    JNZ = 3
    BXC = 4
    OUT = 5
    BDV = 6
    CDV = 7


class Computer(object):

    def __init__(self, register_values, instructions):
        self.registers = register_values
        self.instructions = instructions
        self.ip = 0
        self.output = []

    def reset(self, a_register):
        self.registers = [a_register, 0, 0]
        self.ip = 0
        self.output = []

    def print(self):
        return ','.join(str(c) for c in self.output)

    def run(self):
        while self.ip < len(self.instructions):
            self.step()

    def step(self):
        opcode = self.instructions[self.ip]
        operand = self.instructions[self.ip + 1]
        combo = 0
        match operand:
            case 0 | 1 | 2 | 3:
                combo = operand
            case 4 | 5 | 6:
                combo = self.registers[operand - 4]

        match opcode:
            case OpCode.ADV:
                self.registers[0] = self.registers[0] // 2 ** combo
            case OpCode.BXL:
                self.registers[1] = self.registers[1] ^ operand
            case OpCode.BST:
                self.registers[1] = combo % 8
            case OpCode.JNZ:
                if self.registers[0] != 0:
                    self.ip = operand
                    return
            case OpCode.BXC:
                self.registers[1] = self.registers[1] ^ self.registers[2]
            case OpCode.OUT:
                self.output.append(combo % 8)
            case OpCode.BDV:
                self.registers[1] = self.registers[0] // 2 ** combo
            case OpCode.CDV:
                self.registers[2] = self.registers[0] // 2 ** combo

        self.ip += 2


class Dec17(Day, year=2024, day=17, title='Cronospatial Computer'):

    @staticmethod
    def parse_instructions(instructions):
        groups = Day.parse_groups(instructions)
        pattern = re.compile(r'Register (\w): (\d+)')
        registers = [
            int(pattern.match(line).group(2))
            for line in groups[0]
        ]
        return registers, Day.parse_int_line([groups[1][0][9:]])

    @timer(part=1)
    def part_1(self):
        c = Computer(register_values=self.instructions[0], instructions=self.instructions[1])
        c.run()
        return c.print()

    @timer(part=2)
    def part_2(self):
        """
        Output depends only on register A, which is // 8 in each step. A % 8 with some
        bits shifted is then output.

        Find the correct digits one at a time from the back
        """
        computer = Computer(register_values=self.instructions[0],
                            instructions=self.instructions[1])

        to_visit = deque()
        to_visit.append((0, 1))

        max_len = len(self.instructions[1])
        while to_visit:
            a, digit = to_visit.pop()
            looking_for = self.instructions[1][-digit]
            for i in range(0, 8):
                computer.reset(a_register=a + i)
                computer.run()
                if computer.output[0] == looking_for:
                    if digit == max_len:
                        return a + i
                    elif digit < max_len:
                        to_visit.appendleft(((a + i) * 8, digit + 1))


if __name__ == '__main__':
    with Timer('Total'):
        Dec17().run_day()
