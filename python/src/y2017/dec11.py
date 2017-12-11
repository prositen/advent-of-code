import os
from abc import ABCMeta, abstractmethod

from python.src.y2017.common import DATA_DIR


class HexBase(object, metaclass=ABCMeta):

    def __init__(self):
        self.max_distance = 0

    @abstractmethod
    def walk(self, direction):
        pass

    def solve(self, instructions):
        for i in instructions.split(','):
            self.walk(i)
        return self.distance_from_start(), self.max_distance

    @abstractmethod
    def distance_from_start(self):
        pass


class NaiveHex(HexBase):
    """
    This is the hex grid implementation I came up with tired as f... in the morning,
    before reading that redblobgames article.

    The distance calculation is particularly slow and shitty but hey, it works.
     """

    DELTA = {
        'ne': (2, -1),
        'se': (2, 1),
        's': (0, 2),
        'sw': (-2, 1),
        'nw': (-2, -1),
        'n': (0, -2)
    }

    OPPOSITE = {
        'ne': 'sw',
        'se': 'nw',
        's': 'n',
        'sw': 'ne',
        'nw': 'se',
        'n': 's'
    }

    def __init__(self, pos_x=0, pos_y=0):
        super().__init__()
        self.x = pos_x
        self.y = pos_y

    def walk(self, direction):
        delta = self.DELTA.get(direction)
        self.x += delta[0]
        self.y += delta[1]

    def _on_ns_line(self):
        return self.x == 0

    def _on_diagonal_line(self):
        return abs(self.x) == abs(self.y * 2)

    def distance_from_start(self, base=0):
        if self._on_ns_line():
            return base + abs(self.y / 2)
        elif self._on_diagonal_line():
            return base + abs(self.x / 2)
        else:
            steps = 0
            other = NaiveHex(self.x, self.y)
            while not (other._on_ns_line() or other._on_diagonal_line()):
                steps += 1
                other.walk(other.OPPOSITE.get(other._heading()))
            return other.distance_from_start(base + steps)

    def _heading(self):
        if self.x > 0:
            return 'ne' if self.y else 'se'
        elif self.x < 0:
            return 'nw' if self.y < 0 else 'sw'
        else:
            return 'n' if self.y < 0 else 's'

    def solve(self, instructions):
        visited = set()
        for i in instructions.split(','):
            self.walk(i)
            visited.add((self.x, self.y))
        for v in visited:
            h = NaiveHex(v[0], v[1])
            self.max_distance = max(self.max_distance, h.distance_from_start())
        return self.distance_from_start(), self.max_distance


class QuickerHex(NaiveHex):
    """ Better distance implementation """

    def distance_from_start(self, base=0):
        a = self.x
        b = self.y - self.x / 2
        return int(max(abs(a), abs(b), abs(a + b)) / 2)

    def walk(self, direction):
        super().walk(direction)
        self.max_distance = max(self.max_distance, self.distance_from_start())

    def solve(self, instructions):
        return HexBase.solve(self, instructions)


def main():
    with open(os.path.join(DATA_DIR, 'input.11.txt')) as fh:
        puzzle_input = fh.read()

    solver = QuickerHex()
    distance, max_distance = solver.solve(puzzle_input)
    print("Part 1:", distance)
    print("Part 2:", max_distance)


if __name__ == '__main__':
    main()
