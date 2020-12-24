from collections import defaultdict

from python.src.common import Day, timer, Timer


class HexGrid(object):
    def __init__(self):
        self.tiles = dict()

    DIRECTIONS = {
        'nw': (-0.5, -0.5),
        'ne': (-0.5, 0.5),
        'e': (0, 1),
        'w': (0, -1),
        'sw': (0.5, -0.5),
        'se': (0.5, 0.5)
    }

    def walk_and_flip(self, path):
        pos = (0, 0)
        for step in path:
            dy, dx = self.DIRECTIONS[step]
            pos = pos[0] + dy, pos[1] + dx
        self.tiles[pos] = not self.at(pos)

    def count_black(self):
        return sum(self.tiles.values())

    def at(self, pos):
        return self.tiles.get(pos, False)


class Dec24(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 24, instructions, filename)
        self.grid = None

    @staticmethod
    def parse_instructions(instructions):
        paths = list()
        for instruction in instructions:
            path = list()
            prev = ''
            char = ''
            for char in instruction:
                if prev in ('n', 's'):
                    path.append(prev + char)
                    prev = ''
                elif char in 'ns':
                    prev = char
                else:
                    path.append(char)
                    prev = ''
            if prev in ('n', 's'):
                path.append(prev + char)
            paths.append(path)
        return paths

    @timer(part=1)
    def part_1(self):
        self.grid = HexGrid()
        for path in self.instructions:
            self.grid.walk_and_flip(path)
        return self.grid.count_black()

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        d = Dec24()
        d.part_1()
        d.part_2()
