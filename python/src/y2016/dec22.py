import re
from copy import deepcopy
from collections import deque


def make_node(size, used, large=200):
    if used == 0:
        return '_'
    elif size > large:
        return '#'
    else:
        return '.'


class Grid(object):
    re_NODE = re.compile(r"/dev/grid/node-x(\d+)-y(\d+) +(\d+)T +(\d+)T +\d+T +\d+%")
    _next_id = 0

    @staticmethod
    def next_id():
        Grid._next_id += 1
        return Grid._next_id

    def __init__(self, lines, large=200):
        self.max_dim = 0
        self.goal_node = None
        self.empty_node = None
        self.nodes = []
        self.large = large
        self.parse(lines[2:])

    def parse(self, nodes):
        self.max_dim = int(len(nodes) ** 0.5)  # assuming that the grid is square.
        temp_nodes = dict()
        for line in nodes:
            result = self.re_NODE.match(line)
            if result:
                x = int(result.group(1))
                y = int(result.group(2))
                size = int(result.group(3))
                used = int(result.group(4))
                if used == 0:
                    self.empty_node = (y, x)
                if y not in temp_nodes:
                    temp_nodes[y] = dict()
                temp_nodes[y][x] = make_node(size, used, self.large)
        temp_nodes[0][self.max_dim - 1] = 'G'
        self.goal_node = (0, self.max_dim - 1)

        for y in range(self.max_dim):
            self.nodes.append(''.join([temp_nodes[y][x] for x in range(self.max_dim)]))

    def __str__(self):
        return '\n'.join(self.nodes) + '\n'

    def key(self):
        """ The only important info is: which node is empty, and where is the goal data"""
        return "{}.{}".format(self.empty_node, self.goal_node)

    def node(self, pos):
        return self.nodes[pos[0]][pos[1]]

    def viable_move(self, node1, node2):
        return node2 == self.empty_node and self.node(node1) in ('.', 'G')

    def viable_pairs(self):
        to_node = self.empty_node
        viable = []
        for y in range(self.max_dim):
            for x in range(self.max_dim):
                if self.nodes[y][x] == '.' or self.nodes[y][x] == 'G':
                    viable.append(((y, x), to_node))
        return viable

    def move(self, from_node, to_node):
        y1, x1 = from_node
        y2, x2 = to_node

        c = self.nodes[y1][x1]
        self.nodes[y2] = self.nodes[y2][:x2] + c + (self.nodes[y2][x2 + 1:]
                                                    if x2 < self.max_dim else '')
        self.nodes[y1] = self.nodes[y1][:x1] + '_' + (self.nodes[y1][x1 + 1:]
                                                      if x1 < self.max_dim else '')
        if self.goal_node == from_node:
            self.goal_node = to_node
        self.empty_node = from_node

    def get_moves(self):
        to_node = self.empty_node
        moves = []
        for neighbor in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            from_node = to_node[0] + neighbor[0], to_node[1] + neighbor[1]
            if (0 <= from_node[0] < self.max_dim
                    and 0 <= from_node[1] < self.max_dim
                    and self.viable_move(from_node, to_node)):
                new_grid = deepcopy(self)

                new_grid.move(from_node, to_node)
                moves.append(new_grid)
        return moves


def find_shortest_path(grid):
    root = (grid, 0)
    nodes = deque()
    visited = {grid.key()}
    nodes.append(root)
    # old_steps = 0
    while nodes:
        new_grid, steps = nodes.popleft()
        # if steps != old_steps:
        #     print("Depth: ", steps, "nodes:", len(nodes), "visited:", len(visited))
        #     old_steps = steps
        if new_grid.node((0, 0)) == 'G':
            return steps
        else:
            for move in new_grid.get_moves():
                if move.key() not in visited:
                    visited.add(move.key())
                    nodes.append((move, steps + 1))
                    # nodes.append((move, steps + [desc], desc, nid))


if __name__ == '__main__':
    with open('../../../data/2016/input.22.txt', 'r') as fh:
        df = fh.readlines()
    grid = Grid(df)

    print("Viable pairs:", len(grid.viable_pairs()))
    shortest_path = find_shortest_path(grid)
    print("Shortest path:", shortest_path)
