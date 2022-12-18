from python.src.common import Day, timer, Timer
from python.src.grid import Grid


class LavaGrid(Grid):
    def __init__(self, droplets):
        super().__init__(stay_in_bounds=True, dimensions=3, data_type=int)
        self.x = dict()
        self.y = dict()
        self.z = dict()
        self.droplets = droplets
        self.delta = [(-1, 0, 0), (0, -1, 0), (0, 0, -1),
                      (1, 0, 0), (0, 1, 0), (0, 0, 1)]
        for (x, y, z) in droplets:
            self.grid[(x, y, z)] = 1
        s_x = sorted((x for x, _, _ in droplets))
        s_y = sorted((y for _, y, _ in droplets))
        s_z = sorted((z for _, _, z in droplets))
        self.min_x, self.max_x = s_x[0], s_x[-1]
        self.min_y, self.max_y = s_y[0], s_y[-1]
        self.min_z, self.max_z = s_z[0], s_z[-1]
        for x in range(self.min_x - 1, self.max_x + 2):
            for y in range(self.min_y - 1, self.max_y + 2):
                for z in range(self.min_z - 1, self.max_z + 2):
                    _ = self.at((x, y, z))

    def count_faces(self, facing=0):
        return sum(self.grid.get(s, 0) == facing
                   for pos in self.droplets
                   for s in self.neighbours(pos)
                   )

    def update_pos(self, pos):
        if self.at(pos) == 1:
            return 1
        if any(self.at(n) == 2 for n in self.neighbours(pos)):
            return 2
        return self.at(pos)

    def find_contained_blocks(self):
        s = 0
        self.grid[(self.min_x, self.min_y, self.min_z)] = 2
        while s != self.count():
            s = self.count()
            self.step()

        return self.count_faces(facing=2)


class Dec18(Day, year=2022, day=18):

    @staticmethod
    def parse_instructions(instructions):
        return [
            tuple(map(int, line.split(',')))
            for line in instructions
        ]

    @timer(part=1)
    def part_1(self):
        return LavaGrid(self.instructions).count_faces()

    @timer(part=2)
    def part_2(self):
        return LavaGrid(self.instructions).find_contained_blocks()


if __name__ == '__main__':
    with Timer('Total'):
        Dec18().run_day()
