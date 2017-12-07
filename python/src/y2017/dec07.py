import os
from collections import deque

from python.src.y2017.common import DATA_DIR

""" 
RecursiveCircus contains my first solution which builds up the entire tree and does unspeakable things with it

My second attempt is SmallerCircus which only looks at the individual nodes (ok ok and their children, but nothing
deeper than that)

I should also try looking at some existing graph libraries to get a feeling of what they can do. Later, perhaps.

"""


class Node(object):
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children
        self.children_weights = dict()
        self.total_weight = weight

    def set_children(self, children):
        self.children = children

    def __repr__(self):
        return "{0} ({1}) -> {2}".format(self.name, self.weight, self.children)

    @staticmethod
    def print_tree(node):
        visit = deque()
        visit.append((node, 0))
        while visit:
            node, tab = visit.pop()
            print("{0}{1} {2}, {3}".format(tab * '\t', node.name, node.weight, node.total_weight))
            for x in node.children:
                visit.append((x, tab + 1))


class RecursiveCircus(object):

    def __init__(self, puzzle_input):
        self.towers = list()
        for line in puzzle_input:
            name, weight, parents = self.parse_line(line)
            self.towers.append(Node(name, weight, parents))

    @staticmethod
    def parse_line(line):
        words = line.split()
        name = words[0]
        weight = int(words[1][1:-1], 10)
        if len(words) > 3:
            parents = [word.rstrip(',') for word in words[3:]]
        else:
            parents = []
        return name, weight, parents

    def find_bottom_program(self):
        towers = dict()
        root = dict()
        for tower in self.towers:
            towers[tower.name] = tower
            root[tower.name] = tower

        for node in towers.values():
            node.children = [towers[c] for c in node.children]
            for x in node.children:
                root.pop(x.name, None)

        return list(root.values())[0]

    def get_weights(self, node, weight_above):
        for x in node.children:
            w = self.get_weights(x, weight_above + node.weight)
            if w not in node.children_weights:
                node.children_weights[w] = []
            node.children_weights[w].append(x)
            node.total_weight += w
        return node.total_weight

    def get_rebalanced_weight(self, node, expected):
        if len(node.children_weights) > 1:
            cw = sorted(node.children_weights.items(), key=lambda x: len(x[1]))
            wrong_tree = cw[0][1][0]
            correct_sum = cw[1][0]
            return self.get_rebalanced_weight(wrong_tree, correct_sum)

        node.weight += expected - node.total_weight
        return node.weight, node.name

    def balance_weights(self):
        node = self.find_bottom_program()
        self.get_weights(node, 0)
        return self.get_rebalanced_weight(node, node.total_weight)


class SmallerCircus(RecursiveCircus):

    def find_bottom_program(self):
        """
        Start with the name of all programs, and subtract the names appearing as "children"
        (or "parents" depending on which way you look at it)
        """
        return list(set(t.name for t in self.towers) - set(t for c in self.towers for t in c.children))[0]

    def _balance_weights(self):
        programs = {p.name: p for p in self.towers}
        for x,v in programs.items():
            print(x, v)

def main():
    with open(os.path.join(DATA_DIR, 'input.7.txt')) as fh:
        puzzle_input = fh.readlines()
    rc = SmallerCircus(puzzle_input)
    root = rc.find_bottom_program()
    print("Root is", root.name)
    print("Changed weight is", rc.balance_weights())


if __name__ == '__main__':
    main()
