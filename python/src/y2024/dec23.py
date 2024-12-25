from collections import defaultdict
from python.src.common import Day, timer, Timer


class LANParty(object):
    def __init__(self, network):
        self.edges = defaultdict(set)

        for c1, c2 in network:
            self.edges[c1].add(c2)
            self.edges[c2].add(c1)

        self.max = {}

    def bron_kerbousch(self, clique: set, to_check: set, checked: set):
        if not to_check and not checked:
            if len(clique) > len(self.max):
                self.max = clique

        for v in list(to_check):
            self.bron_kerbousch(clique | {v}, to_check & self.edges[v], checked & self.edges[v])
            to_check.remove(v)
            checked.add(v)

    def find_sets_of_three(self):
        sets_of_three = set()
        for computer in self.edges:
            for connected in self.edges[computer]:
                for third in self.edges[connected].intersection(self.edges[computer]):
                    sets_of_three.add(tuple(sorted((computer, connected, third))))
        return sets_of_three


class Dec23(Day, year=2024, day=23, title='LAN Party'):

    @staticmethod
    def parse_instructions(instructions):
        return [
            line.split('-')
            for line in instructions
        ]

    @timer(part=1)
    def part_1(self):
        lp = LANParty(self.instructions)
        s3 = lp.find_sets_of_three()
        return len([s for s in s3 if any(c.startswith('t') for c in s)])

    @timer(part=2)
    def part_2(self):
        lp = LANParty(self.instructions)
        lp.bron_kerbousch(set(), set(lp.edges.keys()), set())
        return ','.join(sorted(lp.max))


if __name__ == '__main__':
    with Timer('Total'):
        Dec23().run_day()
