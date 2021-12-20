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

    def add(self, x, y, z):
        self.x += x
        self.y += y
        self.z += z
        return z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __lt__(self, other):
        return (self.x, self.y, self.z) < (other.x, other.y, other.z)

    def __repr__(self):
        return f'<{self.x}, {self.y}, {self.z}>'

    def distance(self, other):
        return (self.x - other.x,
                self.y - other.y, self.z - other.z)


class Scanner(object):
    def __init__(self, beacons):
        self.beacons = [b for b in beacons]
        self.x = 0
        self.y = 0
        self.z = 0
        self._distances = dict()

    @property
    def distances(self):
        if not self._distances:
            for i, ba in enumerate(self.beacons):
                for j, bb in enumerate(self.beacons[i + 1:]):
                    self._distances[ba.distance(bb)] = (ba, bb)
        return self._distances

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
        return set(self.distances).intersection(set(other.distances))

    def reorient(self, other):
        overlaps = self.overlaps(other)
        if len(overlaps) > 11:
            ol = overlaps.pop()
            my_pos = self.distances[ol][0]
            their_pos = other.distances[ol][0]
            diff = their_pos.distance(my_pos)
            self.x += diff[0]
            self.y += diff[1]
            self.z += diff[2]
            for b in self.beacons:
                b.add(*diff)
            return True
        return False


class Dec19(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 19, instructions, filename)
        self.scanners = self.instructions
        self.beacons = list()

    @staticmethod
    def parse_instructions(instructions):
        return [Scanner.from_string(group[1:]) for group in Day.parse_groups(instructions)]

    def find_all_beacons(self):
        if not self.beacons:
            to_visit = deque()
            reoriented = list()
            reoriented.append((0, self.scanners[0]))
            to_visit.extend(list(enumerate(self.scanners[1:], start=1)))
            tested = dict()
            while to_visit:
                i, sc = to_visit.popleft()
                found = False
                for j, compare in reoriented:
                    if j in tested.get(i, list()):
                        continue

                    for rs in sc.rotations():
                        if rs.reorient(compare):
                            reoriented.append((i, rs))
                            found = True
                            break
                    tested[i] = tested.get(i, list()) +[j]
                    if found:
                        break
                else:
                    to_visit.append((i, sc))

            beacons = set()
            self.scanners = [sc for (_, sc) in reoriented]
            for sc in self.scanners:
                for beacon in sc.beacons:
                    beacons.add((beacon.x, beacon.y, beacon.z))
            self.beacons = sorted(Beacon(b) for b in beacons)
        return self.beacons

    @timer(part=1)
    def part_1(self):
        return len(self.find_all_beacons())

    @timer(part=2)
    def part_2(self):
        self.find_all_beacons()
        sc = Scanner(beacons=[
            Beacon((sc.x, sc.y, sc.z)) for sc in self.scanners
        ])
        return max((abs(d[0])+abs(d[1])+abs(d[2])) for d in sc.distances.keys())


if __name__ == '__main__':
    with Timer('Beacon Scanner'):
        Dec19().run_day()
