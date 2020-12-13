from functools import reduce
from math import gcd

from python.src.common import Day, Timer, timer


def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)


def lcmm(*args):
    """Return lcm of args."""
    return reduce(lcm, args)


class Dec13(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 13, instructions, filename)
        self.timestamp, self.buses = self.instructions

    @staticmethod
    def parse_instructions(instructions):
        timestamp = int(instructions[0], 10)
        buses = [int(c, 10) if c != 'x' else 0 for c in instructions[1].split(',')]
        return timestamp, buses

    @timer(part=1)
    def part_1(self):
        minutes = [(c, c - (self.timestamp % c)) for c in self.buses if c]
        next_bus = min(minutes, key=lambda c: c[1])
        return next_bus[0] * next_bus[1]

    @timer(part=2)
    def part_2(self):
        buses = [c for c in enumerate(self.buses) if c[1]]
        largest = max(buses, key=lambda b: b[1])
        largest_offset = largest[0]
        buses = [(c[0] - largest[0], c[1]) for c in buses]
        n = 1
        while True:
            timestamp = largest[1] * n
            valid = True
            for offset, bus in buses:
                if (timestamp + offset) % bus:
                    valid = False
                    break
            if valid:
                return timestamp - largest_offset
            n += 1


if __name__ == '__main__':
    with Timer():
        Dec13().run_day()
