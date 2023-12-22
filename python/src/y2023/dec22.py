from python.src.common import Day, timer, Timer
from src.grid import Grid


class BrickTower(object):

    def __init__(self, falling_bricks):
        self.min_z = 0
        self.bricks = {
            i: brick
            for i, brick in enumerate(falling_bricks)
        }
        self.grid = Grid(dimensions=3, data_type=int,
                         stay_in_bounds=False)
        for index, brick in self.bricks.items():
            for x in range(brick[0][0], brick[1][0]):
                for y in range(brick[0][1], brick[1][1]):
                    for z in range(brick[0][2], brick[1][2]):
                        print(index, x, y, z)
class Dec22(Day, year=2023, day=22):

    @staticmethod
    def parse_instructions(instructions):
        return [
            (tuple(map(int, s[0].split(','))),
             tuple(map(int, s[1].split(','))))
            for row in instructions
            for s in [row.split('~')]
        ]

    @timer(part=1)
    def part_1(self):
        bt = BrickTower(self.instructions)

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec22().run_day()
