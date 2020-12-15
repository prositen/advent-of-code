import itertools

from python.src.common import Day, timer, Timer


class Dec24(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2019, 24, instructions, filename)
        self.grids = dict()
        self.reset_grid()
        self.max_x = 5
        self.max_y = 5

    def reset_grid(self):
        self.grids = dict()
        self.grids[0] = dict()
        for y, row in enumerate(self.instructions):
            for x, col in enumerate(row):
                self.grids[0][(y, x)] = col == '#'

    def get_biodiversity(self):
        return sum(2 ** i for i, c in enumerate(self.grids[0].values()) if c)

    def pos(self, row, col, level=0):
        if level in self.grids:
            if 0 <= row < self.max_y and 0 <= col < self.max_x:
                return self.grids[level][(row, col)]
        return False

    def count_neighbours(self, row, col):
        c = 0
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            c += self.pos(row + dy, col + dx)
        return c

    def step(self):
        new_layout = dict()
        for y in range(self.max_y):
            for x in range(self.max_x):
                neighbours = self.count_neighbours(y, x)
                bug = self.pos(y, x)
                if bug and neighbours != 1:
                    new_layout[(y, x)] = False
                elif not bug and neighbours in (1, 2):
                    new_layout[(y, x)] = True
                else:
                    new_layout[(y, x)] = bug
        self.grids[0] = new_layout

    def count_recursive_neighbours(self, row, col, level):
        c = 0
        neighbours = []
        # Look up
        if row == 0:
            neighbours.append((1, 2, level - 1))
        elif (row, col) == (3, 2):
            neighbours.extend([(4, x, level + 1) for x in range(5)])
        else:
            neighbours.append((row - 1, col, level))

        # Look down
        if row == 4:
            neighbours.append((3, 2, level - 1))
        elif (row, col) == (1, 2):
            neighbours.extend([(0, x, level + 1) for x in range(5)])
        else:
            neighbours.append((row + 1, col, level))

        # Look left
        if col == 0:
            neighbours.append((2, 1, level - 1))
        elif (row, col) == (2, 3):
            neighbours.extend([(y, 4, level + 1) for y in range(5)])
        else:
            neighbours.append((row, col - 1, level))

        # Look right
        if col == 4:
            neighbours.append((2, 3, level - 1))
        elif (row, col) == (2, 1):
            neighbours.extend([(y, 0, level + 1) for y in range(5)])
        else:
            neighbours.append((row, col + 1, level))

        count = sum(self.pos(*n) for n in neighbours)
        return count

    def step_recursive(self):
        new_grids = dict()
        min_level, max_level = min(self.grids.keys()), max(self.grids.keys())
        for level in range(min_level - 1, max_level + 2):
            grid_level = {
                (2, 2): False
            }
            for y in range(self.max_y):
                for x in range(self.max_x):
                    if (y, x) != (2, 2):
                        neighbours = self.count_recursive_neighbours(
                            row=y, col=x, level=level
                        )
                        bug = self.pos(y, x, level)
                        if bug and neighbours != 1:
                            grid_level[(y, x)] = False
                        elif not bug and neighbours in (1, 2):
                            grid_level[(y, x)] = True
                        else:
                            grid_level[(y, x)] = bug
            new_grids[level] = grid_level
        self.grids = new_grids

    def count_bugs(self, level):
        return sum(self.grids.get(level, dict()).values())

    @timer(part=1)
    def part_1(self):
        seen = set()
        while True:
            if (bd := self.get_biodiversity()) in seen:
                return bd
            seen.add(bd)
            self.step()

    def print(self, level):
        print(f'Level {level}')
        for y in range(self.max_y):
            print(''.join('#' if self.pos(y, x, level) else '.' for x in range(self.max_x)))
        print()

    def run(self, minutes):
        for i in range(minutes):
            self.step_recursive()
        return sum(self.count_bugs(level) for level in self.grids)

    @timer(part=2)
    def part_2(self):
        self.reset_grid()
        return self.run(200)


if __name__ == '__main__':
    with Timer('Total'):
        d = Dec24()
        d.part_1()
        d.part_2()
