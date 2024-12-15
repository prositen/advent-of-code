from python.src.common import Day, timer, Timer


class Warehouse(object):

    def __init__(self, walls, blocks, robot_pos):
        self.walls = walls
        self.blocks = blocks
        self.ry, self.rx = robot_pos

    def gps_sum(self):
        return sum(
            y * 100 + x
            for (y, x) in self.blocks
        )

    def push_block(self, by, bx, dy, dx):
        if (by + dy, bx + dx) in self.blocks:
            if not self.push_block(by + dy, bx + dx, dy, dx):
                return False
        elif (by + dy, bx + dx) in self.walls:
            return False

        if (by, bx) in self.blocks:
            self.blocks.discard((by, bx))
            self.blocks.add((by + dy, bx + dx))
        return True

    def move_robot(self, instructions):
        _delta = {
            '^': (-1, 0),
            '>': (0, 1),
            'v': (1, 0),
            '<': (0, -1)
        }
        for direction in instructions:
            dy, dx = _delta[direction]

            if self.push_block(self.ry, self.rx, dy, dx):
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
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec15().run_day()
