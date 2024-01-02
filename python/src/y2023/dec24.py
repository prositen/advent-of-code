import itertools
import math

from python.src.common import Day, timer, Timer


class Hailstone(object):
    def __init__(self, pos, velocity):
        self.pos = pos
        self.vel = velocity
        if self.vel[0] != 0:
            self.slope = self.vel[1] / self.vel[0]
            self.c = (-self.slope * self.pos[0] + self.pos[1])
        else:
            self.slope = None
            self.c = None

    def __repr__(self):
        return f'{str(self.pos)} @ {str(self.vel)}'

    def crosses2d(self, other: 'Hailstone', dim_0=0, dim_1=1):
        det = self.vel[dim_0] * other.vel[dim_1] - self.vel[dim_1] * other.vel[dim_0]
        if det == 0:
            return None

        b0 = self.vel[dim_0] * self.pos[dim_1] - self.vel[dim_1] * self.pos[dim_0]
        b1 = other.vel[dim_0] * other.pos[dim_1] - other.vel[dim_1] * other.pos[dim_0]

        x = (other.vel[dim_0] * b0 - self.vel[dim_0] * b1) / det
        y = (other.vel[dim_1] * b0 - self.vel[dim_1] * b1) / det
        return x, y

    def __sub__(self, other):
        pos = (self.pos[0] - other.pos[0], self.pos[1] - other.pos[1], self.pos[2] - other.pos[2])
        vel = (self.vel[0] - other.vel[0], self.vel[1] - other.vel[1], self.vel[2] - other.vel[2])
        return Hailstone(pos=pos, velocity=vel)


class Hailstorm(object):

    def __init__(self, hailstones):
        self.hailstones = [Hailstone(*hs) for hs in hailstones]

    @staticmethod
    def in_range(pos, min_pos, max_pos):
        if not pos:
            return False
        return min_pos <= pos[0] <= max_pos and min_pos <= pos[1] <= max_pos

    @staticmethod
    def in_future(hailstone: Hailstone, pos):
        if not pos:
            return False
        return math.copysign(1, pos[0] - hailstone.pos[0]) == math.copysign(1, hailstone.vel[0])

    def count_intersections(self, min_pos, max_pos):
        return sum(
            self.in_range(pos, min_pos, max_pos) and self.in_future(me, pos) and self.in_future(
                other, pos)
            for i, me in enumerate(self.hailstones)
            for other in self.hailstones[i + 1:]
            for pos in (me.crosses2d(other),))

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
        # Find rocks that are moving in the same velocity in one dimension.
        groups = self.group_velocities()

        # Using the above, brute-force through possible velocities until we find one
        # that would make it possible to hit all rocks with the same velocity
        # On my input, there's only one possible velocity per dimension
        # The test input doesn't have the same constraint, thus the loop.
        rock_vxs, rock_vys, rock_vzs = (self.find_velocity(groups[0]),
                                        self.find_velocity(groups[1]),
                                        self.find_velocity(groups[2]))

        # Now pick any two hailstones and figure out where we need to start to hit both
        # of them with the  given velocities.
        for rock_vx, rock_vy, rock_vz in itertools.product(rock_vxs, rock_vys, rock_vzs):
            rel_a = self.hailstones[0] - Hailstone(pos=(0, 0, 0),
                                                   velocity=(rock_vx, rock_vy, rock_vz))
            rel_b = self.hailstones[1] - Hailstone(pos=(0, 0, 0),
                                                   velocity=(rock_vx, rock_vy, rock_vz))

            pos_xy = rel_a.crosses2d(rel_b)
            pos_xz = rel_a.crosses2d(rel_b, dim_0=0, dim_1=2)
            if pos_xy[0] == pos_xz[0]:
                return int(pos_xy[0] + pos_xy[1] + pos_xz[1])

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
                        # The relative distance of the rock (pv - velocity)
                        # must perfectly divide the distance between the rocks
                        if pv != velocity and diff % (pv - velocity) == 0:
                            this_v.add(pv)
            if not possible_v:
                possible_v = this_v
            else:
                possible_v.intersection_update(this_v)

        return possible_v


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
