from collections import deque

from python.src.common import Day, timer, Timer


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
        self.start = (0, 1)
        self.goal = (height, width - 1)
        self.deltas = ((-1, 0), (0, 1), (1, 0), (0, -1))

    def solve(self, here_and_back_again=False):
        to_visit = deque([(self.start, 0)])

        visited = set()
        blizzard_history = {0: self.blizzards}
        blizzard_pos = {0: {b.pos for b in self.blizzards}}
        goal_found = 0
        while to_visit:
            pos, time = to_visit.popleft()
            if pos == self.goal:
                if not here_and_back_again or goal_found == 2:
                    return time
                else:
                    goal_found += 1
                    visited = set()
                    self.goal, self.start = self.start, self.goal
                    to_visit = deque([(pos, time)])
                    continue
            if (pos, time) in visited:
                continue

            visited.add((pos, time))
            if time + 1 not in blizzard_history:
                blizzard_history[time + 1] = [
                    blizzard.move() for blizzard in blizzard_history[time]
                ]
                blizzard_pos[time + 1] = {blizzard.pos
                                          for blizzard in
                                          blizzard_history[time + 1]}

            for d in self.deltas:
                y, x = pos[0] + d[0], pos[1] + d[1]
                if (y, x) not in blizzard_pos[time + 1]:
                    if (y, x) == self.goal or (0 < y < self.height and 0 < x < self.width):
                        to_visit.append(((y, x), time + 1))

            if pos not in blizzard_pos[time + 1]:
                to_visit.append((pos, time + 1))


class Dec24(Day, year=2022, day=24):

    def __init__(self, filename=None, instructions=None):
        super().__init__(instructions=instructions, filename=filename)
        self.blizzards, self.height, self.width = self.instructions

    @staticmethod
    def parse_instructions(instructions):
        height = len(instructions) - 1
        width = len(instructions[0]) - 1
        blizzards = list()
        for y, line in enumerate(instructions):
            for x, c in enumerate(line):
                match c:
                    case '>' | '<':
                        blizzards.append(Blizzard(pos=(y, x), direction=c, border=width))
                    case '^' | 'v':
                        blizzards.append(Blizzard(pos=(y, x), direction=c, border=height))
        return blizzards, height, width

    @timer(part=1)
    def part_1(self):
        return Valley(self.blizzards, self.height, self.width).solve()

    @timer(part=2)
    def part_2(self):
        return Valley(self.blizzards, self.height, self.width).solve(here_and_back_again=True)


if __name__ == '__main__':
    with Timer('Total'):
        Dec24().run_day()
