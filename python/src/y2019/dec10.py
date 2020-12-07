import math
from collections import defaultdict
from python.src.common import Day, timer


class Dec10(Day):

    def __init__(self, filename=None, instructions=None):
        super().__init__(2019, 10, instructions, filename)
        self.max_x, self.max_y, self.asteroids = self.instructions
        self.best_position = (-1, -1)
        self.positions = dict()
        self.calc_angles()

    @staticmethod
    def parse_instructions(instructions):
        pos = list()
        for y, row in enumerate(instructions):
            for x, c in enumerate(row):
                if c != '.':
                    pos.append((x, y))
        return len(instructions[0]), len(instructions), pos

    @staticmethod
    def dist(a, b):
        return abs(a[1] - b[1]) + abs(a[0] - b[0])

    def calc_angles(self):
        pi2 = 2 * math.pi
        for me in self.asteroids:
            positions = defaultdict(list)
            for other in self.asteroids:
                if me != other:
                    # Switch around the coordinates a bit to get the order I want
                    # for sorting. (Start ^ and rotate >)
                    angle = (pi2 + math.atan2(other[0] - me[0], me[1] - other[1])) % pi2
                    positions[angle].append((self.dist(me, other), other))
            self.positions[me] = positions

    @timer(part=1, title='Asteroids detected')
    def part_1(self):
        best = 0
        for asteroid, positions in self.positions.items():
            if len(positions.keys()) > best:
                best = len(positions.keys())
                self.best_position = asteroid
        return best

    @timer(part=2, title='Last vaporized asteroid @ X*100 + Y')
    def part_2(self):
        starmap = self.positions[self.best_position]
        sorted_map = {
            k: sorted(starmap[k])
            for k in sorted(starmap)
        }
        vaporized = 0
        while True:
            for angle in sorted_map:
                try:
                    _, pos = sorted_map[angle].pop()
                    vaporized += 1
                    if vaporized == 200:
                        return pos[1] + (pos[0] * 100)
                except IndexError:
                    pass


if __name__ == '__main__':
    Dec10().run_day()
