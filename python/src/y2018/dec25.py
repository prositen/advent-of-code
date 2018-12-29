import re
from python.src.common import Day


def mh(p1, p2):
    """ Manhattan distance between two tuples of arbitrary length """
    return sum(abs(x1 - x2) for x1, x2 in zip(p1, p2))


class Dec25(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 25, instructions, filename)
        self.stars = self.instructions

    @staticmethod
    def parse_instructions(instructions):
        re_int = re.compile(r'(-?\d+)')
        return [
            list(map(int, re_int.findall(row))) for row in instructions
        ]

    def part_1(self):
        constellations = list()
        distances = dict()
        for i in range(len(self.stars)):
            distances[i] = dict()
            for j in range(i):
                distances[i][j] = distances[j][i]
            for j in range(i + 1, len(self.stars)):
                distances[i][j] = mh(self.stars[i], self.stars[j])

        not_handled = [i for i in range(len(distances))]
        handled = set()
        while not_handled:
            nearby = [not_handled.pop(-1)]
            while nearby:
                i = nearby.pop(-1)
                handled.add(i)
                nearby.extend(j for j in distances[i] if distances[i][j] <= 3 and j not in handled)
            constellations.append(list(handled))
            for i in handled:
                if i in not_handled:
                    not_handled.remove(i)
            handled = set()
        return len(constellations)


if __name__ == '__main__':
    d = Dec25()
    print('Number of constellations:', d.part_1())
