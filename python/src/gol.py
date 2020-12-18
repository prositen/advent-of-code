import itertools
import operator
from collections import defaultdict


class GameOfLife(object):

    def __init__(self, stay_alive, new_life, dimensions=2, stay_in_bounds=True):
        self.stay_alive = set(stay_alive)
        self.new_life = set(new_life)
        self.dimensions = dimensions
        self.grid = defaultdict(bool)
        self.stay_in_bounds = stay_in_bounds
        self.delta = list(itertools.product((-1, 0, 1), repeat=self.dimensions))
        self.delta.remove((0,) * self.dimensions)

    def set(self, state):
        self.grid = defaultdict(bool, state)

    def at(self, pos):
        return self.grid[pos]

    def count_neighbours(self, pos):
        n = 0
        for delta in self.delta:
            n += self.grid[tuple(map(operator.add, pos, delta))]
        return n

    def update_pos(self, pos):
        alive = self.grid[pos]
        neighbours = self.count_neighbours(pos)
        if alive and neighbours not in self.stay_alive:
            return False
        elif not alive and neighbours in self.new_life:
            return True
        else:
            return alive

    def step(self, steps=1):
        for _ in range(steps):
            next_grid = defaultdict(bool)
            for pos in list(self.grid):
                next_grid[pos] = self.update_pos(pos)
            if not self.stay_in_bounds:
                for pos in set(self.grid) - set(next_grid):
                    next_grid[pos] = self.update_pos(pos)

            self.grid = next_grid

    def count(self):
        return sum(self.grid.values())
