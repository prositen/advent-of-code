from python.src.common import Day, timer, Timer


class Cube(object):
    def __init__(self, x, y, z, limited=False, number=0):
        self.x = x
        self.y = y
        self.z = z
        self.limited = limited
        if self.limited:
            self.x = max(x[0], -50), min(x[1], 51)
            self.y = max(y[0], -50), min(y[1], 51)
            self.z = max(z[0], -50), min(z[1], 51)

        self.contains = list()
        self.number = number

    def volume(self):
        return ((self.x[1] - self.x[0] + 1) *
                (self.y[1] - self.y[0] + 1) *
                (self.z[1] - self.z[0] + 1)
                - sum(c.volume() for c in self.contains)
                )

    @staticmethod
    def line_intersects(m, n):
        return (m[0] <= n[0] <= m[1] or
                m[0] <= n[1] <= m[1] or
                n[0] <= m[0] <= n[1] or
                n[0] <= m[1] <= n[1])

    @staticmethod
    def get_overlap(m, n):
        return max(m[0], n[0]), min(m[1], n[1])

    def intersects(self, other):
        return (self.line_intersects(self.x, other.x) and
                self.line_intersects(self.y, other.y) and
                self.line_intersects(self.z, other.z))

    def contain(self, other):
        if self.intersects(other):
            xr = self.get_overlap(self.x, other.x)
            yr = self.get_overlap(self.y, other.y)
            zr = self.get_overlap(self.z, other.z)

            intersecting_cube = Cube(xr, yr, zr, self.limited, other.number)
            if not intersecting_cube.empty():
                for cube in self.contains:
                    cube.contain(intersecting_cube)
                self.contains.append(intersecting_cube)

    def empty(self):
        return self.x[1] < self.x[0] or self.y[1] < self.y[0] or self.z[1] < self.z[0]

    def __repr__(self):
        return f'<Cube {self.number}: {self.x} {self.y} {self.z}>'


class Reactor2(object):
    def __init__(self, instructions, limited=False):
        self.limited = limited
        self.reboot_instructions = instructions
        self.cubes = list()

    def boot(self):
        for i, (on, (x, y, z)) in enumerate(self.reboot_instructions):
            c = Cube(x, y, z, self.limited, i)
            if not c.empty():
                for other in self.cubes:
                    other.contain(c)
                if on:
                    self.cubes.append(c)

    def volume(self):
        return sum(cube.volume() for cube in self.cubes)


class Dec22(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 22, instructions=instructions, filename=filename)

    @staticmethod
    def parse_instructions(instructions):
        ins = list()
        for line in instructions:
            on, dimensions = line.split(' ')
            on = (on == "on")
            dimensions = tuple(
                (int((dd := d.split('..'))[0][2:]),
                 int(dd[1]))
                for d in dimensions.split(',')
            )
            ins.append((on, dimensions))
        return ins

    @timer(part=1)
    def part_1(self):
        reactor = Reactor2(instructions=self.instructions, limited=True)
        reactor.boot()
        return reactor.volume()

    @timer(part=2)
    def part_2(self):
        reactor = Reactor2(instructions=self.instructions)
        reactor.boot()
        return reactor.volume()


if __name__ == '__main__':
    with Timer('Reactor Reboot'):
        Dec22().run_day()
