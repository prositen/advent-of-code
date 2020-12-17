import itertools
import operator
from collections import defaultdict
from functools import cache


class GameOfLife(object):

    def __init__(self, stay_alive, new_life, dimensions=2):
        self.stay_alive = stay_alive
        self.new_life = new_life
        self.dimensions = dimensions
        self.grid = defaultdict(bool)
        self.delta = list(itertools.product((-1, 0, 1), repeat=self.dimensions))

    def set(self, state):
        self.grid = defaultdict(bool, state)

    @cache
    def at(self, pos):
        return self.grid[pos]

    def count_neighbours(self, pos):
        n = 0
        for delta in self.delta:
            new_pos = tuple(map(operator.add, pos, delta))
            if new_pos != pos:
                n += self.at(new_pos)
        return n

    def update_pos(self, pos):
        alive = self.at(pos)
        neighbours = self.count_neighbours(pos)
        if alive and neighbours not in self.stay_alive:
            return False
        elif not alive and neighbours in self.new_life:
            return True
        else:
            return alive

    def step(self, steps=1):
        for _ in range(steps):
            self.at.cache_clear()
            next_grid = defaultdict(bool)
            for pos in list(self.grid):
                next_grid[pos] = self.update_pos(pos)
            for pos in set(self.grid) - set(next_grid):
                next_grid[pos] = self.update_pos(pos)

            self.grid = next_grid

    def count(self):
        return sum(self.grid.values())
