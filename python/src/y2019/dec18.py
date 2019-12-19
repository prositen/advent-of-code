from collections import deque
from heapq import heappush, heappop

from python.src.common import Day


class Dec18(Day):
    def __init__(self, filename=None, instructions=None):
        super().__init__(2019, 18, filename=filename, instructions=instructions)
        start, self.keys, self.grid = self.instructions
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.pos_y, self.pos_x = divmod(start, self.width)

    @staticmethod
    def parse_instructions(instructions):
        _line = ''.join(instructions).strip()
        keys = ''.join(sorted(''.join(c for c in _line if c.islower())))
        return _line.index('@'), keys, [[c for c in row.strip()] for row in instructions]

    def can_go(self, pos_y, pos_x):
        if 0 <= pos_y < self.height and 0 <= pos_x < self.width:
            return self.grid[pos_y][pos_x] != '#'
        return False

    def part_1(self):
        bots = '@'
        paths = self.find_path_between_keys()
        return self.find_best_paths(bots, paths)

    def find_path_between_keys(self):
        paths = dict()
        for ry in range(1, self.height):
            for rx in range(1, self.width):
                c = self.grid[ry][rx]
                if c.islower() or c in '@1234':
                    to_visit = deque()
                    to_visit.append(((ry, rx), '', 0))
                    visited = {(ry, rx)}
                    paths[c] = list()

                    while to_visit:
                        (y, x), doors, steps = to_visit.popleft()
                        this = self.grid[y][x]
                        if this.islower() and this != c:
                            paths[c].append((this, steps, doors))
                        elif this.isupper():
                            doors += this

                        for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
                            ny, nx = y + dy, x + dx
                            if (ny, nx) not in visited and self.can_go(ny, nx):
                                visited.add((ny, nx))
                                to_visit.append(((ny, nx), doors, steps + 1))
        return paths

    def find_best_paths(self, bots, paths):
        # Start by moving from bots to nearest key
        # When a bot reaches a key, trace the step
        # from it to the next one, as contained in paths

        # to_visit = deque()
        # to_visit.append((bots, '', 0))
        to_visit = list()
        to_visit.append((0, bots, frozenset()))
        visited = dict()
        best_move = 10 ** 6
        while to_visit:
            # bots, keys, steps = to_visit.popleft()
            steps, bots, keys = heappop(to_visit)
            if (bots, keys) in visited:
                continue
            visited[(bots, keys)] = steps
            if len(keys) == len(self.keys):
                return steps

            for i, bot in enumerate(bots):
                for (dest, steps_to_dest, doors) in paths.get(bot, []):
                    if dest in keys or any([door.lower() not in keys for door in doors]):
                        continue
                    next_keys = keys | frozenset(dest)
                    next_move = bots[:i] + dest + bots[i + 1:]
                    next_steps = steps + steps_to_dest
                    heappush(to_visit, (next_steps,
                                        next_move, next_keys))
                    # to_visit.append((next_move, next_keys, next_steps))
                    # visited[(next_move, next_keys)] = next_steps

        return best_move

    def part_2(self):
        self.grid[self.pos_y - 1][self.pos_x - 1:self.pos_x + 2] = ['1', '#', '2']
        self.grid[self.pos_y][self.pos_x - 1:self.pos_x + 2] = ['#', '#', '#']
        self.grid[self.pos_y + 1][self.pos_x - 1:self.pos_x + 2] = ['3', '#', '4']
        bots = '1234'
        paths = self.find_path_between_keys()
        return self.find_best_paths(bots, paths)


if __name__ == '__main__':
    day = Dec18()
    # print("Part 1:", day.part_1())
    print("Part 2:", day.part_2())
