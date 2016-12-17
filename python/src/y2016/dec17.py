from collections import deque
from hashlib import md5


class Node:
    def __init__(self, passcode, x, y, path):
        self.passcode = passcode
        self.x = x
        self.y = y
        self.path = path

    def hashcode(self):
        value = self.passcode + "".join(self.path)
        value = value.encode('utf-8')
        return md5(value).hexdigest()[:4]

    def children(self):
        code = self.hashcode()
        children = []
        if self.y > 0 and int(code[0], 16) > 10:
            children.append(Node(self.passcode, self.x, self.y - 1, self.path + ['U']))
        if self.y < 3 and int(code[1], 16) > 10:
            children.append(Node(self.passcode, self.x, self.y + 1, self.path + ['D']))
        if self.x > 0 and int(code[2], 16) > 10:
            children.append(Node(self.passcode, self.x - 1, self.y, self.path + ['L']))
        if self.x < 3 and int(code[3], 16) > 10:
            children.append(Node(self.passcode, self.x + 1, self.y, self.path + ['R']))
        return children

    def __repr__(self):
        return "<Node x={0} y={1} path={2}>".format(self.x, self.y, self.path)


def shortest_path(passcode):
    nodes = deque()
    nodes.append(Node(passcode, 0, 0, []))

    while nodes:
        node = nodes.popleft()
        if node.x == 3 and node.y == 3:
            return ''.join(node.path)
        else:
            nodes.extend(node.children())

def longest_path(passcode):
    nodes = deque()
    nodes.append(Node(passcode, 0, 0, []))
    max_length = 0
    while nodes:
        node = nodes.popleft()
        if node.x == 3 and node.y == 3:
            max_length = max(len(node.path), max_length)
        else:
            nodes.extend(node.children())
    return max_length

if __name__ == '__main__':
    print("Shortest path is", shortest_path('lpvhkcbi'))
    print("Longest path is", longest_path('lpvhkcbi'))


