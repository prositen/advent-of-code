from collections import deque

from python.src.common import Day, timer, Timer


class Grid(object):

    def __init__(self, items):
        self.grid = {
            y: line for y, line in enumerate(items)
        }
        self.maxy = len(self.grid)
        self.maxx = len(self.grid[0])

    def neighbours(self, y, x):
        nb = list()
        if y > 0:
            nb.append((y - 1, x, self.grid[y - 1][x]))
        if y < self.maxy - 1:
            nb.append((y + 1, x, self.grid[y + 1][x]))
        if x > 0:
            nb.append((y, x - 1, self.grid[y][x - 1]))
        if x < self.maxx - 1:
            nb.append((y, x + 1, self.grid[y][x + 1]))
        return nb

    def risk_levels(self):
        return sum(p[2] + 1 for p in self.low_points())

    def low_points(self):
        low_points = list()
        for y, row in self.grid.items():
            for x, val in enumerate(row):
                if all(val < n[2] for n in self.neighbours(y, x)):
                    low_points.append((y, x, val))
        return low_points

    def fill_areas(self):
        basins = list()
        for (y, x, _) in self.low_points():
            to_visit = deque()
            to_visit.append((y, x))

            visited = set()
            while to_visit:
                y, x = to_visit.pop()
                if (y, x) not in visited:
                    to_visit.extendleft((yy, xx)
                                        for yy, xx, val in self.neighbours(y, x)
                                        if val < 9)
                    visited.add((y, x))
            basins.append(len(visited))

        basins = sorted(basins, reverse=True)
        return basins[0] * basins[1] * basins[2]


class Dec09(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 9, instructions=instructions, filename=filename)

    @staticmethod
    def parse_instructions(instructions):
        return [Day.parse_digits([line])
                for line in instructions]

    @timer(part=1)
    def part_1(self):
        return Grid(self.instructions).risk_levels()

    @timer(part=2)
    def part_2(self):
        return Grid(self.instructions).fill_areas()


if __name__ == '__main__':
    with Timer('Smoke Basin'):
        Dec09().run_day()
