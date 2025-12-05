from functools import cache

from python.src.common import Day, timer, Timer
from python.src.grid import Grid


class ToiletGrid(Grid):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.delta = set(self.delta).difference({(0, 0)})

    def accessible(self):
        return sum(
            sum(self.grid[nb] for nb in self.neighbours(pos))<4
            for pos in list(self.grid)
            if self.at(pos)
        )

    @cache
    def neighbours(self, pos):
        return [nb for nb in super().neighbours(pos)]

    def update_pos(self, pos):
        return self.grid[pos] and sum(self.grid[nb] for nb in self.neighbours(pos))>=4

    def remove_all_we_can(self):
        starting_rolls = self.count()
        prev_count, current_count = 0, starting_rolls
        while current_count != prev_count:
            self.step()
            prev_count = current_count
            current_count = self.count()

        return starting_rolls - current_count

class Dec04(Day, year=2025, day=4, title='Printing Department'):

    @staticmethod
    def parse_instructions(instructions):
        return [
            [ch == '@' for ch in line]
            for line in instructions
        ]

    @timer(part=1)
    def part_1(self):
        return ToiletGrid.from_lists(self.instructions).accessible()

    @timer(part=2)
    def part_2(self):
        return ToiletGrid.from_lists(self.instructions).remove_all_we_can()


if __name__ == '__main__':
    with Timer('Total'):
        Dec04().run_day()
