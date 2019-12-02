import os
from collections import deque

from python.src.y2017.common import DATA_DIR

"""
RecursiveCircus builds up the entire tree and does unspeakable things with it.

I should really look at a graph library to do the actual tree building instead of
hacking like this...
"""


class Node(object):
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children
        self.children_weights = dict()
        self.total_weight = weight

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
        self.root = None
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
        if not self.root:

            towers = dict()
            root = dict()
            for tower in self.towers:
                towers[tower.name] = tower
                root[tower.name] = tower

            for node in towers.values():
                node.children = [towers[c] for c in node.children]
                for x in node.children:
                    root.pop(x.name, None)
            self.root = list(root.values())[0]
        return self.root

    def get_weights(self, node):
        for x in node.children:
            w = self.get_weights(x)
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
        self.get_weights(node)
        return self.get_rebalanced_weight(node, node.total_weight)


def main():
    with open(os.path.join(DATA_DIR, 'input.7.txt')) as fh:
        puzzle_input = fh.readlines()

    rc = RecursiveCircus(puzzle_input)
    root = rc.find_bottom_program()
    print("Root is", root.name)
    print("Changed weight is", rc.balance_weights())


if __name__ == '__main__':
    main()
