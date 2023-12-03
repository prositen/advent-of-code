import itertools

from python.src.common import Day, timer, Timer


class Schematic(object):

    def __init__(self, instructions):
        self.grid = instructions
        self.max_x = len(instructions[0])
        self.max_y = len(instructions)
        self.delta = list(itertools.product((-1, 0, 1), repeat=2))
        self.part_sum = 0
        self.gear_ratio = 0
        self.find_parts()

    def neighbours(self, y, x):
        for delta in self.delta:
            ny, nx = y + delta[0], x + delta[1]
            if 0 <= ny < self.max_y and 0 <= nx < self.max_x:
                yield self.grid[ny][nx], ny, nx

    def find_parts(self):
        gears = dict()
        for y, line in enumerate(self.grid):
            num, part = 0, None
            for x, ch in enumerate(line):
                if '0' <= ch <= '9':
                    num = 10 * num + (ord(ch) - ord('0'))
                    if not part:
                        for nb, ny, nx in self.neighbours(y, x):
                            if not (('0' <= nb <= '9') or nb == '.'):
                                part = (nb, (ny, nx))
                elif num > 0:
                    if part:
                        self.part_sum += num
                        if part[0] == '*':
                            if v := gears.pop(part[1], None):
                                self.gear_ratio += (v * num)
                            else:
                                gears[part[1]] = num
                    num, part = 0, None


class Dec03(Day, year=2023, day=3):

    @staticmethod
    def parse_instructions(instructions):
        return Schematic(instructions)

    @timer(part=1)
    def part_1(self):
        return self.instructions.part_sum

    @timer(part=2)
    def part_2(self):
        return self.instructions.gear_ratio


if __name__ == '__main__':
    with Timer('Total'):
        Dec03().run_day()
