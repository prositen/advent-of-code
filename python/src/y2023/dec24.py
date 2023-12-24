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
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec24().run_day()
