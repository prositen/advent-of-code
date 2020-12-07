from python.src.common import Day, timer


class Grid(object):
    DIRS = {
        'U': (1, 0),
        'R': (0, 1),
        'D': (-1, 0),
        'L': (0, -1)
    }

    def __init__(self):
        self.grid = dict()
        self.closest = None
        self.delay = None

    def next_move(self, pos, m):
        _dir = self.DIRS.get(m[0])
        for step in range(1, int(m[1:]) + 1):
            yield pos[0] + step * _dir[0], pos[1] + step * _dir[1]

    def add_wire(self, path, wire_id=0):
        pos = (0, 0)
        steps = 1
        for step in path:
            for pos in self.next_move(pos, step):
                prev_steps = self.grid.get(pos, {0: None, 1: None})
                if prev_steps[1 - wire_id] is not None:
                    if not prev_steps[wire_id]:
                        prev_steps[wire_id] = steps
                    self.add_intersection(pos[0], pos[1], prev_steps)
                self.grid[pos] = {wire_id: steps, 1 - wire_id: prev_steps[1 - wire_id]}
                steps += 1

    def add_intersection(self, y, x, steps):
        distance = abs(x) + abs(y)
        if distance == 0:
            return
        if self.closest is None or self.closest > distance:
            self.closest = distance
        delay = sum(steps.values())
        if self.delay is None or self.delay > delay:
            self.delay = delay


class Dec03(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2019, 3, instructions, filename)
        self.g = Grid()
        self.g.add_wire(self.instructions[0], wire_id=0)
        self.g.add_wire(self.instructions[1], wire_id=1)

    @staticmethod
    def parse_instructions(instructions):
        return [row.split(',') for row in instructions]

    @timer(part=1, title='Manhattan distance to closest intersection')
    def part_1(self):
        return self.g.closest

    @timer(part=2, title='Minimum number of steps to an intersection')
    def part_2(self):
        return self.g.delay


if __name__ == '__main__':
    Dec03().run_day()
