import os
from collections import deque

from python.src.y2017.common import DATA_DIR


class Node(object):
    def __init__(self, *, score, parent):
        self.score = 0
        self.children = []
        self.parent = parent
        self.score = score
        self.garbage_length = 0

    @staticmethod
    def print_tree(node):
        visit = deque()
        visit.append((node, 0))
        while visit:
            node, tab = visit.pop()
            print("{0}{1}".format(tab * '\t', node.score))
            for x in node.children:
                visit.append((x, tab + 1))

    def sum_tree(self):
        visit = deque()
        visit.append(self)
        score = 0
        garbage_length = 0
        while visit:
            node = visit.pop()
            score += node.score
            garbage_length += node.garbage_length
            for x in node.children:
                visit.append(x)
        return score, garbage_length

    def __repr__(self):
        return "<Node score={} children={}>".format(self.score, self.children)


def build_tree(line):
    group = Node(score=0, parent=None)
    skip_next = False
    in_garbage = False
    for c in line:
        if in_garbage:
            if skip_next:
                skip_next = False
            elif c == '!':
                skip_next = True
            elif c == '>':
                in_garbage = False
            else:
                group.garbage_length += 1
        else:
            if c == '{':
                next_group = Node(score=group.score + 1, parent=group)
                group.children.append(next_group)
                group = next_group
            elif c == '}':
                group = group.parent
            elif c == '<':
                in_garbage = True

    return group


def main():
    with open(os.path.join(DATA_DIR, 'input.9.txt')) as fh:
        puzzle_input = fh.readlines()

    for line in puzzle_input:
        tree = build_tree(line)
        a, b = tree.sum_tree()
        print("Score", a)
        print("Garbage", b)


if __name__ == '__main__':
    main()
