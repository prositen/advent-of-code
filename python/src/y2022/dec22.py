from enum import IntEnum

from python.src.common import Day, timer, Timer


class Dir(IntEnum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


class MonkeyMap(object):
    def __init__(self, data):
        self.data = data
        self.y, self.x = 0, self.data[0].index('.')
        self.facing = Dir.RIGHT
        self.allowed_outside = True
        self.delta = {
            Dir.RIGHT: (0, 1),
            Dir.DOWN: (1, 0),
            Dir.LEFT: (0, -1),
            Dir.UP: (-1, 0)
        }

    def turn_right(self):
        self.facing = Dir((self.facing + 1) % 4)

    def turn_left(self):
        self.facing = Dir((self.facing - 1) % 4)

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


class MonkeyCube(MonkeyMap):
    def __init__(self, data):
        super().__init__(data)
        self.faces = [
            [data[y][50:100] for y in range(0, 50)],
            [data[y][100:150] for y in range(0, 50)],
            [data[y][50:100] for y in range(50, 100)],
            [data[y][0:50] for y in range(100, 150)],
            [data[y][50:100] for y in range(100, 150)],
            [data[y][0:50] for y in range(150, 200)]
        ]

        self.current_face = 0
        self.x = self.faces[0][0].index('.')

    def step(self, steps):
        moved = 0
        next_y, next_x = self.y, self.x
        while moved < steps:
            face = self.current_face
            facing = self.facing
            y, x = self.delta[self.facing]
            next_y, next_x = next_y + y, next_x + x

            if not ((0 <= next_y < 50) and (0 <= next_x < 50)):
                next_y, next_x, face, facing = self.warp(next_y, next_x)
            match self.faces[face][next_y][next_x]:
                case '.':
                    moved += 1
                    self.y, self.x = next_y, next_x
                    self.current_face = face
                    self.facing = facing

                case '#':
                    return

    def warp(self, next_y, next_x):
        if next_y == -1:
            match self.current_face:
                case 0:
                    return next_x, 0, 5, Dir.RIGHT
                case 1:
                    return 49, next_x, 5, Dir.UP
                case 2:
                    return 49, next_x, 0, Dir.UP
                case 3:
                    return next_x, 0, 2, Dir.RIGHT
                case 4:
                    return 49, next_x, 2, Dir.UP
                case 5:
                    return 49, next_x, 3, Dir.UP
        elif next_y == 50:
            match self.current_face:
                case 0:
                    return 0, next_x, 2, Dir.DOWN
                case 1:
                    return next_x, 49, 2, Dir.LEFT
                case 2:
                    return 0, next_x, 4, Dir.DOWN
                case 3:
                    return 0, next_x, 5, Dir.DOWN
                case 4:
                    return next_x, 49, 5, Dir.LEFT
                case 5:
                    return 0, next_x, 1, Dir.DOWN
        elif next_x == 50:
            match self.current_face:
                case 0:
                    return next_y, 0, 1, Dir.RIGHT
                case 1:
                    return 49 - next_y, 49, 4, Dir.LEFT
                case 2:
                    return 49, next_y, 1, Dir.UP
                case 3:
                    return next_y, 0, 4, Dir.RIGHT
                case 4:
                    return 49 - next_y, 49, 1, Dir.LEFT
                case 5:
                    return 49, next_y, 4, Dir.UP
        elif next_x == -1:
            match self.current_face:
                case 0:
                    return 49 - next_y, 0, 3, Dir.RIGHT
                case 1:
                    return next_y, 49, 0, Dir.LEFT
                case 2:
                    return 0, next_y, 3, Dir.DOWN
                case 3:
                    return 49 - next_y, 0, 0, Dir.RIGHT
                case 4:
                    return next_y, 49, 3, Dir.LEFT
                case 5:
                    return 0, next_y, 0, Dir.DOWN

    def map_pos(self):
        match self.current_face:
            case None:
                return self.y, self.x
            case 0:
                return self.y, 50 + self.x
            case 1:
                return self.y, 100 + self.x
            case 2:
                return 50 + self.y, 50 + self.x
            case 3:
                return 100 + self.y, self.x
            case 4:
                return 100 + self.y, 50 + self.x
            case 5:
                return 150 + self.y, self.x


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
        mc = MonkeyCube(self.instructions[0])
        mc.follow(self.instructions[1][0])
        pos = mc.map_pos()
        print(mc.current_face, mc.y, mc.x, pos)
        return 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + mc.facing


if __name__ == '__main__':
    with Timer('Total'):
        Dec22().run_day()
