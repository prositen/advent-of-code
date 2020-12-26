from python.src.common import Day, timer, Timer
from python.src.gol import GameOfLife


class HexGrid(GameOfLife):
    def __init__(self):
        super().__init__(stay_alive=(1, 2),
                         new_life=(2,), stay_in_bounds=False)
        self.delta = self.DIRECTIONS.values()

    DIRECTIONS = {
        'nw': (-0.5, -0.5),
        'ne': (-0.5, 0.5),
        'e': (0, 1),
        'w': (0, -1),
        'sw': (0.5, -0.5),
        'se': (0.5, 0.5)
    }

    def walk_and_flip(self, path):
        pos = (0, 0)
        for step in path:
            dy, dx = self.DIRECTIONS[step]
            pos = pos[0] + dy, pos[1] + dx
        self.grid[pos] = not self.at(pos)

    def count_black(self):
        return sum(self.grid.values())


class Dec24(Day, year=2020, day=24):

    def __init__(self, instructions=None, filename=None):
        super().__init__(instructions=instructions, filename=filename)
        self.grid = HexGrid()
        for path in self.instructions:
            self.grid.walk_and_flip(path)

    @staticmethod
    def parse_instructions(instructions):
        paths = list()
        for instruction in instructions:
            path = list()
            prev = None
            char = ''
            for char in instruction:
                if prev and prev in 'ns':
                    path.append(prev + char)
                    prev = None
                elif char in 'ns':
                    prev = char
                else:
                    path.append(char)
                    prev = None
            if prev and prev in 'ns':
                path.append(prev + char)
            paths.append(path)
        return paths

    @timer(part=1)
    def part_1(self):
        return self.grid.count_black()

    @timer(part=2)
    def part_2(self):
        self.grid.step(100)
        return self.grid.count_black()


if __name__ == '__main__':
    with Timer('Lobby Layout'):
        Dec24().run_day()
