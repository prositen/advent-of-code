from collections import deque

from python.src.common import Day, timer, Timer
from python.src.grid import Grid


class HeightMap(Grid):
    START = ord('S') - ord('a')
    END = ord('E') - ord('a')

    def __init__(self, heights):
        super().__init__(dimensions=2, data_type=int, stay_in_bounds=True, state=heights)
        self.delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.pos = (0, 0)
        self.max_coord = max(self.grid.keys())
        self.lowest = list()
        for k, v in self.grid.items():
            if v == self.START:
                self.pos = k
                self.lowest.append(k)
            elif v == self.END:
                self.end = k
            elif v == 0:
                self.lowest.append(k)
        self.grid[self.pos] = 0
        self.grid[self.end] = 25

    def __str__(self):
        return '\n'.join(
            ''.join(chr(self.grid[(r, c)] + ord('a'))
                    for c in range(self.max_coord[1]))
            for r in range(self.max_coord[0])
        )

    def find_paths(self, from_pos, to_positions):
        to_visit = deque()
        to_visit.append((from_pos, 0, tuple()))
        visited = set()
        do_reverse = len(to_positions) > 1

        def height_check(me, other):
            if do_reverse:
                return self.at(me) - self.at(other) < 2
            else:
                return self.at(other) - self.at(me) < 2

        while to_visit:
            position, length, path = to_visit.popleft()
            if position in to_positions:
                return length
            elif position not in visited:
                visited.add(position)
                for neighbour in self.neighbours(position):
                    if (neighbour not in visited) and height_check(position, neighbour):
                        to_visit.append((neighbour, length + 1, tuple([*path, position])))
        return 0


class Dec12(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2022, 12, instructions=instructions, filename=filename)
        self.heights = HeightMap(self.instructions)

    @staticmethod
    def parse_instructions(instructions):
        return {
            (r, c): ord(height) - ord('a')
            for r, line in enumerate(instructions)
            for c, height in enumerate(line)
        }

    @timer(part=1)
    def part_1(self):
        return self.heights.find_paths(from_pos=self.heights.pos,
                                       to_positions=[self.heights.end])

    @timer(part=2)
    def part_2(self):
        return self.heights.find_paths(from_pos=self.heights.end,
                                       to_positions=self.heights.lowest)


if __name__ == '__main__':
    with Timer('Total'):
        Dec12().run_day()
