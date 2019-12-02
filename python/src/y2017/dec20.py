import os
import re
from python.src.y2017.common import DATA_DIR

re_VECTOR = re.compile(
    r'p=<( ?-?\d+),( ?-?\d+),(-?\d+)>, '
    r'v=<( ?-?\d+),( ?-?\d+),( ?-?\d+)>, '
    r'a=<( ?-?\d+),( ?-?\d+),( ?-?\d+)>')


class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __repr__(self):
        return "<{},{},{}>".format(self.x, self.y, self.z)

    def hash(self):
        return self.x, self.y, self.z


class Particle(object):
    def __init__(self, p1, p2, p3, v1, v2, v3, a1, a2, a3):
        self.p = Vector(p1, p2, p3)
        self.v = Vector(v1, v2, v3)
        self.a = Vector(a1, a2, a3)
        self.number = 0
        self.closest = self.distance()

    def update(self):
        self.v += self.a
        self.p += self.v
        self.closest = min(self.closest, self.distance())

    def distance(self):
        return abs(self.p.x) + abs(self.p.y) + abs(self.p.z)

    def __repr__(self):
        return "p={}, v={}, a={}".format(self.p, self.v, self.a)


class Swarm(object):
    def __init__(self, puzzle_input):
        self.particles = [self.parse_line(line) for line in puzzle_input]
        for i, p in enumerate(self.particles):
            p.number = i
        self.tick_count = 0

    @staticmethod
    def parse_line(line):
        r = re.match(re_VECTOR, line)
        if r:
            g = [int(x) for x in r.groups()]
            return Particle(*g)
        else:
            print(line)

    def tick(self, collide=False):
        positions = {}
        to_remove = []
        for i, p in enumerate(self.particles):
            p.update()
            hp = str(p.p)
            if hp in positions:
                to_remove += [i, positions[hp]]
            positions[hp] = i
        if collide:
            self.particles = [p for i, p in enumerate(self.particles) if i not in to_remove]
        self.tick_count += 1

    def __len__(self):
        return len(self.particles)

    def distances(self):
        return [x.number for x in sorted(self.particles, key=lambda x: x.distance())]

    def get_closest(self):
        closest = self.distances()
        while self.tick_count < 2:
            prev_closest = closest
            self.tick()
            closest = self.distances()
            if prev_closest != closest:
                self.tick_count = 0
        return closest[0]

    def get_particle_count(self):
        particle_count = len(self)
        while self.tick_count < 10:
            self.tick(collide=True)
            last_count = particle_count
            particle_count = len(self)
            if particle_count != last_count:
                self.tick_count = 0
        return particle_count


def main():
    with open(os.path.join(DATA_DIR, 'input.20.txt')) as fh:
        puzzle_input = fh.readlines()

    s = Swarm(puzzle_input)
    print("Part 1:", s.get_closest())

    s = Swarm(puzzle_input)
    print("Part 2:", s.get_particle_count())


if __name__ == '__main__':
    main()
