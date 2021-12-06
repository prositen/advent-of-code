from collections import Counter

from python.src.common import Day, timer, Timer


class Line(object):

    def __init__(self, line):
        (y1, x1), (y2, x2) = [p.split(',') for p in line.split(' -> ')]
        (self.y1, self.x1, self.y2, self.x2) = (int(i) for i in (y1, x1, y2, x2))


    def step(self, diagonals):
        if self.y1 == self.y2:
            for x in range(min(self.x1, self.x2),
                           max(self.x1, self.x2) + 1):
                yield self.y1, x
        elif self.x1 == self.x2:
            for y in range(min(self.y1, self.y2),
                           max(self.y1, self.y2) + 1):
                yield y, self.x1
        elif diagonals:
            step_x = 1 if self.x1 < self.x2 else -1
            step_y = 1 if self.y1 < self.y2 else -1
            y = self.y1
            for x in range(self.x1, self.x2 + step_x, step_x):
                yield y, x
                y += step_y


class Dec05(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 5, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return [Line(line) for line in instructions]

    def map_vents(self, diagonals):
        grid = Counter()
        for line in self.instructions:
            for (y, x) in line.step(diagonals=diagonals):
                grid[(y, x)] += 1
        c = Counter(grid.values())
        c[1] = 0
        return sum(c.values())

    @timer(part=1)
    def part_1(self):
        return self.map_vents(False)

    @timer(part=2)
    def part_2(self):
        return self.map_vents(True)


if __name__ == '__main__':
    with Timer('Hydrothermal Venture'):
        Dec05().run_day()
