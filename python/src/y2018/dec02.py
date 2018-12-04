from collections import Counter

from python.src.common import Day


class Day02(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 2, instructions, filename)

    def part_1(self):
        box_counters = [Counter(box) for box in self.instructions]
        twos = len([b for b in box_counters if 2 in b.values()])
        threes = len([b for b in box_counters if 3 in b.values()])
        return twos * threes

    def part_2(self):
        for i, this_box in enumerate(self.instructions[:-1]):
            for other_box in self.instructions[i + 1:]:
                w = [a for a, b in zip(this_box, other_box) if a == b]
                if len(w) == len(this_box) - 1:
                    return ''.join(w)


if __name__ == '__main__':
    d = Day02()
    print("Box checksum:", d.part_1())
    print("Common letters:", d.part_2())
