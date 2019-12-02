import re

from python.src.common import Day


class Dec17(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 17, instructions, filename)
        self.spring = (500, 0)
        self.veins = self.instructions
        self.min_x = min(self.veins)[0][0] - 1
        self.max_x = max(self.veins, key=lambda xy: xy[0][1])[0][1]
        self.min_y = min(self.veins, key=lambda xy: xy[1][0])[1][0] - 1
        self.max_y = max(self.veins, key=lambda xy: xy[1][1])[1][1] + 1
        self.grid = self.make_grid()
        self.fill_water()
        self.running_water = 0
        self.still_water = 0
        for y in self.grid:
            self.running_water += y.count('|')
            self.still_water += y.count('~')

    @staticmethod
    def parse_instructions(instructions):
        re_scan = re.compile(r'\d+')
        veins = list()
        x, y = None, None
        for row in instructions:
            for coord in row.split(' '):
                numbers = list(map(int, re_scan.findall(coord)))
                if len(numbers) == 1:
                    numbers += numbers
                if coord[0] == 'x':
                    x = numbers
                else:
                    y = numbers
            veins.append((x, y))
        return veins

    def make_grid(self):
        grid = [
            ['_' for _ in range(self.max_x - self.min_x + 2)]
            for _ in range(self.max_y - self.min_y)]
        for vein in self.veins:
            for y in range(vein[1][0], vein[1][1] + 1):
                for x in range(vein[0][0], vein[0][1] + 1):
                    grid[y - self.min_y][x - self.min_x] = '#'
        grid[self.spring[1]][self.spring[0] - self.min_x] = '+'
        return grid

    def render_veins(self):
        for y in range(len(self.grid)):
            print('{:>4}: {}'.format(y, ''.join(self.grid[y])))

    def probe_down(self, x, y):
        while (y + 1) < len(self.grid) and \
                self.grid[y + 1][x] == self.SAND:
            self.grid[y][x] = '|'
            y += 1
        if y + 1 == len(self.grid):
            self.grid[y][x] = '|'
            return False
        self.grid[y][x] = '|'
        while self.grid[y + 1][x] in self.STOPS_WATER:
            (left, fill_left) = self.probe_left(x - 1, y)
            (right, fill_right) = self.probe_right(x + 1, y)
            if fill_left and fill_right:
                self.grid[y][left + 1:right] = '~' * (right - left - 1)
            y -= 1

    SAND = '_'
    STOPS_WATER = ('~', '#')

    def probe_left(self, x, y):
        while x > 0 and \
                self.grid[y + 1][x] in self.STOPS_WATER and \
                self.grid[y][x] not in self.STOPS_WATER:
            self.grid[y][x] = '|'
            x -= 1
        if x < 0:
            return 0, False
        if self.grid[y][x] in self.STOPS_WATER:
            return x, True
        else:
            self.grid[y][x] = '|'
            return x, self.probe_down(x, y + 1)

    def probe_right(self, x, y):
        while x + 1 < len(self.grid[y]) and \
                self.grid[y + 1][x] in self.STOPS_WATER and \
                self.grid[y][x] not in self.STOPS_WATER:
            self.grid[y][x] = '|'
            x += 1
        if x + 1 == len(self.grid[y]):
            return x, False
        if self.grid[y][x] in self.STOPS_WATER:
            return x, True
        else:
            self.grid[y][x] = '|'
            return x, self.probe_down(x, y + 1)

    def fill_water(self):
        x, y = tuple(self.spring)
        self.probe_down(x - self.min_x, y + 1)

    def part_1(self):
        return self.running_water + self.still_water

    def part_2(self):
        return self.still_water


if __name__ == '__main__':
    d = Dec17()
    print("Water reach:", d.part_1())
    print("Still water:", d.part_2())
