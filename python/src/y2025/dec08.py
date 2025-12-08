import operator
from collections import deque
from functools import reduce

from python.src.common import Day, timer, Timer
from python.src.common import straight_line_distance


class Decoration:
    def __init__(self, junction_boxes, connections):
        self.junction_boxes = junction_boxes
        self.distances = dict()
        self.circuits: list[set] = []
        self.connections = connections

    def calculate_distance(self):
        for i, box_a in enumerate(self.junction_boxes):
            for box_b in self.junction_boxes[i + 1:]:
                self.distances[(box_a, box_b)] = straight_line_distance(box_a, box_b)

    def add_to_circuits(self, boxes):
        for circuit in self.circuits:
            if circuit.intersection(boxes):
                circuit.update(boxes)
                break
        else:
            self.circuits.append(boxes)

    def connect_closest(self):
        reverse_distances = list(sorted(self.distances.items(), key=lambda d: d[1]))
        for _ in range(self.connections):
            (box_a, box_b), _ = reverse_distances.pop(0)
            self.add_to_circuits({box_a, box_b})

        queue = deque(self.circuits)
        self.circuits = []
        while queue:
            circuit = queue.popleft()
            for n, other_circuit in enumerate(queue):
                if circuit.intersection(other_circuit):
                    queue.remove(other_circuit)
                    queue.appendleft(other_circuit | circuit)

                    break
            else:
                self.circuits.append(circuit)
        remaining_boxes = set(self.junction_boxes).difference(*self.circuits)
        for c in remaining_boxes:
            self.add_to_circuits({c})

    def largest_circuits(self):
        self.calculate_distance()
        self.connect_closest()
        sizes = sorted([len(c) for c in self.circuits], reverse=True)
        return reduce(operator.mul, sizes[:3])


class Dec08(Day, year=2025, day=8, title='Playground'):

    @staticmethod
    def parse_instructions(instructions):
        return list(tuple(map(int, line.split(',')))
                    for line in instructions)

    @timer(part=1)
    def part_1(self):
        return Decoration(self.instructions, connections=1000).largest_circuits()

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec08().run_day()
