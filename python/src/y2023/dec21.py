from python.src.common import Day, timer, Timer


class Farm(object):
    def __init__(self, farm_map):
        self.max_dim = len(farm_map)
        assert (self.max_dim == len(farm_map[0]))
        self.start = (0, 0)
        for y, row in enumerate(farm_map):
            if 'S' in row:
                self.start = (y, row.index('S'))

        self.tiles = {(y, x) for y, row in enumerate(farm_map)
                      for x, c in enumerate(row) if c in '.S'}
        self.count = {0: 1, -1: 0}
        self.visited = {self.start}
        self.next_step = {self.start}

    def move(self, max_steps):
        delta = (-1, 0), (1, 0), (0, -1), (0, 1)
        for step in range(max(self.count), max_steps):
            self.visited, self.next_step = self.next_step, {
                (ny, nx)
                for (y, x) in self.next_step
                for (dy, dx) in delta
                for (ny, nx) in ((y + dy, x + dx),)
                if
                (ny, nx) not in self.visited and (
                    ny % self.max_dim, nx % self.max_dim) in self.tiles
            }
            self.count[step + 1] = len(self.next_step) + self.count[step - 1]

        return self.count[max_steps]

    def calculate(self, max_steps):
        # I barely understand this myself...
        # We know that the input contains a corridor to the edges from the starting point
        # so with 'm' steps we can move to the edge of the first farm
        #
        d, m = divmod(max_steps, self.max_dim)
        assert m == self.start[0]

        # With three known datapoints we can use the Lagrange Interpolation formula to calculate
        # the result (given that the growth is quadratic)
        #
        # f(x) = the number of spaces we can reach after getting to the edge of farm no x
        #
        xs = (0, 1, 2)
        ys = tuple(self.move(max_steps=m + x * self.max_dim) for x in xs)

        #              (x-x1)(x-x2)           (x-x0)(x-x2)          (x-x0)(x-x1)
        # f(x) =  y0 * -------------  + y1 * --------------  + y2 * ------------
        #             (x0-x1)(x0-x2)         (x1-x0)(x1-x2)        (x2-x0)(x2-x1)
        #
        f_x = ys[0] * (d - xs[1]) * (d - xs[2]) // ((xs[0] - xs[1]) * (xs[0] - xs[2]))
        f_x += ys[1] * (d - xs[0]) * (d - xs[2]) // ((xs[1] - xs[0]) * (xs[1] - xs[2]))
        f_x += ys[2] * (d - xs[0]) * (d - xs[1]) // ((xs[2] - xs[0]) * (xs[2] - xs[1]))

        return f_x


class Dec21(Day, year=2023, day=21):

    @timer(part=1)
    def part_1(self):
        return Farm(self.instructions).move(max_steps=64)

    @timer(part=2)
    def part_2(self):
        """
        628206330073385

        :return:
        """

        return Farm(self.instructions).calculate(max_steps=26501365)


if __name__ == '__main__':
    with Timer('Total'):
        Dec21().run_day()
