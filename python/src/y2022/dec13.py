import functools
import itertools
import json

from python.src.common import Day, timer, Timer


def compare_lists(left, right):
    to_visit = [pair for pair in itertools.zip_longest(left, right)]
    while to_visit:
        left, right = to_visit.pop(0)
        if left is None:
            return 1
        elif right is None:
            return -1
        if isinstance(left, int):
            if isinstance(right, int):
                if left < right:
                    return 1
                elif left > right:
                    return -1
            else:
                to_visit = [([left], right)] + to_visit
        else:
            if isinstance(right, int):
                to_visit = [(left, [right])] + to_visit
            else:
                to_visit = [pair for pair in itertools.zip_longest(left, right)] + to_visit

    return 0


class Dec13(Day, year=2022, day=13):

    @staticmethod
    def parse_instructions(instructions):
        groups = Dec13.parse_groups(instructions)
        return [
            (json.loads(g[0]), json.loads(g[1]))
            for g in groups
        ]

    @timer(part=1)
    def part_1(self):
        in_order = 0
        for i, pair in enumerate(self.instructions):
            if compare_lists(*pair) == 1:
                in_order += i + 1
        return in_order

    @timer(part=2)
    def part_2(self):
        all_packets = [[[2]], [[6]]]
        for left, right in self.instructions:
            all_packets.extend((left, right))
        sorted_packets = sorted(all_packets,
                                key=functools.cmp_to_key(compare_lists),
                                reverse=True)
        return (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)


if __name__ == '__main__':
    with Timer('Total'):
        Dec13().run_day()
