from collections import deque

from python.src.common import Day, timer
from python.src.y2018.dec08 import Node


class Dec06(Day):
    def __init__(self, instructions=None, filename=None):
        super().__init__(2019, 6, instructions, filename)
        self.nodes = None
        self.build_tree()

    @staticmethod
    def parse_instructions(instructions):
        return [x.split(')') for x in instructions]

    def build_tree(self):
        vertices = dict()
        for a, b in self.instructions:
            vertices[a] = vertices.get(a, list()) + [b]
        self.nodes = {
            a: Node(name=a) for a in set(x[1] for x in self.instructions)
        }
        self.nodes['COM'] = Node(name='COM')

        for a in self.nodes.keys():
            self.nodes[a].children = [self.nodes.get(b) for b in vertices.get(a, list())]
            for c in self.nodes[a].children:
                c.parent = self.nodes[a]

    @timer(part=1, title='Total number of orbits')
    def part_1(self):
        visit = deque()
        visit.append((self.nodes.get('COM'), 0))
        orbits = 0
        while visit:
            node, depth = visit.popleft()
            orbits += depth
            visit.extend([(c, depth + 1) for c in node.children])
        return orbits

    @timer(part=2, title='Number of orbits between you and Santa')
    def part_2(self):
        def find_root(node):
            while node and node.parent:
                node = node.parent
                yield node.name

        your_path = [r for r in find_root(self.nodes.get('YOU'))]
        santas_path = [r for r in find_root(self.nodes.get('SAN'))]

        return len(set(your_path).symmetric_difference(santas_path))


if __name__ == '__main__':
    Dec06().run_day()
