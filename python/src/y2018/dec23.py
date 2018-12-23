import re

from python.src.common import Day


class Dec23(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 23, instructions, filename)
        self.nanobots = [((i[0], i[1], i[2]), i[3]) for i in self.instructions]

    @staticmethod
    def parse_instructions(instructions):
        re_int = re.compile(r'(-?\d+)')
        return [
            list(map(int, re_int.findall(line)))
            for line in instructions
        ]

    def part_1(self):
        strongest = max(self.nanobots, key=lambda nb: nb[1])
        within_radius = [nb for nb in self.nanobots if md(nb[0], strongest[0]) <= strongest[1]]
        return len(within_radius)

    def part_2(self):
        # Let's try a binary search
        x_range = [nb[0][0] for nb in self.nanobots]
        y_range = [nb[0][1] for nb in self.nanobots]
        z_range = [nb[0][2] for nb in self.nanobots]
        x_range, y_range, z_range = ((max(l), min(l)) for l in (x_range, y_range, z_range))

        skip = 1
        while skip < max(x_range) - min(x_range):
            skip *= 2
        while True:
            position = (0, 0, 0)
            distance = 0
            bot_count = 0
            for x in range(min(x_range), max(x_range) + 1, skip):
                for y in range(min(y_range), max(y_range) + 1, skip):
                    for z in range(min(z_range), max(z_range) + 1, skip):
                        count = 0
                        for nb in self.nanobots:
                            if md((x, y, z), nb[0]) < nb[1]:
                                count += 1
                        if count < bot_count:
                            continue
                        to_zero = md((x, y, z), (0, 0, 0))
                        if count > bot_count or distance > to_zero:
                            bot_count = count
                            position = (x, y, z)
                            distance = to_zero
            if skip == 1:
                return distance
            else:
                x_range, y_range, z_range = ((position[i] - skip, position[i] + skip) for i in (0, 1, 2))
                skip //= 2


def md(p1, p2):
    return sum(abs(x1 - x2) for x1, x2 in zip(p1, p2))


if __name__ == '__main__':
    d = Dec23()
    print('Nanobots in range of the strongest:', d.part_1())
    print('Distance to nearest teleportation point:', d.part_2())
