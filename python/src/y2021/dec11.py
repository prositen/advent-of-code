from collections import deque

from python.src.common import Day, timer, Timer
from python.src.grid import Grid


class OctopusCave(Grid):

    def __init__(self, state):
        super().__init__(state=state)

    def update_pos(self, pos):
        return self.grid[pos] + 1

    def step(self, steps=1):
        flash_count = 0
        for _ in range(steps):
            to_flash = deque()
            flashed = set()
            super().step(steps=1)
            for pos in list(self.grid):
                if self.grid[pos] > 9:
                    to_flash.append(pos)

            while to_flash:
                pos = to_flash.pop()
                val = self.grid[pos]
                if val > 9 and pos not in flashed:
                    for n in self.neighbours(pos):
                        if n in self.grid:
                            self.grid[n] = self.update_pos(n)
                            if self.grid[n] > 9:
                                to_flash.append(n)
                flashed.add(pos)
            flash_count += len(flashed)
            for pos in flashed:
                self.grid[pos] = 0
        return flash_count


class Dec11(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 11, instructions=instructions, filename=filename)

    def make_grid(self):
        grid = dict()
        for y, line in enumerate(self.instructions):
            for x, char in enumerate(line):
                grid[(y, x)] = int(char)
        return grid

    @timer(part=1)
    def part_1(self):
        cave = OctopusCave(state=self.make_grid())
        return cave.step(100)

    @timer(part=2)
    def part_2(self):
        cave = OctopusCave(state=self.make_grid())
        s = len(cave.grid)
        steps = 1
        while cave.step() < s:
            steps += 1
        return steps


if __name__ == '__main__':
    with Timer('Dumbo Octopus'):
        Dec11().run_day()
