import string
from collections import deque

from python.src.common import Day


class Dec05(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 5, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return instructions[0].strip()

    def part_1(self):
        return self.react(self.instructions)

    @staticmethod
    def react(polymer):
        stack = deque('.')
        for c in polymer:
            prev = stack.pop()
            if abs(ord(prev) - ord(c)) != 32:
                stack.append(prev)
                stack.append(c)
        stack.popleft()
        return ''.join(stack)

    def part_2(self):
        m = len(self.instructions)
        for unit in string.ascii_lowercase:
            polymer = self.instructions.replace(unit, '')
            polymer = polymer.replace(unit.upper(), '')
            m = min(m, len(self.react(polymer)))
        return m


if __name__ == '__main__':
    d = Dec05()
    print("Part 1:", len(d.part_1()))
    print("Part 2:", d.part_2())
