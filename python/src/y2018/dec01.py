from itertools import cycle
from python.src.common import Day


class Dec01(Day):
    def __init__(self, instructions=None):
        super().__init__(2018, 1, instructions)

    @staticmethod
    def parse_instructions(instructions):
        return list(map(int, instructions))

    def part_1(self):
        return sum(self.instructions)

    def part_2(self):
        found = {0}
        current = 0
        for n in cycle(self.instructions):
            current += n
            if current in found:
                return current
            found.add(current)


if __name__ == '__main__':
    d = Dec01()
    print("Frequency sum", d.part_1())
    print("Captcha sum: ", d.part_2())
