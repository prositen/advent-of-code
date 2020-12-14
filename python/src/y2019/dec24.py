import itertools

from python.src.common import Day, timer, Timer


class Dec24(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2019, 24, instructions, filename)
        self.grid = dict()
        for y, row in enumerate(self.instructions):
            for x, col in enumerate(row):
                self.grid[(y, x)] = col
        self.max_x = 5
        self.max_y = 5

    def get_biodiversity(self):
        return sum(2 ** i for i, c in enumerate(self.grid.values()) if c == '#')

    def pos(self, row, col):
        if 0 <= row < self.max_y and 0 <= col < self.max_x:
            return self.grid[(row, col)]
        return '.'

    def count_neighbours(self, row, col):
        c = 0
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            c += self.pos(row + dy, col + dx) == '#'
        return c

    def step(self):
        new_layout = dict()
        for y in range(self.max_y):
            for x in range(self.max_x):
                neighbours = self.count_neighbours(y, x)
                col = self.pos(y, x)
                if col == '#' and neighbours != 1:
                    new_layout[(y, x)] = '.'
                elif col == '.' and neighbours in (1, 2):
                    new_layout[(y, x)] = '#'
                else:
                    new_layout[(y, x)] = col
        self.grid = new_layout

    def print(self):
        print('\n'.join(self.instructions))
        print('\n\n')

    @timer(part=1)
    def part_1(self):
        seen = set()
        while True:
            bd = self.get_biodiversity()
            if bd in seen:
                return bd
            seen.add(bd)
            self.step()

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        d = Dec24()
        d.part_1()
        d.part_2()
