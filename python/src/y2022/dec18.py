from python.src.common import Day, timer, Timer


class LavaGrid(object):
    def __init__(self, droplets):
        self.grid = dict()
        self.x = dict()
        self.y = dict()
        self.z = dict()
        for (x, y, z) in droplets:
            self.grid[(x, y, z)] = True
            self.z[x] = self.z.get(x, set()).union(y)
            self.y[x] = self.y.get(x, set()).union(z)
            self.x[y] = self.x.get(y, set()).union(z)
        s_x = sorted((x for x, _, _ in droplets))
        s_y = sorted((y for _, y, _ in droplets))
        s_z = sorted((z for _, _, z in droplets))
        self.min_x, self.max_x = s_x[0], s_x[-1]
        self.min_y, self.max_y = s_y[0], s_y[-1]
        self.min_z, self.max_z = s_z[0], s_z[-1]

    def count_faces(self):
        print()
        print(self.x)
        print(self.y)
        print(self.z)



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
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec18().run_day()
