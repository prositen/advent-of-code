class SimpleGrid(object):

    def __init__(self, grid_map,
                 walls='#', start='S', end='E'):
        self.max_y = len(grid_map)
        self.max_x = len(grid_map[0])

        self.walls = set()
        self.start = self.end = (0, 0)
        for y, row in enumerate(grid_map):
            for x, cell in enumerate(row):
                if cell == walls:
                    self.walls.add((x, y))
                elif cell == start:
                    self.start = (x, y)
                elif cell == end:
                    self.end = (x, y)
        self.delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def nbs(self, pos):
        for d in self.delta:
            if 0 <= (px := pos[0] + d[0]) < self.max_x and 0 <= (py := pos[1] + d[1]) < self.max_y:
                yield px, py
