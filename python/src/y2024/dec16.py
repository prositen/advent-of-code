from collections import defaultdict
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
        path = defaultdict(set)

        heappush(to_visit, (0, (self.start, 1), None))
        self.best_paths.add(self.end)
        while to_visit:
            cost, current, prev = heappop(to_visit)
            if cost > self.best_score:
                continue
            if current[0] == self.end:
                self.best_score = cost

            if current in visited:
                if visited[current] == cost:
                    path[current].add(prev)
                continue
            visited[current] = cost
            if prev:
                path[current].add(prev)

            pos, d = current
            if (n_pos := (pos[0] + delta[d][0], pos[1] + delta[d][1])) not in self.walls:
                heappush(to_visit, (cost + 1, (n_pos, d), current))

            for n_d in ((d + 1) % 4, (d - 1) % 4):
                if (n_pos := (pos[0] + delta[n_d][0], pos[1] + delta[n_d][1])) not in self.walls:
                    heappush(to_visit, (cost + 1001, (n_pos, n_d), current))

        lookup_path = {p for p in path if p[0] == self.end}

        while lookup_path:
            node = lookup_path.pop()
            self.best_paths.add(node[0])
            lookup_path.update(path[node])


class Dec16(Day, year=2024, day=16, title='Reindeer Maze'):

    @timer(part=1)
    def part_1(self):
        rm = ReindeerMaze(self.instructions)
        rm.find_cheapest_path()
        return rm.best_score

    @timer(part=2)
    def part_2(self):
        rm = ReindeerMaze(self.instructions)
        rm.find_cheapest_path()
        return len(rm.best_paths)


if __name__ == '__main__':
    with Timer('Total'):
        Dec16().run_day()
