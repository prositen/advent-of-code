from collections import defaultdict

from python.src.common import Day, timer, Timer


class Pipes(object):
    def __init__(self, surface_pipes: list):
        self.max_x = len(surface_pipes[0])
        self.max_y = len(surface_pipes)

        index = ''.join(surface_pipes).find('S')
        self.start = divmod(index, self.max_x)

        self.pipes = defaultdict(lambda: '.')
        self.pipes.update({
            (y, x): surface_pipes[y][x]
            for y in range(0, self.max_y)
            for x in range(0, self.max_x)
        })

        possible_pipes = {'|', '-', 'L', 'J', '7', 'F'}
        if self.pipes[self.start[0] - 1, self.start[1]] in {'|', '7', 'F'}:
            possible_pipes.difference_update({'-', '7', 'F'})
        else:
            possible_pipes.difference_update({'|', 'J', 'L'})

        if self.pipes[self.start[0] + 1, self.start[1]] in {'|', 'J', 'L'}:
            possible_pipes.difference_update({'L', 'J', '-'})
        else:
            possible_pipes.difference_update({'|', '7', 'F'})

        if self.pipes[self.start[0], self.start[1] - 1] in {'-', 'F', 'L'}:
            possible_pipes.difference_update({'|', 'L', 'F'})
        else:
            possible_pipes.difference_update({'-', '7', 'J'})
        assert (len(possible_pipes) == 1)

        self.pipes[self.start] = possible_pipes.pop()

    def run_loop(self):
        pos = self.start
        steps = 0
        match self.pipes[self.start]:
            case '|' | '7' | 'F':
                direction = (1, 0)
            case '-' | 'L':
                direction = (0, 1)
            case 'J' | _:
                direction = (1, 0)

        visited = set()
        while True:
            steps += 1
            pos = pos[0] + direction[0], pos[1] + direction[1]
            if pos == self.start:
                return steps // 2
            visited.add(pos)
            match self.pipes[pos]:
                case '|' | '-':
                    continue
                case 'L' | '7':
                    direction = direction[1], direction[0]
                case 'J' | 'F':
                    direction = -direction[1], -direction[0]
                case _:
                    print('Ended up outside maze, something is wrong')
                    return None


class Dec10(Day, year=2023, day=10):

    @timer(part=1)
    def part_1(self):
        pipes = Pipes(self.instructions)
        return pipes.run_loop()

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec10().run_day()
