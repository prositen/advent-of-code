import itertools

from python.src.common import Day, timer, Timer


class TileFloor:
    def __init__(self, red_tiles: list[tuple]):
        self.red_tiles = red_tiles

    def largest_rectangle(self):
        areas = sorted(
            ((abs(1 + t1[0] - t2[0])) * (abs(1 + t1[1] - t2[1])))
            for (t1, t2) in itertools.combinations(self.red_tiles, 2)
        )
        return areas[-1]


class Dec09(Day, year=2025, day=9, title='Movie Theater'):

    @staticmethod
    def parse_instructions(instructions):
        return [tuple(map(int, line.split(','))) for line in instructions]

    @timer(part=1)
    def part_1(self):
        return TileFloor(self.instructions).largest_rectangle()

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec09().run_day()
