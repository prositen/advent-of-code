from python.src.common import Day, timer, Timer
from python.src.gol import GameOfLife


class Dec17(Day, year=2020, day=17):

    @staticmethod
    def parse_instructions(instructions):
        return instructions

    def make_grid(self, dimensions):
        grid = dict()
        for y, line in enumerate(self.instructions):
            for x, char in enumerate(line):
                if dimensions == 3:
                    pos = (0, y, x)
                else:
                    pos = (0, 0, y, x)
                grid[pos] = char == '#'
        return grid

    @timer(part=1)
    def part_1(self):
        gol = GameOfLife(stay_alive=(2, 3), new_life=(3,), dimensions=3, stay_in_bounds=False)
        gol.set(self.make_grid(dimensions=3))
        gol.step(steps=6)
        return gol.count()

    @timer(part=2)
    def part_2(self):
        gol = GameOfLife(stay_alive=(2, 3), new_life=(3,), dimensions=4, stay_in_bounds=False)
        gol.set(self.make_grid(dimensions=4))
        gol.step(steps=6)
        return gol.count()


if __name__ == '__main__':
    with Timer('Conway Cubes'):
        Dec17().run_day()
