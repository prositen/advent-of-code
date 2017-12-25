import os
from collections import deque

from python.src.y2017.common import DATA_DIR


class Bridges(object):

    def __init__(self, puzzle_input):
        self.components = [self.parse(line) for line in puzzle_input]
        self.bridges = list()

    def is_starter(self, component):
        return self.has_port(component, 0)

    def has_port(self, component, num):
        return component[0] == num or component[1] == num

    def parse(self, line):
        nums = line.split('/')
        return int(nums[0]), int(nums[1])

    def build(self):
        queue = deque()
        for starter in filter(self.is_starter, self.components):
            queue.append(((starter,), starter[1]))
        visited = list()
        cm = set(self.components)

        while queue:
            bridge, port = queue.pop()
            sb = sorted(bridge)
            if sb not in visited:
                visited.append(sb)
                rm = cm - set(bridge)
                next_parts = filter(lambda x: self.has_port(x, port), rm)
                for part in next_parts:
                    if part[0] == port:
                        p = part[1]
                    else:
                        p = part[0]
                    b = bridge + (part,)
                    queue.appendleft((b, p))
        self.bridges = visited

    def bridge_strength(self, bridge):
        strength = 0
        for component in bridge:
            strength += component[0] + component[1]
        return strength

    def part1(self):
        return max(self.bridge_strength(b) for b in self.bridges)

    def part2(self):
        longest = max(len(b) for b in self.bridges)
        max_length_bridges = filter(lambda x: len(x) == longest, self.bridges)
        return max(self.bridge_strength(b) for b in max_length_bridges)


def main():
    with open(os.path.join(DATA_DIR, 'input.24.txt')) as fh:
        puzzle_input = fh.readlines()

    b = Bridges(puzzle_input)
    b.build()
    print("Part 1:", b.part1())
    print("Part 2:", b.part2())


if __name__ == '__main__':
    main()
