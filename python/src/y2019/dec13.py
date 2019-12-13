from collections import Counter

from python.src.common import Day
from python.src.y2019.intcode import IntCode


class Dec13(Day):
    def __init__(self, filename=None, instructions=None):
        super().__init__(2019, 13, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)

    def part_1(self):
        ic = IntCode(self.instructions)
        ic.run()
        tiles = Counter()
        for i in range(0, len(ic.output), 3):
            _, _, tile_id = ic.output[i:i + 3]
            tiles[tile_id] += 1
        return tiles[2]

    def part_2(self):
        pass


if __name__ == '__main__':
    d = Dec13()
    print("Part 1:", d.part_1())
    print("Part 2:", d.part_2())
