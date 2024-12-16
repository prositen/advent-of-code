from heapq import heappop, heappush

from python.src.common import Day, timer, Timer


class ReindeerMaze(object):

    def __init__(self, maze_map):
        self.start = divmod(
            ''.join(maze_map).index('S'),
            len(maze_map)
        )

        self.end = divmod(
            ''.join(maze_map).index('E'),
            len(maze_map)
        )

        self.walls = {
            (y, x)
            for y, line in enumerate(maze_map)
            for x, ch in enumerate(line)
            if ch == '#'
        }

        self.best_score = 1000 * len(''.join(maze_map))
        self.best_paths = set()

    def find_cheapest_path(self):
        visited = dict()

        to_visit = list()
        delta = (
            (1, 0), (0, 1), (-1, 0), (0, -1)
        )
        heappush(to_visit, (0, self.start, 1, [self.start]))
        self.best_paths.add(self.end)
        while to_visit:
            cost, pos, d, path = heappop(to_visit)
            if cost > self.best_score:
                continue
            if pos == self.end:
                if cost < self.best_score:
                    self.best_score = cost
                    self.best_paths = {p for p in path}
                else:
                    self.best_paths.update(path)

            if (pos, d) in visited:
                if visited[(pos, d)] < cost:
                    continue
            visited[(pos, d)] = cost

            if (n_pos := (pos[0] + delta[d][0], pos[1] + delta[d][1])) not in self.walls:
                heappush(to_visit, (cost + 1, n_pos, d, path + [n_pos]))

            for n_d in ((d + 1) % 4, (d - 1) % 4):
                if (n_pos := (pos[0] + delta[n_d][0], pos[1] + delta[n_d][1])) not in self.walls:
                    heappush(to_visit, (cost + 1001, n_pos, n_d, path + [n_pos]))

class Dec16(Day, year=2024, day=16):

    def __init__(self, year=2024, day=16, instructions=None, filename=None):
        super().__init__(year, day, instructions, filename)
        self.rm = ReindeerMaze(self.instructions)

    @timer(part=1)
    def part_1(self):
        self.rm.find_cheapest_path()
        return self.rm.best_score

    @timer(part=2)
    def part_2(self):
        if not self.rm.best_paths:
            self.rm.find_cheapest_path()
        return len(self.rm.best_paths)


if __name__ == '__main__':
    with Timer('Total'):
        Dec16().run_day()
