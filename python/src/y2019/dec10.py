from collections import defaultdict
from python.src.common import Day


class Dec10(Day):

    def __init__(self, filename=None, instructions=None):
        super().__init__(2019, 10, instructions, filename)
        self.max_x, self.max_y, self.asteroids = self.instructions
        self.best_position = (-1, -1)

    @staticmethod
    def parse_instructions(instructions):
        pos = list()
        for y, row in enumerate(instructions):
            for x, c in enumerate(row.strip()):
                if c != '.':
                    pos.append((x, y))
        return len(instructions[0]), len(instructions), pos

    def part_1(self):
        best = 0
        for me in self.asteroids:
            lines_of_sight = set()
            for other in self.asteroids:
                if me != other:
                    sign = me < other
                    try:
                        angle = (me[1]-other[1])/(me[0]-other[0])
                    except ZeroDivisionError:
                        angle = 1000
                    lines_of_sight.add((sign, angle))

            if len(lines_of_sight) > best:
                best = len(lines_of_sight)
                self.best_position = me
        return best

    def part_2(self):

        pass


if __name__ == '__main__':
    d = Dec10()
    print("Part 1:", d.part_1())
    print("Part 2:", d.part_2())
