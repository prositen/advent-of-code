import sys
from heapq import heappop, heappush

from python.src.common import Day, timer, Timer


class LavaPool(object):
    def __init__(self, heat_loss_map):
        self.grid = [
            [int(ch) for ch in row]
            for row in heat_loss_map
        ]
        self.max_y = len(self.grid)
        self.max_x = len(self.grid[0])
        self.target = (self.max_y - 1, self.max_x - 1)

    def minimize_heat_loss(self, min_steps, max_steps):

        visited = set()
        to_visit = list()
        to_visit.extend([
            (0, (0, 0), 0, (0, 1)),
            (0, (0, 0), 0, (1, 0))
            # heat loss, pos, blocks moved in a single direction, direction
        ])

        while to_visit:
            heat_loss, pos, moved, d = heappop(to_visit)
            if pos == self.target and moved > min_steps:
                return heat_loss
            if (pos, moved, d) in visited:
                continue

            visited.add((pos, moved, d))

            if moved < max_steps:
                ny, nx = pos[0] + d[0], pos[1] + d[1]
                if 0 <= ny < self.max_y and 0 <= nx < self.max_x:
                    heappush(to_visit,
                             (heat_loss + self.grid[ny][nx],
                              (pos[0] + d[0], pos[1] + d[1]),
                              moved + 1, d))
            if moved >= min_steps:
                for nd in ((-d[1], d[0]), (d[1], -d[0])):
                    ny, nx = pos[0] + nd[0], pos[1] + nd[1]
                    if 0 <= ny < self.max_y and 0 <= nx < self.max_x:
                        heat = heat_loss + self.grid[ny][nx]
                        heappush(to_visit,
                                 (heat,
                                  (ny, nx), 1, nd)
                                 )

        return sys.maxsize


class Dec17(Day, year=2023, day=17):
    @timer(part=1)
    def part_1(self):
        lp = LavaPool(self.instructions)
        return lp.minimize_heat_loss(min_steps=0, max_steps=3)

    @timer(part=2)
    def part_2(self):
        lp = LavaPool(self.instructions)
        return lp.minimize_heat_loss(min_steps=4, max_steps=10)


if __name__ == '__main__':
    with Timer('Total'):
        Dec17().run_day()
