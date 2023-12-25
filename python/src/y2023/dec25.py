import itertools
import random
from heapq import heappop, heappush

from python.src.common import Day, timer, Timer
from collections import Counter, deque, defaultdict


class Diagram(object):

    def __init__(self):
        self.parts = defaultdict(set)
        self.cut = set()
        self.shortest_paths = dict()

    def add_cut(self, part, other):
        if part < other:
            self.cut.add((part, other))
        else:
            self.cut.add((other, part))

    def add_part(self, part, connections):
        self.parts[part].update(connections)
        for c in connections:
            self.parts[c].add(part)

    def bfs(self, from_node, to_node=None):
        if (from_node, to_node) in self.shortest_paths:
            return

        visited = set()
        to_visit = [(0, from_node, [])]
        while to_visit:
            d, name, path = heappop(to_visit)
            if name == to_node:
                self.shortest_paths[(from_node, to_node)] = path
                return 0
            if name in visited:
                continue
            visited.add(name)
            connections = self.parts[name]
            for nb in connections:
                edge = min(nb, name), max(nb, name)
                if nb not in visited and edge not in self.cut:
                    heappush(to_visit, (d + 1, nb, path + [edge]))

        if len(visited) != len(self.parts):
            return len(visited) * (len(self.parts) - len(visited))

    def visit_all(self):
        edge_count = Counter()
        nodes = list(self.parts.keys())
        for _ in range(500):
            from_node, to_node = random.choices(nodes, k=2)
            self.bfs(from_node=from_node, to_node=to_node)
            for edge in self.shortest_paths[(from_node, to_node)]:
                edge_count[edge] += 1
        most_common = [e for e, _ in edge_count.most_common(5)]
        for (e1, e2, e3) in itertools.combinations(most_common, 3):
            self.shortest_paths = dict()
            self.cut = set()
            self.add_cut(*e1)
            self.add_cut(*e2)
            self.add_cut(*e3)
            if r := self.bfs(from_node=nodes[0]):
                return r

class Dec25(Day, year=2023, day=25):

    @staticmethod
    def parse_instructions(instructions):
        return {
            (s := line.split(': '))[0]: s[1].split()
            for line in instructions
        }

    @timer(part=1)
    def part_1(self):
        dm = Diagram()
        for name, conns in self.instructions.items():
            dm.add_part(name, conns)
        return dm.visit_all()


if __name__ == '__main__':
    with Timer('Total'):
        Dec25().run_day()
