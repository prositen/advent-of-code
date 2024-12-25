from collections import defaultdict, deque

from python.src.common import Day, timer, Timer


class FruitMonitor(object):

    def __init__(self, register_values):
        self.reg = defaultdict(int, register_values)

    def run(self, instructions):
        to_run = deque(instructions)

        while to_run:
            (op1, command, op2, _, target) = instruction = to_run.popleft()
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
        output = 0
        for o in output_gates:
            output = output * 2 + self.reg[o]
        return output


class Analyzer(object):

    def __init__(self, gates):
        self.gates_by_operation = {
            (g[1], frozenset({g[0], g[2]})): g[4]
            for g in gates
        }
        self.faulty = set()

    def run(self):
        carry = self.gates_by_operation[('AND', frozenset({'x00', 'y00'}))]
        for i in range(1, 44):
            carry = self.adder(i, carry)

    def lookup(self, op, a, b):
        ab = frozenset({a, b})
        return self.gates_by_operation.get((op, ab))

    def adder(self, i, carry):
        x = f'x{i:02}'
        y = f'y{i:02}'
        z = f'z{i:02}'
        xor_1 = self.lookup('XOR', x, y)

        if (and_1 := self.lookup('AND', x, y)) == z:
            self.faulty.add(z)

        if not (and_2 := self.lookup('AND', xor_1, carry)):
            self.faulty.add(and_1)
            self.faulty.add(xor_1)
            (and_1, xor_1) = (xor_1, and_1)
            and_2 = self.lookup('AND', xor_1, carry)

        if (xor_2 := self.lookup('XOR', xor_1, carry)) != z:
            self.faulty.update({xor_2, z})
            if and_1 == z:
                xor_2, and_1 = z, xor_2

        if carry := self.lookup('OR', and_1, and_2):
            if carry == z:
                self.faulty.add(carry)
                if xor_2 in self.faulty:
                    return xor_2
            return carry

        return self.lookup('OR', and_1, xor_2)


class Dec24(Day, year=2024, day=24, title='Crossed Wires'):

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
        al = Analyzer(self.instructions[1])
        al.run()
        return ','.join(sorted(al.faulty))


if __name__ == '__main__':
    with Timer('Total'):
        Dec24().run_day()
