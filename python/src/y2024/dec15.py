from python.src.common import Day, timer, Timer


class Warehouse(object):

    def __init__(self, wh_map, wide=False):
        self.wide = wide
        if self.wide:
            wh_map = [
                line.replace('.', '..')
                .replace('O', '[]')
                .replace('#', '##')
                .replace('@', '@.') for line in wh_map]
        self.ry, self.rx = divmod(''.join(wh_map).index('@'),
                                  len(wh_map[0]))
        self.grid = {
            (y, x): ch
            for y, line in enumerate(wh_map)
            for x, ch in enumerate(line)
        }

    def gps_sum(self):
        return sum(y * 100 + x
                   for (y, x) in self.grid
                   if self.grid[(y, x)] in ('O', '['))

    def push_block(self, by, bx, dy, dx, dry_run):
        ny, nx = by + dy, bx + dx
        if self.grid[ny, nx] == '#':
            return False
        elif self.grid[ny, nx] != '.':
            if dy == 0 or self.grid[ny, nx] == 'O':
                if not self.push_block(ny, nx, dy, dx, dry_run):
                    return False
            elif self.grid[ny, nx] == '[':
                if not (self.push_block(ny, nx, dy, dx, dry_run)
                        and self.push_block(ny, nx + 1, dy, dx, dry_run)):
                    return False
            elif self.grid[ny, nx] == ']':
                if not (self.push_block(ny, nx, dy, dx, dry_run)
                        and self.push_block(ny, nx - 1, dy, dx, dry_run)):
                    return False

        if not dry_run:
            self.grid[by, bx], self.grid[ny, nx] = \
                self.grid[ny, nx], self.grid[by, bx]
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
            if self.push_block(self.ry, self.rx, dy, dx, dry_run=True):
                self.push_block(self.ry, self.rx, dy, dx, dry_run=False)
                self.ry += dy
                self.rx += dx

    def __str__(self):
        max_x = max(self.grid, key=lambda m: m[1])[1] + 1
        max_y = max(self.grid, key=lambda m: m[0])[0] + 1
        return '\n'.join(''.join(self.grid[y, x] for x in range(0, max_x))
                         for y in range(0, max_y))


class Dec15(Day, year=2024, day=15, title='Warehouse Woes'):

    @staticmethod
    def parse_instructions(instructions):
        groups = Day.parse_groups(instructions)
        return groups[0], ''.join(groups[1])

    @timer(part=1)
    def part_1(self):
        wh = Warehouse(wh_map=self.instructions[0])
        wh.move_robot(self.instructions[1])
        return wh.gps_sum()

    @timer(part=2)
    def part_2(self):
        wh = Warehouse(wh_map=self.instructions[0],
                       wide=True)
        wh.move_robot(self.instructions[1])
        return wh.gps_sum()


if __name__ == '__main__':
    with Timer('Total'):
        Dec15().run_day()
