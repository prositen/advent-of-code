import itertools
import random
from collections import Counter, deque, defaultdict

from python.src.common import Day, timer, Timer


class Diagram(object):

    def __init__(self):
        self.parts = defaultdict(set)

    def add_part(self, part, connections):
        self.parts[part].update(connections)
        for c in connections:
            self.parts[c].add(part)

    def bfs(self, from_node, to_node=None, cut=None):
        if cut is None:
            cut = set()
        visited = set()
        to_visit = deque([(from_node, [])])
        while to_visit:
            name, path = to_visit.popleft()
            if name == to_node:
                return path
            if name in visited:
                continue
            visited.add(name)
            connections = self.parts[name]
            for nb in connections:
                edge = min(nb, name), max(nb, name)
                if nb not in visited and edge not in cut:
                    to_visit.append((nb, path + [edge]))

        if len(visited) != len(self.parts):
            return len(visited) * (len(self.parts) - len(visited))

    def visit_all(self):

        nodes = list(self.parts.keys())
        from_node = nodes[0]
        for to_node in set(nodes[1:]).difference(self.parts[from_node]):
            cut = set()
            for _ in range(3):
                path = self.bfs(from_node=from_node, to_node=to_node, cut=cut)
                cut.update(set(path))

            if r := self.bfs(from_node=from_node, cut=cut):
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
