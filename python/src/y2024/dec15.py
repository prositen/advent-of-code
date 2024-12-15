from python.src.common import Day, timer, Timer
from src.grid import Grid


class Warehouse(Grid):

    def __init__(self):
        super().__init__(dimensions=2, data_type=lambda: '#')

class Dec15(Day, year=2024, day=15):

    @staticmethod
    def parse_instructions(instructions):
        groups = Day.parse_groups(instructions)
        return groups[0], ''.join(groups[1])

    @timer(part=1)
    def part_1(self):
        print(self.instructions)
        return 0

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec15().run_day()
