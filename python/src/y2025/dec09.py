import itertools
import random

from python.src.common import Day, timer, Timer


class Rectangle:
    x_min: int
    y_min: int
    x_max: int
    y_max: int

    def __init__(self, tile_1, tile_2):
        x0, y0 = tile_1
        x1, y1 = tile_2
        self.x_min, self.x_max = min(x0, x1), max(x0, x1)
        self.y_min, self.y_max = min(y0, y1), max(y0, y1)

    def area(self) -> int:
        return (1 + self.x_max - self.x_min) * (1 + self.y_max - self.y_min)

    def intersects(self, other) -> bool:
        return not (
                self.x_max <= other.x_min or
                self.x_min >= other.x_max or
                self.y_max <= other.y_min or
                self.y_min >= other.y_max
        )


class TileFloor:
    def __init__(self, red_tiles: list[tuple]):
        self.red_tiles = red_tiles

    def largest_rectangle(self):
        return max(
            (1 + (abs(t1[0] - t2[0]))) * (1 + (abs(t1[1] - t2[1])))
            for (t1, t2) in itertools.combinations(self.red_tiles, 2)
        )

    def largest_rectangle_with_red_or_green_tiles(self):
        borders = [
            Rectangle(t1, t2)
            for t1, t2 in itertools.pairwise(self.red_tiles + self.red_tiles[:1])
        ]
        # Now shuffle!
        random.shuffle(borders)
        for rectangle in sorted(
                (Rectangle(t1, t2)
                 for t1, t2 in itertools.combinations(self.red_tiles, 2)),
                key=lambda rect: rect.area(),
                reverse=True
        ):
            if not any(rectangle.intersects(border) for border in borders):
                return rectangle.area()


class Dec09(Day, year=2025, day=9, title='Movie Theater'):

    @staticmethod
    def parse_instructions(instructions):
        return [tuple(map(int, line.split(','))) for line in instructions]

    @timer(part=1)
    def part_1(self):
        return TileFloor(self.instructions).largest_rectangle()

    @timer(part=2)
    def part_2(self):
        return TileFloor(self.instructions).largest_rectangle_with_red_or_green_tiles()


if __name__ == '__main__':
    with Timer('Total'):
        Dec09().run_day()
