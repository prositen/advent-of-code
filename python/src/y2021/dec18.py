import itertools

from python.src.common import Day, timer, Timer


class SnailFish(object):
    def __init__(self, numbers):
        self.numbers = [c for c in numbers]

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
        for i, (depth, number) in enumerate(self.numbers):
            if depth >= 5:
                _, right = self.numbers.pop(i + 1)
                if i > 0:
                    l_depth, l_num = self.numbers[i - 1]
                    self.numbers[i - 1] = (l_depth, l_num + number)
                self.numbers[i] = (depth - 1, 0)
                if i < len(self.numbers) - 1:
                    r_depth, r_num = self.numbers[i + 1]
                    self.numbers[i + 1] = (r_depth, r_num + right)
                break

        return self

    def split(self):
        for i, (depth, number) in enumerate(self.numbers):
            if number >= 10:
                half, rest = divmod(number, 2)
                self.numbers[i] = (depth + 1, half)
                self.numbers.insert(i + 1, (depth + 1, half + rest))
                break
        return self

    def magnitude(self):
        def mag(items, level):
            for i, (_depth, _number) in enumerate(items):
                if _depth == level:
                    items[i] = (level - 1, 3 * items[i][1] + 2 * items[i + 1][1])
                    items.pop(i + 1)
                    return items
            return items

        numbers = list(self.numbers)
        for depth in (4, 3, 2):
            while len(numbers) != len(mag(numbers, depth)):
                pass

        return 3 * numbers[0][1] + 2 * numbers[1][1]

    def __eq__(self, other):
        e = [(d1, n1) == (d2, n2)
             for (d1, n1), (d2, n2) in zip(self.numbers,
                                           other.numbers)]
        return all(e)

    def __str__(self):
        return str(self.numbers)

    def __repr__(self):
        return f'<SnailFishList {str(self)}>'

    def __add__(self, other):
        sf = SnailFish([
            (depth + 1, number)
            for (depth, number) in self.numbers + other.numbers
        ])

        changed = True
        while changed:
            if str(sf) != str(sf.explode()):
                continue
            changed = False

            if str(sf) != str(sf.split()):
                changed = True
                continue

        return sf


class Dec18(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 18, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return [
            SnailFish.from_string(row) for row in instructions
        ]

    def add_all(self, items):
        sf = SnailFish(numbers=items[0].numbers)
        for t2 in items[1:]:
            sf = sf + t2
        return sf

    @timer(part=1)
    def part_1(self):
        return self.add_all(self.instructions).magnitude()

    @timer(part=2)
    def part_2(self):
        max_mag = 0
        for items in itertools.permutations(self.instructions, 2):
            max_mag = max(max_mag, self.add_all(items).magnitude())
        return max_mag


if __name__ == '__main__':
    with Timer():
        Dec18().run_day()
