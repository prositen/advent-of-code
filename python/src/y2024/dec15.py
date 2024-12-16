import sys

from python.src.common import Day, timer, Timer


class Warehouse(object):

    def __init__(self, walls, blocks, robot_pos, wide=False):
        self.walls = set()
        self.blocks = set()
        self.wide_block = set()
        self.wide = wide

        if wide:
            for y, x in walls:
                self.walls.add((y, x * 2))
                self.walls.add((y, x * 2 + 1))
            for y, x in blocks:
                self.blocks.add((y, x * 2))
                self.wide_block.add((y, x * 2 + 1))
            self.ry = robot_pos[0]
            self.rx = 2 * robot_pos[1]
        else:
            self.walls = {w for w in walls}
            self.blocks = {b for b in blocks}
            self.ry, self.rx = robot_pos

        self.move_blocks = list()

    def gps_sum(self):
        return sum(
            y * 100 + x
            for (y, x) in self.blocks
        )

    def push_block(self, by, bx, dy, dx):
        if (by, bx) in self.walls:
            return False
        if (by, bx) not in (self.blocks | self.wide_block):
            return True

        if not self.push_block(by + dy, bx + dx, dy, dx):
            return False

        if self.wide and dx == 0:
            if (by, bx) in self.blocks:
                if not self.push_block(by + dy, bx + 1, dy, 0):
                    return False
            elif (by, bx) in self.wide_block:
                if not self.push_block(by + dy, bx - 1, dy, 0):
                    return False

        if (by, bx) in self.blocks:
            self.move_blocks.append((by, bx))
        elif (by, bx) in self.wide_block:
            self.move_blocks.append((by, bx - 1))
        return True

    def move_robot(self, instructions):
        _delta = {
            '^': (-1, 0),
            '>': (0, 1),
            'v': (1, 0),
            '<': (0, -1)
        }

        for i, direction in enumerate(instructions):
            dy, dx = _delta[direction]
            self.move_blocks = list()
            if self.push_block(self.ry + dy, self.rx + dx, dy, dx):
                for by, bx in self.move_blocks[::1]:
                    self.blocks.discard((by, bx))
                    self.blocks.add((by + dy, bx + dx))
                    if self.wide:
                        self.wide_block.discard((by, bx + self.wide))
                        self.wide_block.add((by + dy, bx + dx + self.wide))

                self.ry += dy
                self.rx += dx


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
        # wh.print()
        return wh.gps_sum()


if __name__ == '__main__':
    with Timer('Total'):
        Dec15().run_day()
