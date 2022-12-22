from enum import IntEnum

from python.src.common import Day, timer, Timer


class Facing(IntEnum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


class MonkeyMap(object):
    def __init__(self, data):
        self.data = data
        self.y, self.x = 0, 0
        self.facing = Facing.RIGHT
        self.allowed_outside = True
        self.delta = {
            Facing.RIGHT: (0, 1),
            Facing.DOWN: (1, 0),
            Facing.LEFT: (0, -1),
            Facing.UP: (-1, 0)
        }

    def turn_right(self):
        self.facing = Facing((self.facing + 1) % 4)

    def turn_left(self):
        self.facing = Facing((self.facing - 1) % 4)

    def step(self, steps):
        y, x = self.delta[self.facing]
        moved = 0
        next_y, next_x = self.y, self.x
        while moved < steps:
            next_y, next_x = (next_y + y, next_x + x)
            next_y = next_y % len(self.data)
            row = self.data[next_y]
            next_x = next_x % len(row)
            col = row[next_x]
            match col:
                case ' ':
                    if self.allowed_outside:
                        moved += 1
                        self.y, self.x = next_y, next_x
                case '.':
                    moved += 1
                    self.y, self.x = next_y, next_x
                    self.allowed_outside = False
                case '#':
                    return

    def follow(self, path):
        steps = 0
        for c in path:
            match c:
                case 'L':
                    self.step(steps)
                    steps = 0
                    self.turn_left()

                case 'R':
                    self.step(steps)
                    steps = 0
                    self.turn_right()

                case _:
                    steps = 10 * steps + int(c)
        if steps:
            self.step(steps)
        return self.y, self.x


class Dec22(Day, year=2022, day=22):

    @staticmethod
    def parse_instructions(instructions):
        return Dec22.parse_groups(instructions=instructions)

    @timer(part=1)
    def part_1(self):
        mm = MonkeyMap(self.instructions[0])
        mm.follow(self.instructions[1][0])

        return 1000 * (mm.y + 1) + 4 * (mm.x + 1) + mm.facing

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec22().run_day()
