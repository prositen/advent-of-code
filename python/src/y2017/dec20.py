import os
import re

re_VECTOR = re.compile(
    r'p=<( ?-?\d+),( ?-?\d+),(-?\d+)>, v=<( ?-?\d+),( ?-?\d+),( ?-?\d+)>, a=<( ?-?\d+),( ?-?\d+),( ?-?\d+)>')

from python.src.y2017.common import DATA_DIR


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

    def parse_line(self, line):
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
            if str(p.p) in positions:
                to_remove.append(i)
                to_remove.append(positions[str(p.p)])
            positions[str(p.p)] = i
        if collide:
            self.particles = [p for i, p in enumerate(self.particles) if i not in to_remove]

    def __len__(self):
        return len(self.particles)

    def distances(self):
        return [x.number for x in sorted(self.particles, key=lambda x: x.distance())]


def main():
    with open(os.path.join(DATA_DIR, 'input.20.txt')) as fh:
        puzzle_input = fh.readlines()
    # puzzle_input = ["p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>",
    #                "p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>"]
    """
    puzzle_input = ["p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>",
                    "p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>",
                    "p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>",
                    "p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>"
                    ]
    """
    s = Swarm(puzzle_input)

    prev_closest, closest = -1, 0
    while prev_closest != closest:
        prev_closest = closest
        s.tick()
        closest = s.distances()
    print("Part 1:", closest[0])

    s = Swarm(puzzle_input)
    particle_count = len(s)
    tick_count = 0
    while True:
        s.tick(collide=True)
        last_count = particle_count
        particle_count = len(s)
        if particle_count != last_count:
            tick_count = 0
        tick_count += 1
        if tick_count > 30:
            break
    print("Part 2:", len(s.particles))


if __name__ == '__main__':
    main()
