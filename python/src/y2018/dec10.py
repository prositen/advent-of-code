import re
from python.src.common import Day

re_POINT = re.compile(r'(-?\d+)')


class Point(object):
    def __init__(self, args):
        (self.x, self.y, self.dx, self.dy) = args

    @staticmethod
    def from_str(string):
        return Point(map(int, re_POINT.findall(string)))

    def at_time(self, time):
        return Point((self.x + self.dx * time, self.y + self.dy * time, self.dx, self.dy))


class Grid(object):
    def __init__(self, points):
        self.points = points
        self.min_x = self.max_x = points[0].x
        self.min_y = self.max_y = points[0].y
        for p in points[1:]:
            self.min_x = min(self.min_x, p.x)
            self.max_x = max(self.max_x, p.x)
            self.min_y = min(self.min_y, p.y)
            self.max_y = max(self.max_y, p.y)

    def get_bounding_box_area(self):
        return abs(self.max_x - self.min_x) * abs(self.max_y - self.min_y)

    def __str__(self):
        grid = [
            ['.' for _ in range(self.min_x, self.max_x + 1)]
            for _ in range(self.min_y, self.max_y + 1)
        ]
        for p in self.points:
            grid[p.y - self.min_y][p.x - self.min_x] = '#'
        return '\n'.join(''.join(y) for y in grid)


class Dec10(Day):
    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 10, instructions, filename)
        self.time = 0
        self.run()

    @staticmethod
    def parse_instructions(instructions):
        return [Point.from_str(s) for s in instructions]

    def run(self):
        g = Grid(self.instructions)
        prev_area = g.get_bounding_box_area()
        time = 0
        while True:
            time += 1
            g = Grid([p.at_time(time) for p in self.instructions])
            area = g.get_bounding_box_area()
            if area > prev_area:
                break
            prev_area = area

        self.time = time - 1

    def part_1(self):
        return Grid([p.at_time(self.time) for p in self.instructions])

    def part_2(self):
        return self.time


if __name__ == '__main__':
    d = Dec10()
    print("Message:")
    print(d.part_1())
    print("Time to wait:", d.part_2())
