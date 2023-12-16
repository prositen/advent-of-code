from python.src.common import Day, timer, Timer


class MetalPlatform(object):
    def __init__(self, platform):
        self.platform = [
            [ch for ch in row]
            for row in platform
        ]
        self.max_y = len(platform)
        self.max_x = len(platform[0])

        self.move = {
            'N': {
                'dx': 0,
                'dy': -1,
                'start_y': 1,
                'stop_y': self.max_y,
                'step_y': 1,
                'start_x': 0,
                'stop_x': self.max_x,
                'step_x': 1
            },
            'E': {
                'dx': 1,
                'dy': 0,
                'start_y': 0,
                'stop_y': self.max_y,
                'step_y': 1,
                'start_x': self.max_x - 2,
                'stop_x': -1,
                'step_x': -1
            },
            'S': {
                'dx': 0,
                'dy': 1,
                'start_y': self.max_y - 2,
                'stop_y': -1,
                'step_y': -1,
                'start_x': 0,
                'stop_x': self.max_x,
                'step_x': 1
            },
            'W': {
                'dx': -1,
                'dy': 0,
                'start_y': 0,
                'stop_y': self.max_y,
                'step_y': 1,
                'start_x': 1,
                'stop_x': self.max_x,
                'step_x': 1
            }
        }

    def roll(self, direction):
        move = self.move[direction]
        dy, dx = move['dy'], move['dx']
        for y in range(move['start_y'], move['stop_y'], move['step_y']):
            for x in range(move['start_x'], move['stop_x'], move['step_x']):
                if self.platform[y][x] == 'O':
                    move_y, move_x  = y, x
                    test_y, test_x = move_y + dy, move_x + dx
                    while (0 <= test_y < self.max_y and
                           0 <= test_x < self.max_x
                           and self.platform[test_y][test_x] == '.'):
                        move_y, move_x = test_y, test_x
                        test_y += dy
                        test_x += dx

                    self.platform[y][x] = '.'
                    self.platform[move_y][move_x] = 'O'

    def weight(self):
        return sum((self.max_y - y) * self.platform[y].count('O')
                   for y in range(self.max_y))

    def print(self, title=''):
        print(f'\n--- {title} ---')
        for y in self.platform:
            print(''.join(y))

    def cycle(self):
        self.roll('N')
        self.roll('W')
        self.roll('S')
        self.roll('E')

    def key(self):
        return '\n'.join(''.join(row) for row in self.platform)

    def run(self, cycle_count):
        seen = dict()
        weights = list()
        for i in range(cycle_count):
            self.cycle()
            if (key := self.key()) in seen:
                loop = i - seen[key]
                still_to_go = (cycle_count - i - 1) % loop
                return weights[seen[key] + still_to_go]
            seen[key] = i
            weights.append(self.weight())


class Dec14(Day, year=2023, day=14):

    @timer(part=1)
    def part_1(self):
        mp = MetalPlatform(self.instructions)
        mp.roll('N')
        return mp.weight()

    @timer(part=2)
    def part_2(self):
        mp = MetalPlatform(self.instructions)
        return mp.run(1000000000)


if __name__ == '__main__':
    with Timer('Total'):
        Dec14().run_day()
