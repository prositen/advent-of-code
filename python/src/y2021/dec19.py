import itertools
from collections import deque

from python.src.common import Day, timer, Timer

cos = {
    0: 1,
    90: 0,
    180: -1,
    270: 0
}

sin = {
    0: 0,
    90: 1,
    180: 0,
    270: -1
}


class Beacon(object):
    def __init__(self, pos=None, beacon=None):
        if pos:
            (self.x, self.y, self.z) = pos
        else:
            self.x, self.y, self.z = beacon.x, beacon.y, beacon.z

    @staticmethod
    def from_string(beacon):
        return Beacon(tuple(map(int, beacon.split(','))))

    def rotate_x(self, theta):
        y = self.y * cos[theta] - self.z * sin[theta]
        z = self.y * sin[theta] + self.z * cos[theta]
        self.y, self.z = y, z

    def rotate_y(self, theta):
        x = self.x * cos[theta] + self.z * sin[theta]
        z = self.z * cos[theta] - self.x * sin[theta]
        self.x, self.z = x, z

    def rotate_z(self, theta):
        x = self.x * cos[theta] - self.y * sin[theta]
        y = self.x * sin[theta] + self.y * cos[theta]
        self.x, self.y = x, y

    def rotate(self, x, y, z):
        self.rotate_x(x)
        self.rotate_y(y)
        self.rotate_z(z)
        return self

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __lt__(self, other):
        return (self.x, self.y, self.z) < (other.x, other.y, other.z)

    def __repr__(self):
        return f'<{self.x}, {self.y}, {self.z}>'

    def distance(self, other):
        return (abs(self.x - other.x),
                abs(self.y - other.y), abs(self.z - other.z))


class Scanner(object):
    def __init__(self, beacons):
        self.beacons = [b for b in beacons]
        self.distances = {
            a.distance(b) for a, b in itertools.permutations(self.beacons, 2)
        }

    @staticmethod
    def from_string(instructions):
        return Scanner(beacons=[
            Beacon.from_string(line) for line in instructions
        ])

    def rotations(self):
        for x in (0, 90, 180, 270):
            for y in (0, 90, 180, 270):
                yield Scanner(
                    [Beacon(beacon=b).rotate(x, y, 0) for b in self.beacons]
                )
            for z in (90, 270):
                yield Scanner(
                    [Beacon(beacon=b).rotate(x, 0, z) for b in self.beacons]
                )

    def __eq__(self, other):
        return sorted(self.beacons) == sorted(other.beacons)

    def __repr__(self):
        return f'<Scanner beacons={self.beacons}>'

    def overlaps(self, other):
        a = self.distances.intersection(other.distances)
        return len(a) >= 12


class Dec19(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 19, instructions, filename)
        self.scanners = self.instructions

    @staticmethod
    def parse_instructions(instructions):
        return [Scanner.from_string(group[1:]) for group in Day.parse_groups(instructions)]

    def find_all_beacons(self):
        to_visit = deque()
        reoriented = list()
        reoriented.append(self.scanners[0])
        to_visit.extend(self.scanners[1:])
        while to_visit:
            sc = to_visit.pop()
            for rs in sc.rotations():
                overlaps = [rs.overlaps(other) for other in reoriented]
                if any(overlaps):
                    reoriented.append(rs)
                    break
            else:
                to_visit.append(sc)

        beacons = set()
        self.scanners = reoriented
        for sc in self.scanners:
            for beacon in sc.beacons:
                beacons.add((beacon.x, beacon.y, beacon.z))
        return sorted(Beacon(b) for b in beacons)

    @timer(part=1)
    def part_1(self):
        return 0

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Beacon Scanner'):
        Dec19().run_day()
