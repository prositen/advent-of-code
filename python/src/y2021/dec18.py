import json

from python.src.common import Day, timer, Timer


class SnailFishTree(object):

    def __init__(self, left, right, level):
        self.left = left
        self.right = right
        self.level = level

    @staticmethod
    def from_string(sf_string):
        return SnailFishTree.from_list(json.loads(sf_string))

    @staticmethod
    def from_list(sf_list, level=0):
        left, right = sf_list
        if isinstance(left, list):
            left = SnailFishTree.from_list(left, level + 1)
        if isinstance(right, list):
            right = SnailFishTree.from_list(right, level + 1)
        return SnailFishTree(left, right, level)

    def __str__(self):
        left = str(self.left)
        right = str(self.right)
        return f'[{left},{right}]'


class SnailFish(object):
    def __init__(self, numbers):
        self.numbers = numbers

    @staticmethod
    def from_string(sf_string):
        numbers = list()
        depth = 0
        for c in sf_string:
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
            elif c in (',', ' '):
                continue
            else:
                numbers.append((depth, int(c, 10)))
        return SnailFish(numbers)

    def explode(self):
        i = 0
        for depth, number in self.numbers:
            if depth >= 5:
                break
            i += 1
        else:
            return self
        depth, left = self.numbers[i]
        _, right = self.numbers.pop(i + 1)
        if i > 1:
            l_depth, l_num = self.numbers[i - 1]
            self.numbers[i - 1] = (l_depth, l_num + left)
        self.numbers[i] = (depth - 1, 0)
        if i < len(self.numbers) - 1:
            r_depth, r_num = self.numbers[i + 1]
            self.numbers[i + 1] = (r_depth, r_num + right)
        return self

    def split(self):
        i = 0
        for depth, number in self.numbers:
            if number >= 10:
                break
        else:
            return self
    def __eq__(self, other):
        e = [(d1, n1) == (d2, n2)
             for (d1, n1), (d2, n2) in zip(self.numbers,
                                           other.numbers)]
        return all(e)


class Dec18(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 18, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return [
            SnailFishTree.from_string(row) for row in instructions
        ]

    @timer(part=1)
    def part_1(self):
        return 1

    @timer(part=2)
    def part_2(self):
        return 2


if __name__ == '__main__':
    with Timer():
        Dec18().run_day()
