import re

from python.src.common import Day


class Moon(object):
    def __init__(self, x, y, z):
        self.p = [int(x, 10), int(y, 10), int(z, 10)]
        self.v = [0, 0, 0]

    def apply_gravity(self, moon):
        for i in 0, 1, 2:
            self.v[i] += -1 if self.p[i] > moon.p[i] else 0 if self.p[i] == moon.p[i] else 1

    def apply_velocity(self):
        for i in 0, 1, 2:
            self.p[i] += self.v[i]

    def get(self):
        return tuple(self.p), tuple(self.v)

    def get_dim(self, dim):
        return "{},{},".format(self.p[dim], self.v[dim])

    def get_energy(self):
        return sum(abs(p) for p in self.p) * sum(abs(v) for v in self.v)


def lcm(x, y):
    from math import gcd
    return x * y // gcd(x, y)


class Dec12(Day):
    def __init__(self, filename=None, instructions=None):
        super().__init__(2019, 12, instructions, filename)
        self.moons = [Moon(*i) for i in self.instructions]
        self.states = ["", "", ""]
        for i in 0, 1, 2:
            self.states[i] = ",".join(self.moons[j].get_dim(i) for j in (0, 1, 2))
        self.period = [0, 0, 0]
        self.steps = 0

    @staticmethod
    def parse_instructions(instructions):
        re_coords = re.compile(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)')
        i = list()
        for row in instructions:
            result = re_coords.match(row)
            i.append(result.groups())
        return i

    def part_1(self):
        self.simulate(1000)
        return self.get_energy()

    def part_2(self):
        while 0 in self.period:
            self.simulate(100)
        return lcm(lcm(self.period[0], self.period[1]), self.period[2])

    def simulate(self, steps):
        for _ in range(steps):
            self.steps += 1
            for m in self.moons:
                for n in self.moons:
                    m.apply_gravity(n)
            for m in self.moons:
                m.apply_velocity()
            for i in 0, 1, 2:
                if self.period[i] == 0:
                    state = ",".join(self.moons[j].get_dim(i) for j in (0, 1, 2))
                    if state == self.states[i]:
                        self.period[i] = self.steps

    def get_energy(self):
        return sum(m.get_energy() for m in self.moons)


if __name__ == '__main__':
    d = Dec12()
    print("Part 1:", d.part_1())
    print("Part 2:", d.part_2())
