from collections import deque, defaultdict

from python.src.common import Day


class Graph(object):

    def __init__(self):
        self.nodes = set()
        self.vertexes = defaultdict(list)
        self.started_nodes = set()

    def add_dependency(self, from_node, to_node):
        self.vertexes[from_node].append(to_node)
        self.nodes.add(from_node)
        self.nodes.add(to_node)

    def process_node(self, from_node):
        for k, v in list(self.vertexes.items()):
            if from_node in v:
                v.remove(from_node)
            if not v:
                self.vertexes.pop(k)
        self.nodes.remove(from_node)

    def available_nodes(self):
        return sorted(self.nodes - set(self.vertexes.keys()) - set(self.started_nodes),
                      reverse=True)

    def next_node(self):
        node = self.available_nodes().pop()
        if node:
            self.started_nodes.add(node)
        return node


class Dec07(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 7, instructions, filename)
        self.graph = None

    def build_graph(self):
        self.graph = Graph()
        for before, after in self.instructions:
            self.graph.add_dependency(after, before)

    @staticmethod
    def parse_instructions(instructions):
        pairs = []
        for row in instructions:
            words = row.split()
            pairs.append((words[1], words[7]))
        return pairs

    def part_1(self):
        self.build_graph()
        nodes = list()
        while self.graph.available_nodes():
            node = self.graph.next_node()
            nodes.append(node)
            self.graph.process_node(node)
        return ''.join(nodes)

    @staticmethod
    def make_job(node, delay):
        return node, delay + ord(node) - ord('A') + 1

    def part_2(self, elves, delay):
        self.build_graph()
        next_node = self.graph.next_node()
        working_elves = [self.make_job(next_node, delay)]
        time = 0
        while working_elves:
            time += 1
            for (node, duration) in list(working_elves):
                working_elves.remove((node, duration))
                duration -= 1
                if duration == 0:
                    self.graph.process_node(node)
                else:
                    working_elves.append((node, duration))

            free_elves = elves - len(working_elves)
            while free_elves > 0 and len(self.graph.available_nodes()):
                node = self.graph.next_node()
                working_elves.append(self.make_job(node, delay))
                free_elves -= 1
        return time - 1


if __name__ == '__main__':
    d = Dec07()
    print("Instruction order:", d.part_1())
    print("Time to assemble sleigh:", d.part_2(elves=5, delay=60))
