import os

from python.src.y2017.common import DATA_DIR


class Routing(object):
    DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def __init__(self, puzzle_input):
        self.diagram = puzzle_input
        self.path = []
        self.pos = (0, 0)
        self.d = (1, 0)
        self.steps = 0
        self.max_x = len(self.diagram[0])
        self.max_y = len(self.diagram)

    def walk(self):
        while True:
            aa = self.square()
            while aa in ('|', '-'):
                self.move()
                aa = self.square()
            if aa == '+':
                for direction in self.DIRS:
                    if direction != (-self.d[0], -self.d[1]) and self.square(dy=direction[0], dx=direction[1]) != ' ':
                        self.d = direction
                        self.move()
                        break
            elif aa.isalpha():
                self.path.append(aa)
                self.move()
                self.walk()
            else:
                return

    def move(self):
        self.pos = self.pos[0] + self.d[0], self.pos[1] + self.d[1]
        self.steps += 1

    def square(self, dy=0, dx=0):
        y = self.pos[0] + dy
        x = self.pos[1] + dx
        if 0 <= y < self.max_y and 0 <= x <= self.max_x:
            return self.diagram[y][x]
        else:
            return ' '

    def part_1(self):
        self.pos = (0, self.diagram[0].index('|'))
        self.walk()
        return "".join(self.path)

    def part_2(self):
        return self.steps


def main():
    with open(os.path.join(DATA_DIR, 'input.19.txt')) as fh:
        puzzle_input = fh.readlines()

    r = Routing(puzzle_input)
    print("Part 1:", r.part_1())
    print("Part 2:", r.part_2())


if __name__ == '__main__':
    main()
