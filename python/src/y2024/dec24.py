from collections import defaultdict, deque

from python.src.common import Day, timer, Timer

class FruitMonitor(object):

    def __init__(self, register_values):
        self.reg = defaultdict(int, register_values)

    def run(self, instructions):
        to_run = deque(instructions)

        while to_run:
            instruction  = to_run.popleft()
            (op1, command, op2, _, target) = instruction
            if op1 in self.reg and op2 in self.reg:
                match command:
                    case 'AND':
                        self.reg[target] = self.reg[op1] & self.reg[op2]
                    case 'OR':
                        self.reg[target] = self.reg[op1] | self.reg[op2]
                    case 'XOR':
                        self.reg[target] = self.reg[op1] ^ self.reg[op2]
            else:
                to_run.append(instruction)


        output_gates = sorted((k for k in self.reg.keys() if k[0] == 'z'), reverse=True)
        output_bits = ''.join(str(self.reg[o]) for o in output_gates)
        return int(output_bits, 2)

class Dec24(Day, year=2024, day=24):

    @staticmethod
    def parse_instructions(instructions):
        groups = Day.parse_groups(instructions)

        initial_values = {
            (g := line.split(':'))[0]: int(g[1])
            for line in groups[0]
        }

        commands = [
            tuple(g.split(' '))
            for g in groups[1]
        ]
        return initial_values, commands

    @timer(part=1)
    def part_1(self):
        fm = FruitMonitor(self.instructions[0])
        return fm.run(self.instructions[1])

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec24().run_day()
