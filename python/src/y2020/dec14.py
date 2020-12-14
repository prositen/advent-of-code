from collections import defaultdict, deque

from python.src.common import Day, timer, Timer


class Dec14(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 14, instructions, filename)
        self.memory = dict()
        self.floating_mask = ''
        self.one_mask = 0
        self.zero_mask = 0

    def update_mask(self, mask):
        self.one_mask = int(mask.replace('X', '0'), 2)
        self.zero_mask = int(mask.replace('X', '1'), 2)
        self.floating_mask = mask

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

    def set_value(self, address, value, version=1):
        if version == 1:
            value = value & self.zero_mask
            value = value | self.one_mask
            self.memory[address] = value
        else:
            bin_address = f'{address:036b}'
            mask_address = ''.join(
                c1 if c2 == '0' else c2
                for c1, c2 in zip(bin_address, self.floating_mask)
            )
            for a in self.next_address(mask_address):
                self.memory[a] = value

    @staticmethod
    def next_address(mask):
        to_visit = deque()
        to_visit.append(mask)
        while to_visit:
            mask = to_visit.popleft()
            if 'X' not in mask:
                yield int(mask, 2)
            else:
                to_visit.append(mask.replace('X', '0', 1))
                to_visit.append(mask.replace('X', '1', 1))

    def run(self, version=1):
        self.memory = dict()
        for op, value in self.instructions:
            if op == 'mask':
                self.update_mask(value)
            else:
                self.set_value(address=op, value=value, version=version)

    @timer(part=1)
    def part_1(self):
        self.run()
        return sum(self.memory.values())

    @timer(part=2)
    def part_2(self):
        self.run(version=2)
        return sum(self.memory.values())


if __name__ == '__main__':
    with Timer('Total'):
        d = Dec14()
        d.part_1()
        d.part_2()
