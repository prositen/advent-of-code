import heapq
from collections import defaultdict

from python.src.common import Day, timer, Timer
from python.src.helpers.SimpleGrid import SimpleGrid


class Race(SimpleGrid):

    def __init__(self, grid_map, **kwargs):
        super().__init__(grid_map, **kwargs)
        self.path = dict()
        self.found_cheats = defaultdict(int)

    def find_path(self):
        to_visit = [(0, self.start, None)]
        visited = defaultdict(lambda: self.max_y * self.max_x)
        paths = dict()

        while to_visit:
            steps, pos, prev = heapq.heappop(to_visit)
            if visited[pos] < steps:
                continue
            visited[pos] = steps
            if prev is not None:
                paths[pos] = prev
            if pos == self.end:
                break

            for new_pos in self.nbs(pos):
                if new_pos not in self.walls and visited[new_pos] > steps:
                    heapq.heappush(to_visit, (steps + 1, new_pos, pos))

        node = self.end
        self.path[self.start] = 0
        while node != self.start:
            self.path[node] = visited[node]
            node = paths[node]


    def count_cheats(self, skip=2, limit=1):
        if not self.found_cheats:
            self.find_path()
            for pos, steps in self.path.items():
                for dx in range(-skip, skip + 1):
                    for dy in range(-(skip - abs(dx)), skip + 1 - abs(dx)):
                        nx, ny = pos[0] + dx, pos[1] + dy
                        if skip_steps := self.path.get((nx, ny), 0):
                            this_save = skip_steps - steps - abs(dx) - abs(dy)
                            if this_save > 0:
                                self.found_cheats[this_save] += 1

        return sum(v for k, v in self.found_cheats.items() if k >= limit)


class Dec20(Day, year=2024, day=20, title='Race Condition'):

    @timer(part=1)
    def part_1(self):
        return Race(self.instructions).count_cheats(skip=2, limit=100)

    @timer(part=2)
    def part_2(self):
        return Race(self.instructions).count_cheats(skip=20, limit=100)


if __name__ == '__main__':
    with Timer('Total'):
        Dec20().run_day()
