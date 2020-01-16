from collections import Counter

from python.src.common import Day
from python.src.y2019.intcode import IntCode


class Dec19(Day):
    def __init__(self, filename=None, instructions=None):
        super().__init__(2019, 19, filename=filename, instructions=instructions)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)

    def part_1(self):
        grid = list()
        points = 0
        for y in range(0, 50):
            grid.append(list())
            for x in range(0, 50):
                ic = IntCode(self.instructions)
                ic.add_input(x)
                ic.add_input(y)
                ic.run()
                beam = ic.get_output()
                grid[y].append('#' if beam else '.')
                points += beam
        for y, line in enumerate(grid):
            print(''.join(line), y, line.index('#') if '#' in line else '-', Counter(line)['#'])
        return points
    def part_2(self):
        pass


if __name__ == '__main__':
    day = Dec19()
    print("Part 1:", day.part_1())
    print("Part 2:", day.part_2())
