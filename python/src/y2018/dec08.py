from collections import deque

from python.src.common import Day


class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = list()
        self.metadata = list()


class Dec08(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 8, instructions, filename)
        self.root = self.read_nodes()

    @staticmethod
    def parse_instructions(instructions):
        return list(map(int, instructions[0].split()))

    def read_nodes(self):
        tree = deque()
        node_id = 0
        root = node = Node(node_id)
        no_children = self.instructions[0]
        no_metadata = None
        for num in self.instructions[1:]:
            if no_metadata is None:
                no_metadata = num
                continue

            while no_children == len(node.children) \
                    and no_metadata == len(node.metadata):
                node, no_children, no_metadata = tree.pop()

            if no_children > len(node.children):
                tree.append((node, no_children, no_metadata))
                no_children, no_metadata = num, None
                node_id += 1
                new_node = Node(node_id)
                node.children.append(new_node)
                node = new_node
            else:
                node.metadata.append(num)
        return root

    def part_1(self):
        to_visit = deque()
        to_visit.append(self.root)
        checksum = 0
        while to_visit:
            node = to_visit.pop()
            checksum += sum(node.metadata)
            to_visit.extend(node.children)
        return checksum

    def part_2(self):
        return get_checksum(self.root)


def get_checksum(node):
    if node.children:
        check = [node.children[i - 1] for i in node.metadata if 0 < i <= len(node.children)]
        c = sum(get_checksum(c) for c in check)
    else:
        c = sum(node.metadata)
    return c


if __name__ == '__main__':
    d = Dec08()
    print("Checksum: ", d.part_1())
    print("Value of root node:", d.part_2())
