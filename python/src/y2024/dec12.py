from dataclasses import dataclass
from typing import Optional

from python.src.common import Day, timer, Timer


@dataclass
class Region:
    plant: str
    positions: set[tuple[int, int]]
    delta = ((-1, 0), (0, 1), (1, 0), (0, -1))

    @property
    def area(self) -> int:
        return len(self.positions)

    @property
    def perimeter(self) -> int:
        return sum(
            (y + dy, x + dx) not in self.positions
            for y, x in self.positions
            for (dy, dx) in self.delta
        )

    @property
    def sides(self):
        fences = set()
        _sides = 0
        for y, x in sorted(self.positions, key=lambda p: tuple(reversed(p))):
            for side, (dy, dx) in enumerate(self.delta):
                if (y + dy, x + dx) not in self.positions:
                    prev_y = y - 1 if dy == 0 else y
                    prev_x = x - 1 if dx == 0 else x
                    if (prev_y, prev_x, side) not in fences:
                        _sides += 1
                    fences.add((y, x, side))

        return _sides


class Garden(object):
    def __init__(self, garden_map):
        self.map = {
            (y, x): c
            for y, row in enumerate(garden_map)
            for x, c in enumerate(row)
        }
        self._regions: Optional[list[Region]] = None

    @property
    def regions(self):
        if self._regions is None:
            self._regions = []
            garden_pos = set(self.map)
            while garden_pos:
                visited = set()
                pos = garden_pos.pop()
                plant = self.map[pos]
                search = {pos}
                while search:
                    if (p := search.pop()) in visited or self.map[p] != plant:
                        continue
                    visited.add(p)
                    for nb in ((p[0] + d[0], p[1] + d[1]) for d in Region.delta):
                        if nb in self.map:
                            search.add(nb)
                self._regions.append(Region(plant=plant, positions=visited))
                garden_pos.difference_update(visited)

        return self._regions

    def fencing(self, bulk_price=False):
        if bulk_price:
            return sum(r.sides * r.area for r in self.regions)
        return sum(r.perimeter * r.area for r in self.regions)


class Dec12(Day, year=2024, day=12, title='Garden Groups'):

    @timer(part=1)
    def part_1(self):
        return Garden(self.instructions).fencing()

    @timer(part=2)
    def part_2(self):
        return Garden(self.instructions).fencing(bulk_price=True)


if __name__ == '__main__':
    with Timer('Total'):
        Dec12().run_day()
