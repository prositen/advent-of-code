import itertools
import operator
from collections import defaultdict


class Grid(object):

    def __init__(self, dimensions=2, data_type=bool, stay_in_bounds=True, state=None):
        self.dimensions = dimensions
        self.data_type = data_type
        self.delta = list(itertools.product((-1, 0, 1), repeat=self.dimensions))
        self.grid = defaultdict(self.data_type)
        if state:
            self.set(state)
        self.stay_in_bounds = stay_in_bounds

    def at(self, pos):
        return self.grid[pos]

    def set(self, grid_state):
        self.grid = defaultdict(self.data_type, grid_state)

    def neighbours(self, pos):
        for delta in self.delta:
            yield tuple(map(operator.add, pos, delta))

    def update_pos(self, pos):
        return self.grid[pos]

    def step(self, steps=1):
        for _ in range(steps):
            next_grid = defaultdict(self.data_type)
            for pos in list(self.grid):
                next_grid[pos] = self.update_pos(pos)
            if not self.stay_in_bounds:
                for pos in set(self.grid) - set(next_grid):
                    next_grid[pos] = self.update_pos(pos)

            self.grid = next_grid
