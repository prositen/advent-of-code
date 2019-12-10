from collections import defaultdict
from fractions import Fraction

from python.src.common import Day


class Dec10(Day):

    def __init__(self, filename=None, instructions=None):
        super().__init__(2019, 10, instructions, filename)
        self.best_position = (-1, -1)

    @staticmethod
    def parse_instructions(instructions):
        pos = list()
        for y, row in enumerate(instructions):
            for x, c in enumerate(row):
                if c != '.':
                    pos.append((x, y))
        return pos

    def part_1(self):
        best = 0
        satellites = sorted(self.instructions)
        shit = dict()

        for i, me in enumerate(satellites):
            lines_of_sight = set()
            l = defaultdict(list)
            m = dict()
            for j, other in enumerate(satellites):
                if i == j:
                    continue
                if me[1] == other[1]:
                    #slope = '<' if me[0] < other[0] else '>'
                    slope = -1000 if me[0] < other[0] else 1000
                elif me[0] == other[0]:
                    # slope = 'v' if me[1] < other[1] else '^'
                    slope = -2000 if me[1] < other[1] else 2000
                else:
                    slope = Fraction(me[1] - other[1], (me[0] - other[0]))
                lines_of_sight.add(slope)
                l[slope].append(other)
                m[other] = slope
            if len(lines_of_sight) > best:
                best = len(lines_of_sight)
                self.best_position = me
            shit[me] = l, m

        return best

    def part_2(self):
        pass


if __name__ == '__main__':
    d = Dec10()
    print("Part 1:", d.part_1())
    print("Part 2:", d.part_2())
