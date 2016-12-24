from collections import deque

from copy import copy
from itertools import permutations


class Grid(object):
    def __init__(self, lines):
        self.grid = lines
        self.all_numbers = self.find_numbers()

    def find_numbers(self):
        numbers = dict()
        for y, line in enumerate(self.grid[1:-1]):
            numbers.update({c: (y + 1, x) for x, c in enumerate(line) if c.isnumeric()})
        return numbers

    def cell(self, pos):
        return self.grid[pos[0]][pos[1]]

    def to_key(self, numbers):
        return ",".join(str(x) for x in numbers)

    def from_key(self, numbers):
        if len(numbers):
            return list(numbers.split(','))
        else:
            return []

    def shortest_path_between_all_pairs(self):
        paths = dict()
        positions = [self.all_numbers[pos] for pos in sorted(self.all_numbers.keys())]
        for from_index, from_node in enumerate(positions[:-1]):
            for to_index, to_node in enumerate(positions[from_index + 1:]):
                to_index += from_index + 1
                paths[(from_index, to_index)] = self.shortest_path_between(from_node, to_node)
        return paths

    moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    def shortest_path_between(self, from_node, to_node):
        """
        BFS between nodes
        :param from_node:
        :param to_node:
        :return: Shortest path between nodes
        """
        visited = set()
        to_visit = deque()
        to_visit.append((from_node, 0))
        while to_visit:
            node, path_len = to_visit.popleft()
            if node == to_node:
                return path_len
            path_len += 1
            visited.add(node)
            for dy, dx in self.moves:
                new_pos = (node[0] + dy, node[1] + dx)
                if self.cell(new_pos) != '#' and new_pos not in visited:
                    visited.add(new_pos)
                    to_visit.append((new_pos, path_len))

    def find_next_move(self, pos):
        return [new_pos for new_pos in
                [(pos[0] - 1, pos[1]), (pos[0], pos[1] - 1), (pos[0] + 1, pos[1]), (pos[0], pos[1] + 1)] if
                self.cell(new_pos) != '#']

    def shortest_path(self, return_to_start=False):
        num_nodes = len(self.all_numbers)
        tsp_graph = dict()
        for n in range(num_nodes):
            tsp_graph[n] = [None] * num_nodes
            tsp_graph[n][n] = 0

        for key, value in self.shortest_path_between_all_pairs().items():
            from_node, to_node = key
            tsp_graph[from_node][to_node] = value
            tsp_graph[to_node][from_node] = value

        shortest = 2 * sum(tsp_graph[0])  # back and forth between 0 and all nodes

        for path in permutations(range(1, num_nodes)):
            path_len = 0
            from_node = 0
            for to_node in path:
                path_len += tsp_graph[from_node][to_node]
                from_node = to_node
            if return_to_start:
                path_len += tsp_graph[from_node][0]
            shortest = min(shortest, path_len)
        return shortest


if __name__ == '__main__':
    with open('../../../data/2016/input.24.txt', 'r') as fh:
        game_map = fh.readlines()

    grid = Grid(game_map)

    print("Shortest path is", grid.shortest_path())
    print("Shortest path when returning to start is", grid.shortest_path(return_to_start=True))
