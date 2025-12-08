import itertools
import math
from collections import deque
from math import prod

from python.src.common import Day, timer, Timer


class Decoration:
    def __init__(self, junction_boxes):
        self.junction_boxes = junction_boxes
        self.distances = sorted(
            itertools.combinations(self.junction_boxes, 2),
            key=lambda bb: math.dist(*bb)
        )
        self.circuits: list[set] = []

    @staticmethod
    def add_to_circuits(box_a, box_b, circuits):
        new_circuit = {box_a, box_b}
        for index, circuit in enumerate(circuits):
            if box_a in circuit:
                new_circuit |= circuit
                circuits.remove(circuit)
            elif box_b in circuit:
                new_circuit |= circuit
                circuits.remove(circuit)
        circuits.append(new_circuit)

    def largest_circuits(self, connections):
        circuits = list()
        for box_a, box_b in self.distances[:connections]:
            self.add_to_circuits(box_a, box_b, circuits)

        remaining_boxes = set(self.junction_boxes).difference(*circuits)

        circuits.extend([{c} for c in remaining_boxes])

        sizes = sorted([len(c) for c in circuits], reverse=True)
        return prod(sizes[:3])


class Dec08(Day, year=2025, day=8, title='Playground'):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.decoration = None

    @staticmethod
    def parse_instructions(instructions):
        return (tuple(map(int, line.split(',')))
                for line in instructions)

    @timer(part=1)
    def part_1(self):
        self.decoration = self.decoration or Decoration(self.instructions)
        return self.decoration.largest_circuits(connections=1000)

    @timer(part=2)
    def part_2(self):
        self.decoration = self.decoration or Decoration(self.instructions)
        return 0

if __name__ == '__main__':
    with Timer('Total'):
        Dec08().run_day()
