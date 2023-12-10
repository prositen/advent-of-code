from collections import defaultdict, deque

from python.src.common import Day, timer, Timer


class Pipes(object):
    def __init__(self, surface_pipes: list):

        self.max_x = len(surface_pipes[0])
        self.max_y = len(surface_pipes)

        index = ''.join(surface_pipes).find('S')
        self.start = divmod(index, self.max_x)

        self.pipes = {
            (y, x): surface_pipes[y][x]
            for y in range(0, self.max_y)
            for x in range(0, self.max_x)
        }

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
        self.part_of_the_loop = {self.start}
        self.loop_in_order = list()

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

        while True:
            steps += 1
            pos = pos[0] + direction[0], pos[1] + direction[1]
            self.part_of_the_loop.add(pos)
            if pos == self.start:
                return steps // 2
            self.loop_in_order.append((pos, direction))
            match self.pipes[pos]:
                case '|' | '-':
                    continue
                case 'L' | '7':
                    direction = direction[1], direction[0]
                    self.loop_in_order.append((pos, direction))
                case 'J' | 'F':
                    direction = -direction[1], -direction[0]
                    self.loop_in_order.append((pos, direction))
                case _:
                    print('Ended up outside maze, something is wrong')
                    return None

    def find_enclosed_tiles(self):

        def flood_fill(fill_from, color):
            fill = {fill_from}
            while fill:
                p = fill.pop()
                if p not in self.pipes:
                    continue
                if (p in colors) or (p in self.part_of_the_loop):
                    continue
                colors[p] = color
                for nb in ((p[0] + d[0], p[1] + d[1]) for d in delta):
                    fill.add(nb)

        if not self.loop_in_order:
            self.run_loop()
        colors = dict()

        delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
        left_hand = 'a'
        right_hand = 'b'
        for pos, direction in self.loop_in_order:
            left_start = pos[0] - direction[1], pos[1] + direction[0]
            right_start = pos[0] + direction[1], pos[1] - direction[0]

            flood_fill(left_start, left_hand)
            flood_fill(right_start, right_hand)
        outside = {colors.get((0, x)) for x in range(self.max_x)}
        if 'a' in outside:
            return sum(v == 'b' for v in colors.values())
        else:
            return sum(v == 'a' for v in colors.values())

    def print(self, investigated):
        with open('pipes.txt', 'a') as fh:
            for y in range(self.max_y):
                line = list()
                for x in range(self.max_x):
                    line.append(investigated.get((y, x),
                                                 self.pipes[(y, x)]))
                fh.writelines(f'{"".join(line)}   {y}\n')
            fh.writelines('\n\n\n')


class Dec10(Day, year=2023, day=10):

    @staticmethod
    def parse_instructions(instructions):
        return Pipes(instructions)

    @timer(part=1)
    def part_1(self):
        return self.instructions.run_loop()

    @timer(part=2)
    def part_2(self):
        return self.instructions.find_enclosed_tiles()


if __name__ == '__main__':
    with Timer('Total'):
        Dec10().run_day()
