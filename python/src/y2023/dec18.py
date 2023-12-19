from collections import defaultdict
from itertools import pairwise

from python.src.common import Day, timer, Timer


class LavaLagoon(object):
    def __init__(self, dig_plan):
        self.delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
        self.dig_plan = dig_plan
        self.grid = defaultdict(dict)
        self.pos = 0, 0

    def dig(self, delta, step):
        for _ in range(step):
            self.pos = self.pos[0] + delta[0], self.pos[1] + delta[1]
            self.grid[self.pos[0]][self.pos[1]] = True

    def outline(self):
        for direction, step in self.dig_plan:
            self.dig(direction, step)

    def fill(self):

        visit = set()
        while not visit:
            for y, line in enumerate(self.grid):
                x = min(self.grid[line])
                if x + 1 not in self.grid[line]:
                    visit.add((y, x + 1))
                    break

        while visit:
            p = visit.pop()
            if p[1] in self.grid[p[0]]:
                continue

            self.grid[p[0]][p[1]] = True
            for nb in ((p[0] + d[0], p[1] + d[1]) for d in self.delta):
                visit.add(nb)

    def count(self):
        self.outline()
        self.fill()
        return sum(len(row) for row in self.grid.values())


class MathLagoon(object):

    def __init__(self, dig_plan):

        self.vertices = list()
        self.boundary = 0
        self.dig_plan = dig_plan
        self.pos = 20, 20

    def outline(self):
        self.vertices = [self.pos]

        for delta, steps in self.dig_plan:
            self.boundary += steps
            self.pos = self.pos[0] + (steps * delta[0]), self.pos[1] + (steps * delta[1])
            self.vertices.append(self.pos)

    def count(self):
        self.outline()

        # Shoelace formula to get the area
        double_area = 0
        for v1, v2 in pairwise(self.vertices):
            double_area += v1[1] * v2[0] - v2[1] * v1[0]
        area = abs(double_area // 2)

        # This doesn't include the complete area of the boundary
        # since it's 1 meter wide and not just a perimeter line
        #
        # Using Pick's theorem, the interior area of the polygon is as follows:
        # interior = area - self.boundary // 2 + 1
        #
        # And the total area is then interior + area or
        return area + self.boundary // 2 + 1


class Dec18(Day, year=2023, day=18):

    @staticmethod
    def parse_instructions(instructions):
        return [r.split() for r in instructions]

    @timer(part=1)
    def part_1(self):
        delta = {
            'U': (-1, 0),
            'R': (0, 1),
            'D': (1, 0),
            'L': (0, -1)
        }
        dig_plan = [(delta[c[0]], int(c[1])) for c in self.instructions]
        ll = LavaLagoon(dig_plan=dig_plan)
        return ll.count()

    @timer(part=2)
    def part_2(self):
        delta = {
            '0': (0, 1),
            '1': (1, 0),
            '2': (0, -1),
            '3': (-1, 0)
        }
        dig_plan = [(delta[value[-2]], int(value[2:-2], 16))
                    for _, _, value in self.instructions]
        hl = MathLagoon(dig_plan=dig_plan)
        return hl.count()


if __name__ == '__main__':
    with Timer('Total'):
        Dec18().run_day()
