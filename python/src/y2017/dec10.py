import operator
import os
from functools import reduce

from python.src.y2017.common import DATA_DIR

pos = 0
skip_size = 0


class KnotHash(object):
    def __init__(self, lengths, list_length=256, input_is_bytes=True):
        self.values = list(range(list_length))
        if input_is_bytes:
            self.lengths = [ord(x) for x in lengths] + [17, 31, 73, 47, 23]
        else:
            self.lengths = map(int, lengths.split(','))
        self.pos = 0
        self.skip_size = 0
        self.list_length = list_length

    def round(self):
        for l in self.lengths:
            end = self.pos + l
            if end > self.list_length:
                end2 = end % self.list_length
                sub_list = self.values[self.pos:self.list_length] + self.values[:end2]
            else:
                sub_list = self.values[self.pos:end]
            sub_list = sub_list[::-1]
            for i, p in enumerate(range(self.pos, end)):
                self.values[p % self.list_length] = sub_list[i]
            self.pos += l + self.skip_size
            self.pos %= self.list_length
            self.skip_size += 1

    def check_first_two(self):
        return self.values[0] * self.values[1]

    def run(self):
        for _ in range(64):
            self.round()

    def checksum(self):
        sparse = [reduce(operator.xor, self.values[x * 16:(x + 1) * 16], 0) for x in range(16)]
        return "".join("{:0>2}".format(hex(a)[2:]) for a in sparse)


def main():
    with open(os.path.join(DATA_DIR, 'input.10.txt')) as fh:
        puzzle_input = fh.read()

    part_1 = KnotHash(puzzle_input, input_is_bytes=False)
    part_1.round()
    print(part_1.check_first_two())

    part_2 = KnotHash(puzzle_input)
    part_2.run()
    print(part_2.checksum())


if __name__ == '__main__':
    main()
