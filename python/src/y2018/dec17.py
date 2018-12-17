import re
from collections import deque

from python.src.common import Day


class Dec17(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 17, instructions, filename)
        self.spring = (500, 0)
        self.veins = self.instructions
        self.min_x = min(self.veins)[0][0]
        self.max_x = max(self.veins, key=lambda xy: xy[0][1])[0][1]
        self.min_y = min(self.veins, key=lambda xy: xy[1][0])[1][0] - 1
        self.max_y = max(self.veins, key=lambda xy: xy[1][1])[1][1] + 1
        self.grid = self.make_grid()

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
            ['_' for _ in range(self.max_x - self.min_x + 1)]
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

    def fill_water(self):
        to_visit = deque()
        start_x = self.spring[0] - self.min_x
        to_visit.append((0, start_x, start_x, start_x))
        visited = set()
        while to_visit:
            y, x, last_left, last_right = to_visit.pop()
            if y + 1 == len(self.grid):
                continue
            if self.grid[y + 1][x] == '_':
                self.grid[y + 1][x] = '|'
                visited.add((y + 1, x))
                to_visit.append((y + 1, x, last_left, last_right))
            else:
                left_part = self.grid[y][:x][::-1]
                try:
                    left_border = len(left_part) - left_part.index('#')
                except ValueError:
                    left_border = 0

                try:
                    right_border = self.grid[y][x:].index('#') + len(left_part)
                except ValueError:
                    right_border = len(self.grid) - 1

                fill = True
                if self.grid[y + 1][x] != '#':
                    if left_border < last_left:
                        # spill left
                        if last_left > 0:
                            if self.grid[y][last_left-2] == '_':
                                to_visit.append((y, last_left - 2, last_left - 1, last_left))

                        fill_to = min(len(self.grid[y]), last_right+1)
                        fill_from = fill_to - 1
                        while self.grid[y+1][fill_from] in ('#', '~') \
                                and fill_from > 1\
                                and self.grid[y][fill_from-1] != '#':
                            fill_from -= 1
                        self.grid[y][fill_from:fill_to] = '|' * (fill_to - fill_from)
                        fill = False
                    if right_border > last_right:
                        # spill right
                        if last_right < len(self.grid) - 1:
                            if self.grid[y][last_right+1] == '_':
                                to_visit.append((y, last_right + 1, last_right, last_right + 1))
                        fill_from = max(0, last_left)
                        fill_to = fill_from + 1
                        while self.grid[y + 1][fill_to] in ('#', '~') \
                                and fill_to < len(self.grid[y]) - 1\
                                and self.grid[y][fill_to+1] != '#':
                            fill_to += 1

                        self.grid[y][fill_from:fill_to] = '|' * (fill_to - fill_from)
                        fill = False
                if fill:
                    self.grid[y][left_border:right_border] = '~' * (right_border - left_border)
                    for xx in range(left_border, right_border):
                        if self.grid[y + 1][xx] in ('_', '|'):
                            to_visit.append((y, xx, left_border, right_border))
                    to_visit.append((y - 1, x, left_border, right_border))

    def part_1(self):
        self.fill_water()
        self.render_veins()
        water = 0
        for y in self.grid:
            water += y.count('|') + y.count('~')
        return water

    def part_2(self):
        pass


if __name__ == '__main__':
    d = Dec17()
    print("Water reach:", d.part_1())
    print(":", d.part_2())
