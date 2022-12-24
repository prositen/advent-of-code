from collections import deque
from enum import Enum

from python.src.common import Day, timer, Timer


class Direction(Enum):
    NORTH = (-1, 0)
    EAST = (0, 1)
    SOUTH = (1, 0)
    WEST = (0, -1)
    WAIT = (0, 0)

    def __str__(self):
        match self.name:
            case 'NORTH':
                return '^'
            case 'EAST':
                return '>'
            case 'SOUTH':
                return 'v'
            case 'WEST':
                return '<'
            case 'WAIT':
                return 'W'

    def __add__(self, position):
        return position[0] + self.value[0], position[1] + self.value[1]


class Blizzard(object):
    def __init__(self, pos, direction, border):
        self.direction = direction
        self.border = border
        self.pos = pos

    def move(self):
        y, x = self.pos
        match self.direction:
            case '^':
                y -= 1
                if y == 0:
                    y = self.border - 1
            case '>':
                x += 1
                if x == self.border:
                    x = 1
            case 'v':
                y += 1
                if y == self.border:
                    y = 1
            case '<':
                x -= 1
                if x == 0:
                    x = self.border - 1
        return Blizzard(pos=(y, x), direction=self.direction, border=self.border)

    def __repr__(self):
        return f'<Blizzard pos={self.pos} direction="{self.direction}">'


class Valley(object):
    def __init__(self, blizzards, height, width):
        self.blizzards = blizzards
        self.height = height
        self.width = width
        self.pos = (0, 1)
        self.goal = (height - 1, width - 2)
        self.deltas = {
            '^': (-1, 0),
            '>': (0, 1),
            'v': (1, 0),
            '<': (0, -1)
        }

    def solve(self):
        to_visit = deque([(self.pos, 0)])

        visited = set()
        blizzard_history = {-1: self.blizzards}
        blizzard_pos_history = {-1: {b.pos for b in self.blizzards}}
        while to_visit:
            pos, time = to_visit.popleft()

            if (pos, time) in visited:
                continue

            visited.add((pos, time))
            if time not in blizzard_history:
                blizzard_history[time] = [
                    blizzard.move() for blizzard in
                    blizzard_history[time - 1]
                ]
                blizzard_pos_history[time] = {blizzard.pos for blizzard in
                                                        blizzard_history[time]}

            for d, delta in self.deltas.items():
                y, x = pos[0] + delta[0], pos[1] + delta[1]
                if pos == self.goal:
                    return time+1
                if 0 < y < self.height and 0 < x < self.width:
                    if (y, x) not in blizzard_pos_history[time]:
                        to_visit.append(((y, x), time + 1))
            if pos not in blizzard_pos_history[time]:
                to_visit.append((pos, time + 1))


class Dec24(Day, year=2022, day=24):

    @staticmethod
    def parse_instructions(instructions):
        height = len(instructions) - 1
        width = len(instructions[0]) - 1
        blizzards = list()
        for y, line in enumerate(instructions):
            for x, c in enumerate(line):
                match c:
                    case '>' | '<':
                        blizzards.append(Blizzard(pos=(y, x), direction=c,
                                                  border=width))
                    case '^' | 'v':
                        blizzards.append(Blizzard(pos=(y, x), direction=c,
                                                  border=height))
        return Valley(blizzards=blizzards, height=height, width=width)

    @timer(part=1)
    def part_1(self):
        return self.instructions.solve()

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec24().run_day()
