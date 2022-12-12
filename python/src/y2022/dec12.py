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

    def find_paths(self, from_positions, to_position):
        to_visit = deque()
        to_visit.extend([(f, 0, tuple()) for f in from_positions])
        visited = set()

        while to_visit:
            position, length, path = to_visit.popleft()
            if position == to_position:
                return length
            elif position not in visited:
                visited.add(position)
                for neighbour in self.neighbours(position):
                    if (neighbour not in visited) and self.at(neighbour) - self.at(position) < 2:
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
        return self.heights.find_paths(from_positions=[self.heights.pos],
                                       to_position=self.heights.end)

    @timer(part=2)
    def part_2(self):
        return self.heights.find_paths(from_positions=self.heights.lowest,
                                       to_position=self.heights.end)


if __name__ == '__main__':
    with Timer('Total'):
        Dec12().run_day()
