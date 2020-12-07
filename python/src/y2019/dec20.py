from collections import deque

from python.src.common import Day, timer, Timer


class Dec20(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 20, instructions, filename)
        self.maze = self.instructions
        self.portals = dict()
        self.connections = dict()
        self.find_portals()

    @staticmethod
    def parse_instructions(instructions):
        return instructions

    def get_pos(self, row, col):
        if 0 <= row < len(self.maze) and 0 <= col < len(self.maze[0]):
            return self.maze[row][col]
        return ''

    def find_portals(self):
        self.portals = dict()
        for ri in range(len(self.maze)):
            for ci in range(len(self.maze[ri])):
                c = self.get_pos(ri, ci)
                if c.isalpha():
                    right = self.get_pos(ri, ci + 1)
                    if right.isalnum():
                        name = c + right
                        left = self.get_pos(ri, ci - 1)
                        if left == '.':
                            self.portals[(ri, ci - 1)] = name
                        else:
                            self.portals[(ri, ci + 2)] = name
                    else:
                        down = self.get_pos(ri + 1, ci)
                        if down.isalnum():
                            name = c + down
                            up = self.get_pos(ri - 1, ci)
                            if up == '.':
                                self.portals[(ri - 1, ci)] = name
                            else:
                                self.portals[(ri + 2, ci)] = name

        for pos, name in self.portals.items():
            if name not in self.connections:
                self.connections[name] = list()
            self.connections[name] += [pos]

    def find_path(self):
        start_pos = self.connections['AA'][0]
        end_pos = self.connections['ZZ'][0]
        to_visit = deque()
        to_visit.append((0, start_pos))
        visited = set()
        while to_visit:
            steps, pos = to_visit.pop()
            visited.add(pos)
            row, col = pos
            c = self.get_pos(row, col)
            if c != '.':
                continue
            if (row, col) == end_pos:
                return steps
            for next_pos in (row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1):
                if self.get_pos(*next_pos) == '.' and next_pos not in visited:
                    to_visit.append((steps + 1, next_pos))
        return None

    @timer(part=1)
    def part_1(self, use_portals=True):
        return self.find_path()

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        d = Dec20()
        d.part_1()
        d.part_2()
