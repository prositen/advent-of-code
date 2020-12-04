from collections import deque
from heapq import heappush, heappop

from python.src.common import Day, timer


class Dec18(Day):
    def __init__(self, filename=None, instructions=None):
        super().__init__(2019, 18, filename=filename, instructions=instructions)
        start, self.keys, self.grid = self.instructions
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.pos_y, self.pos_x = divmod(start, self.width)

    @staticmethod
    def parse_instructions(instructions):
        _line = ''.join(instructions).strip().replace('\n', '')
        keys = frozenset(c for c in _line if c.islower())
        return _line.index('@'), keys, {y: row.strip() for y, row in enumerate(instructions)}

    def can_go(self, pos_y, pos_x):
        if 0 <= pos_y < self.height and 0 <= pos_x < self.width:
            return self.grid[pos_y][pos_x] != '#'
        return False

    @timer(part=1, title='Shortest path to collect all keys')
    def part_1(self):
        bots = '@'
        paths = self.find_path_between_keys()
        return self.find_best_paths(bots, paths)

    def find_path_between_keys(self):
        paths = dict()
        for ry, row in self.grid.items():
            for rx, c in enumerate(row):
                if c.islower() or c in '@1234':
                    to_visit = deque()
                    to_visit.append(((ry, rx), '', 0))
                    visited = set()
                    paths[c] = list()

                    while to_visit:
                        (y, x), doors, steps = to_visit.popleft()
                        if (y, x) in visited:
                            continue
                        visited.add((y, x))
                        this = self.grid[y][x]
                        if this.islower() and this != c:
                            paths[c].append((this, steps, frozenset(doors)))
                        elif this.isupper():
                            doors += this.lower()
                        elif this == '#':
                            continue
                        for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
                            ny, nx = y + dy, x + dx
                            if (0 <= nx < self.width) and (0 <= ny < self.height):
                                if (ny, nx) in visited:
                                    continue
                                to_visit.append(((ny, nx), doors, steps + 1))
        return paths

    def find_best_paths(self, bots, paths):
        # Start by moving from bots to nearest key
        # When a bot reaches a key, trace the step
        # from it to the next one, as contained in paths

        to_visit = list()
        to_visit.append((0, bots, frozenset()))
        visited = set()
        while to_visit:
            steps, bots, keys = heappop(to_visit)
            if keys == self.keys:
                return steps
            if (bots, keys) in visited:
                continue
            visited.add((bots, keys))

            for i, bot in enumerate(bots):
                for (dest, steps_to_dest, doors) in paths.get(bot, []):
                    if dest in keys or doors - keys:
                        continue
                    next_keys = keys | frozenset(dest)
                    next_move = bots[:i] + dest + bots[i + 1:]
                    if (next_move, next_keys) not in visited:
                        heappush(to_visit, (steps + steps_to_dest,
                                            next_move, next_keys))

    @timer(part=2, title='Shortest path to collect all keys in four mazes')
    def part_2(self):
        y = self.pos_y
        x = self.pos_x
        self.grid[y - 1] = self.grid[y - 1][:x - 1] + '1#2' + self.grid[y - 1][x + 2:]
        self.grid[y] = self.grid[y][:x - 1] + '###' + self.grid[y][x + 2:]
        self.grid[y + 1] = self.grid[y + 1][:x - 1] + '3#4' + self.grid[y + 1][x + 2:]
        bots = '1234'
        paths = self.find_path_between_keys()
        return self.find_best_paths(bots, paths)


if __name__ == '__main__':
    Dec18().run_day()
