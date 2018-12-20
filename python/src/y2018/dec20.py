import re
from collections import defaultdict, deque

from python.src.common import Day


class Sequence(object):

    def __init__(self):
        self.items = list()

    def add(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(-1)


class Option(Sequence):

    def __init__(self):
        super().__init__()
        self.current = None
        self.branch()

    def add(self, item):
        self.current.add(item)

    def branch(self):
        self.current = Sequence()
        super().add(self.current)


class Dec20(Day):
    DIRS = {
        'N': ((-1, 0), 0),
        'E': ((0, 1), 1),
        'S': ((1, 0), 2),
        'W': ((0, -1), 3)
    }

    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 20, instructions, filename)
        self.pos = (0, 0)
        self.map = defaultdict()
        self.map[self.pos] = [0, 0, 0, 0, 0]

    @staticmethod
    def parse_instructions(instructions):
        nested = deque()
        current_path = Sequence()
        for c in instructions[0].strip()[1:-1]:
            if c == '(':
                nested.append(current_path)
                current_path = Option()

            elif c == ')':
                last_branch = nested.pop()
                last_branch.add(current_path)
                current_path = last_branch
            elif c == '|':
                current_path.branch()
            else:
                current_path.add(c)
        return current_path

    def run_sequence(self, seq, pos, dist):
        for s in seq.items:
            if isinstance(s, Option):
                distances = list()
                for o in s.items:
                    distances.append(self.run_sequence(o, pos, dist))
                dist = min(distances)
            else:
                delta, index = self.DIRS[s]
                doors = self.map.get(pos, [0, 0, 0, 0, -1])
                doors[index] = 1

                dist = dist + 1
                pos = pos[0] + delta[0], pos[1] + delta[1]
                doors = self.map.get(pos, [0, 0, 0, 0, -1])
                doors[(index + 2) % 4] = 1
                if doors[4] == -1 or dist < doors[4]:
                    doors[4] = dist
                self.map[pos] = doors
        return dist

    def part_1(self):
        self.run_sequence(self.instructions, self.pos, 0)
        return max(self.map.values(), key=lambda g: g[4])[4]

    def part_2(self):
        return len(list(filter(lambda c: c[4] >= 1000, self.map.values())))


if __name__ == '__main__':
    d = Dec20()
    print('The door furthest away is:', d.part_1())
    print(':', d.part_2())
