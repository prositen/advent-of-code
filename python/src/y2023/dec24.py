from python.src.common import Day, timer, Timer


class Hailstone(object):
    def __init__(self, pos, velocity):
        self.pos = pos
        self.velocity = velocity
        self.slope = self.velocity[1] / self.velocity[0]
        self.c = (-self.slope * self.pos[0] + self.pos[1])

    def __repr__(self):
        return f'{str(self.pos)} @ {str(self.velocity)}'

    def crosses2d(self, other: 'Hailstone', min_pos, max_pos):
        if self.slope == other.slope:
            return False
        x = (other.c - self.c) / (self.slope - other.slope)
        y = self.slope * x + self.c
        if min_pos <= x <= max_pos and min_pos <= y <= max_pos:
            if (
                    ((x - self.pos[0]) / self.velocity[0]) < 1
                    or
                    ((x - other.pos[0]) / other.velocity[0]) < 1
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

    def same_trajectory_in_one_dimension(self):
        for i, me in enumerate(self.hailstones):
            for j, other in enumerate(self.hailstones[i + 1:]):
                for n in (0, 1, 2):
                    if me.pos[n] == other.pos[n] and me.velocity[n] == other.velocity[n]:
                        return n, me.pos[n], me.velocity[n]
        return 0, 0, 0

    def throw_stone(self):
        """
        /u/Mahregell2
        There is a special property again in all inputs completely trivializing the problem,
        but barely anyone found it, that's why we see all those Z3 solutions.

        There are always 2 rocks with a common start coordinate and velocity in one
        dimension. So you know the starting coordinate and velocity of your rock in
        that dimension. Now intersect with any 2 other rocks in that dimension -> 2 points
        in time -> you know everything

        """
        dim, pos, vel = self.same_trajectory_in_one_dimension()
        points = list()
        print(dim, pos, vel)
        for stone in self.hailstones:
            if stone.pos[dim] == pos and stone.velocity[dim] == vel:
                continue

            t = (stone.pos[dim] - pos) / stone.velocity[dim]

            points.append((*stone.pos, t))
            if len(points) == 2:
                break

        print(points)



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
