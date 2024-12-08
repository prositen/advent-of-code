import itertools
from collections import defaultdict
from typing import Tuple

from python.src.common import Day, timer, Timer


class SignalMap(object):

    def __init__(self, instructions, resonant_harmonics=False):
        self.anti_nodes = set()
        self.antennas = defaultdict(set)
        self.max_y = len(instructions)
        self.max_x = len(instructions[0])
        self.resonant_harmonics = resonant_harmonics
        for y, row in enumerate(instructions):
            for x, char in enumerate(row):
                if char != '.':
                    self.antennas[char].add((y, x))

    def get_points(self, point: Tuple[int], dy: int, dx: int):
        point = point[0] + dy, point[1] + dx
        while 0 <= point[0] < self.max_y and 0 <= point[1] < self.max_x:
            yield point
            if not self.resonant_harmonics:
                break
            point = point[0] + dy, point[1] + dx

    def count_anti_nodes(self):
        for antenna, positions in self.antennas.items():
            for p1, p2 in itertools.combinations(positions, 2):
                if self.resonant_harmonics:
                    self.anti_nodes.update({p1, p2})

                dy, dx = p1[0] - p2[0], p1[1] - p2[1]
                for point in self.get_points(p1, dy, dx):
                    self.anti_nodes.add(point)
                for point in self.get_points(p2, -dy, -dx):
                    self.anti_nodes.add(point)

        return len(self.anti_nodes)


class Dec08(Day, year=2024, day=8, title='Resonant Collinearity'):

    @timer(part=1)
    def part_1(self):
        sm = SignalMap(self.instructions)
        return sm.count_anti_nodes()

    @timer(part=2)
    def part_2(self):
        sm = SignalMap(self.instructions, resonant_harmonics=True)
        return sm.count_anti_nodes()


if __name__ == '__main__':
    with Timer('Total'):
        Dec08().run_day()
