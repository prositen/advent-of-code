import math
from collections import Counter

from python.src.common import Day, timer, Timer


class Dec02(Day, year=2023, day=2):

    @staticmethod
    def parse_instructions(instructions):
        games = list()
        for game in instructions:
            info = game.split(':', 1)[1]
            cubes = Counter()
            for cube_info in info.split(';'):
                for color_info in cube_info.split(','):
                    num, color = color_info.strip().split(' ', 1)
                    cubes[color] = max(int(num), cubes[color])
            games.append(cubes)
        return games

    @staticmethod
    def possible(game, outcome):
        return all(game.get(col) <= count
                   for col, count in outcome.items())

    @timer(part=1)
    def part_1(self):
        return sum(game_id
                   for game_id, cubes in enumerate(self.instructions, start=1)
                   if self.possible(game=cubes,
                                    outcome={'red': 12, 'green': 13, 'blue': 14}))

    @timer(part=2)
    def part_2(self):
        return sum(math.prod(cubes.values()) for cubes in self.instructions)


if __name__ == '__main__':
    with Timer('Total'):
        Dec02().run_day()
