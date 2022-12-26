import itertools
import operator
from collections import deque, defaultdict

from python.src.common import Day, timer, Timer


class Grove(object):
    def __init__(self, state):
        self.instructions = deque([
            # NW, N, NE -> N
            ([(-1, -1), (-1, 0), (-1, 1)], (-1, 0)),
            # SW, S, SE -> S
            ([(1, -1), (1, 0), (1, 1)], (1, 0)),
            # NW, W, SW -> W
            ([(-1, -1), (0, -1), (1, -1)], (0, -1)),
            # NE, E, SE -> E
            ([(-1, 1), (0, 1), (1, 1)], (0, 1))
        ])
        self.delta = list(itertools.product((-1, 0, 1), repeat=2))
        self.delta.remove((0, 0))
        self.elves = set(state)

    def step(self, steps=1):
        moved = 0
        while True:
            new_elves = defaultdict(list)
            for e in self.elves:
                if not any((e[0] + d[0], e[1] + d[1]) in self.elves for d in self.delta):
                    new_elves[e].append(e)
                else:
                    for nb, mv in self.instructions:
                        if not any((e[0] + n[0], e[1] + n[1]) in self.elves for n in nb):
                            new_pos = e[0] + mv[0], e[1] + mv[1]
                            new_elves[new_pos].append(e)
                            break
                    else:
                        new_elves[e].append(e)

            next_elves = set()

            for pos, elves in new_elves.items():
                if len(elves) > 1:
                    next_elves.update(elves)
                else:
                    next_elves.add(pos)

            moved += 1
            if self.elves == next_elves or (steps and moved > steps):
                return moved

            self.elves = next_elves
            self.instructions.rotate(-1)

    def count(self):
        x_pos = sorted(e[1] for e in self.elves)
        y_pos = sorted(e[0] for e in self.elves)
        min_x, max_x = x_pos[0], x_pos[-1]
        min_y, max_y = y_pos[0], y_pos[-1]
        total = (1 + max_x - min_x) * (1 + max_y - min_y)
        return total - len(self.elves)


class Dec23(Day, year=2022, day=23):

    @staticmethod
    def parse_instructions(instructions):
        elves = list()
        for y, line in enumerate(instructions):
            for x, char in enumerate(line):
                if char == '#':
                    elves.append((y, x))
        return elves

    @timer(part=1)
    def part_1(self):
        g = Grove(state=self.instructions)
        g.step(10)
        return g.count()

    @timer(part=2)
    def part_2(self):
        return Grove(state=self.instructions).step(None)


if __name__ == '__main__':
    with Timer('Total'):
        Dec23().run_day()
