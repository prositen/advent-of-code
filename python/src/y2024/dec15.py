from python.src.common import Day, timer, Timer


class Warehouse(object):

    def __init__(self, walls, blocks, robot_pos, wide=False):
        self.walls = set()
        self.blocks = set()
        self.wide = wide

        if wide:
            for y, x in walls:
                self.walls.add((y, x * 2))
                self.walls.add((y, x * 2 + 1))
            for y, x in blocks:
                self.blocks.add((y, x * 2))
            self.ry = robot_pos[0]
            self.rx = 2 * robot_pos[1]
        else:
            self.walls = walls
            self.blocks = blocks
            self.ry, self.rx = robot_pos
        self.max_y = max(self.walls, key=lambda wall: wall[0])[0]
        self.max_x = max(self.walls, key=lambda wall: wall[1])[1]

        self.move_blocks = list()

    def gps_sum(self):
        return sum(
            y * 100 + x
            for (y, x) in self.blocks
        )

    def push_block(self, by, bx, dy, dx):
        if (by + dy, bx + dx) in self.walls:
            return False

        if (by + dy, bx + dx) in self.blocks:
            if self.wide:
                return self.push_wide_block(by + dy, bx + dx, dy, dx)

            if not self.push_block(by + dy, bx + dx, dy, dx):
                return False

        if dx == -1 and self.wide and (by, bx - 2) in self.blocks:
            return self.push_wide_block(by, bx - 2, 0, -1)

        if (by, bx) in self.blocks:
            self.move_blocks.append((by, bx))

        return True

    def push_wide_block(self, by, bx, dy, dx):
        if (by + dy, bx + dx) in self.walls:
            return False

        if dx != 0:

            # Check for block start +- 2 from here
            if (by, bx + dx + dx) in self.blocks:
                if not self.push_wide_block(by, bx + dx + dx, dy, dx):
                    return False

            if dx == 1:
                # Check or wall to the right of my right half
                if (by, bx + 2) in self.walls:
                    return False
        else:

            if (by + dy, bx) in self.blocks:
                # Block right above or below me
                if not (self.push_wide_block(by + dy, bx, dy, dx)):
                    return False
                if not (self.push_wide_block(by + dy, bx + 1, dy, dx)):
                    return False

            if (by + dy, bx + 1) in self.blocks:
                if not self.push_wide_block(by, bx + 1, dy, dx):
                    return False

            if (by + dy, bx - 1) in self.blocks:
                if not self.push_wide_block(by, bx - 1, dy, dx):
                    return False

        self.move_blocks.append((by, bx))
        return True

    def move_robot(self, instructions):
        _delta = {
            '^': (-1, 0),
            '>': (0, 1),
            'v': (1, 0),
            '<': (0, -1)
        }
        self.print()
        for direction in instructions:
            dy, dx = _delta[direction]
            self.move_blocks = list()
            if self.push_block(self.ry, self.rx, dy, dx):
                for by, bx in self.move_blocks[::1]:
                    self.blocks.discard((by, bx))
                    self.blocks.add((by + dy, bx + dx))
                self.ry += dy
                self.rx += dx
            print(direction)
            self.print()

    def print(self):
        for y in range(0, self.max_y):
            row = []
            for x in range(0, self.max_x):
                if (y, x) in self.walls:
                    row.append('#')
                elif (y, x) in self.blocks:
                    row.append('[')
                elif (y, x - 1) in self.blocks:
                    row.append(']')
                elif (y, x) == (self.ry, self.rx):
                    row.append('@')
                else:
                    row.append('.')
            print(''.join(row))


class Dec15(Day, year=2024, day=15):

    @staticmethod
    def parse_instructions(instructions):
        groups = Day.parse_groups(instructions)
        walls = set()
        blocks = set()
        start_pos = 0, 0
        for y, line in enumerate(groups[0]):
            for x, ch in enumerate(line):
                match ch:
                    case '@':
                        start_pos = y, x
                    case 'O':
                        blocks.add((y, x))
                    case '#':
                        walls.add((y, x))

        return walls, blocks, start_pos, ''.join(groups[1])

    @timer(part=1)
    def part_1(self):
        wh = Warehouse(walls=self.instructions[0],
                       blocks=self.instructions[1],
                       robot_pos=self.instructions[2])
        wh.move_robot(self.instructions[3])
        return wh.gps_sum()

    @timer(part=2)
    def part_2(self):
        wh = Warehouse(walls=self.instructions[0],
                       blocks=self.instructions[1],
                       robot_pos=self.instructions[2],
                       wide=True)
        wh.move_robot(self.instructions[3])
        return wh.gps_sum()


if __name__ == '__main__':
    with Timer('Total'):
        Dec15().run_day()
