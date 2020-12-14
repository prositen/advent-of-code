from collections import defaultdict

from python.src.common import Day, timer, Timer


class Dec14(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 14, instructions, filename)
        self.memory = defaultdict(int)
        self.or_mask = '0' * 36
        self.and_mask = '1' * 36

    def update_mask(self, mask):
        self.or_mask = int(mask.replace('X', '0'), 2)
        self.and_mask = int(mask.replace('X', '1'), 2)

    @staticmethod
    def parse_instructions(instructions):
        result = list()
        for row in instructions:
            op, value = row.split(' = ')
            if op != 'mask':
                op = int(op[4:-1], 10)
                value = int(value, 10)
            result.append((op, value))
        return result

    @timer(part=1)
    def part_1(self):
        for op, value in self.instructions:
            if op == 'mask':
                self.update_mask(value)
            else:
                value = value & self.and_mask
                value = value | self.or_mask
                self.memory[op] = value
        return sum(self.memory.values())

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        d = Dec14()
        d.part_1()
        d.part_2()
