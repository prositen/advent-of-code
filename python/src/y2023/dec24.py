from python.src.common import Day, timer, Timer


class Hailstone(object):
    def __init__(self, pos, velocity):
        self.pos = pos
        self.vel = velocity
        self.slope = self.vel[1] / self.vel[0]
        self.c = (-self.slope * self.pos[0] + self.pos[1])

    def __repr__(self):
        return f'{str(self.pos)} @ {str(self.vel)}'

    def crosses2d(self, other: 'Hailstone', min_pos, max_pos):
        if self.slope == other.slope:
            return False
        x = (other.c - self.c) / (self.slope - other.slope)
        y = self.slope * x + self.c
        if min_pos <= x <= max_pos and min_pos <= y <= max_pos:
            if (
                    ((x - self.pos[0]) / self.vel[0]) < 1
                    or
                    ((x - other.pos[0]) / other.vel[0]) < 1
            ):
                return False
            return True
        else:
            return False


class Hailstorm(object):

    def __init__(self, hailstones):
        self.hailstones = [Hailstone(*hs) for hs in hailstones]

    def count_intersections(self, min_pos, max_pos):
        return sum(me.crosses2d(other, min_pos=min_pos, max_pos=max_pos) == True
                   for i, me in enumerate(self.hailstones)
                   for other in self.hailstones[i + 1:])

    def group_velocities(self):
        vels = {
            0: dict(),
            1: dict(),
            2: dict()
        }

        for hs in self.hailstones:
            for dim in 0, 1, 2:
                if hs.vel[dim] not in vels[dim]:
                    vels[dim][hs.vel[dim]] = list()
                vels[dim][hs.vel[dim]].append(hs.pos[dim])

        return vels

    def throw_stone(self):
        groups = self.group_velocities()
        rock_vx, rock_vy, rock_vz = self.find_velocity(groups[0]), self.find_velocity(
            groups[1]), self.find_velocity(groups[2])

        (ax, ay, az), (avx, avy, avz) = self.hailstones[0].pos, self.hailstones[0].vel
        (bx, by, bz), (bvx, bvy, bvz) = self.hailstones[1].pos, self.hailstones[1].vel

        slope_a = (avy - rock_vy) / (avx - rock_vx)
        slope_b = (bvy - rock_vy) / (bvx - rock_vx)
        ca = ay - (slope_a * ax)
        cb = by - (slope_b * bx)
        x = ((cb - ca) / (slope_a - slope_b))
        y = (slope_a * x + ca)
        time = (x - ax) / (avx - rock_vx)
        z = az + (avz - rock_vz) * time
        print(x, y, z)
        return x + y + z

    @staticmethod
    def find_velocity(group):
        possible_v = set()
        for velocity, distances in group.items():
            if len(distances) < 2:
                continue
            this_v = set()
            for i, d1 in enumerate(distances):
                for j, d2 in enumerate(distances[i + 1:]):
                    diff = abs(d1 - d2)
                    for pv in range(-500, 500):
                        if pv != velocity and diff % (pv - velocity) == 0:
                            this_v.add(pv)
            if not possible_v:
                possible_v = this_v
            else:
                possible_v.intersection_update(this_v)
        assert (len(possible_v) == 1)
        return possible_v.pop()


class Dec24(Day, year=2023, day=24):

    @staticmethod
    def parse_instructions(instructions):
        return [
            (
                tuple(map(int, (s := row.split('@'))[0].split(','))),
                tuple(map(int, s[1].split(',')))
            )
            for row in instructions
        ]

    @timer(part=1)
    def part_1(self):
        hs = Hailstorm(self.instructions)
        return hs.count_intersections(200000000000000, 400000000000000)

    @timer(part=2)
    def part_2(self):
        hs = Hailstorm(self.instructions)
        return hs.throw_stone()


if __name__ == '__main__':
    with Timer('Total'):
        Dec24().run_day()
