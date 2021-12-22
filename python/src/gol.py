import itertools

from python.src.grid import Grid


class GameOfLife(Grid):

    def __init__(self, stay_alive, new_life, dimensions=2, stay_in_bounds=True,
                 state=None):
        super().__init__(dimensions=dimensions, data_type=bool,
                         stay_in_bounds=stay_in_bounds, state=state)
        self.stay_alive = set(stay_alive)
        self.new_life = set(new_life)
        self.delta.remove((0,) * self.dimensions)

    def count_neighbours(self, pos):
        return sum(self.grid[p] for p in self.neighbours(pos))

    def update_pos(self, pos):
        alive = self.grid[pos]
        neighbours = self.count_neighbours(pos)
        if alive and neighbours not in self.stay_alive:
            return False
        elif not alive and neighbours in self.new_life:
            return True
        else:
            return alive


