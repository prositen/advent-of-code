from heapq import heappop, heappush

from python.src.common import Day, timer, Timer


class Computer(object):

    def __init__(self, max_y, max_x, falling):
        self.corrupted = set()
        self.delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
        self.target_y = max_y - 1
        self.target_x = max_x - 1
        self.falling = falling

    def corrupt(self, number):
        self.corrupted = {block for block in self.falling[:number]}

    def in_bounds(self, position):
        return 0 <= position[0] <= self.target_x and 0 <= position[1] <= self.target_y

    def safe_path(self):
        to_visit = list()
        to_visit.append((0, (0, 0)))
        visited = dict()

        while to_visit:
            steps, pos = heappop(to_visit)
            if pos == (self.target_x, self.target_y):
                return steps
            elif pos in visited:
                if visited[pos] <= steps:
                    continue

            visited[pos] = steps
            for d in self.delta:
                px = pos[0] + d[0]
                py = pos[1] + d[1]
                if self.in_bounds((px, py)):
                    if (px, py) not in self.corrupted:
                        heappush(to_visit, (steps + 1, (px, py)))
        return 0

    def bisect(self, low, high=None):
        if high is None:
            high = len(self.falling)
        mid = (low + high) // 2

        self.corrupt(mid)
        if not self.safe_path():
            return self.bisect(low, mid)
        else:
            if high - mid < 2:
                return self.falling[high - 1]
            return self.bisect(mid, high)


class Dec18(Day, year=2024, day=18, title='RAM Run'):

    @staticmethod
    def parse_instructions(instructions):
        return [
            (line[0], line[1]) for line in
            Day.parse_multiple_ints_per_line(instructions, separator=',')
        ]

    @timer(part=1)
    def part_1(self):
        c = Computer(max_y=71, max_x=71, falling=self.instructions)
        c.corrupt(1024)
        return c.safe_path()

    @timer(part=2)
    def part_2(self):
        c = Computer(max_y=71, max_x=71, falling=self.instructions)
        p = c.bisect(low=1024)
        return f'{(p[0])},{p[1]}'


if __name__ == '__main__':
    with Timer('Total'):
        Dec18().run_day()
