import itertools
import math

from python.src.common import Day, timer, Timer


class Dec20(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 20, instructions, filename)
        self.update_edges()
        self.find_matches()

    @staticmethod
    def parse_instructions(instructions):
        return {int(g[0].split(' ')[1][:-1]): g[1:]
                for g in Day.parse_groups(instructions)}

    def update_edges(self):
        for tile, data in self.instructions.items():
            edges = [data[0],
                     ''.join(d[-1] for d in data),
                     data[-1],
                     ''.join(d[0] for d in data)]
            self.instructions[tile] = {
                'tile': data,
                'edges': edges,
                'inverted': [e[::-1] for e in edges],
                'connections': dict()
            }

    def find_matches(self):
        for en1, n1 in enumerate(self.instructions):
            for n2 in list(self.instructions)[en1 + 1:]:
                t1 = self.instructions[n1]
                t2 = self.instructions[n2]
                for i1, e1 in enumerate(t1['edges']):
                    for i2, e2 in enumerate(t2['edges']):
                        if e1 == e2:
                            t1['connections'][i1] = (n2, i2, True)
                            t2['connections'][i2] = (n1, i1, True)
                    for i2, e2 in enumerate(t2['inverted']):
                        if e1 == e2:
                            t1['connections'][i1] = (n2, i2, False)
                            t2['connections'][i2] = (n1, i1, False)

    def find_corners(self):
        return [n for n in self.instructions if len(self.instructions[n]['connections']) == 2]

    def form_image(self):
        corners = self.find_corners()
        nw = corners[0]
        print(nw)

    @timer(part=1)
    def part_1(self):
        return math.prod(self.find_corners())

    @timer(part=2)
    def part_2(self):
        self.form_image()


if __name__ == '__main__':
    with Timer():
        Dec20().run_day()
