from collections import deque, defaultdict

from python.src.common import Day, timer, Timer
from python.src.grid import Grid


class HikingMap(Grid):

    def __init__(self, topography):
        super().__init__(dimensions=2, stay_in_bounds=True, state=topography)
        self.delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
        self.trailheads = {
            pos for pos, height in self.grid.items() if height == 0
        }

    def walk(self, can_revisit=False):
        positions = deque()
        seen_count = 0
        visited = set()
        for pos in self.trailheads:
            positions.append((pos, pos))
        while positions:
            th, pos = positions.popleft()
            if can_revisit or (th, pos) not in visited:
                visited.add((th, pos))
                if (height := self.at(pos)) == 9:
                    seen_count += 1
                    continue
                for nb in self.neighbours(pos):
                    if self.at(nb) == height + 1:
                        positions.append((th, nb))
        return seen_count


class Dec10(Day, year=2024, day=10, title='Hoof It'):

    @staticmethod
    def parse_instructions(instructions):
        return {
            (r, c): int(height)
            for r, line in enumerate(instructions)
            for c, height in enumerate(line)
        }

    @timer(part=1)
    def part_1(self):
        return HikingMap(self.instructions).walk()

    @timer(part=2)
    def part_2(self):
        return HikingMap(self.instructions).walk(can_revisit=True)


if __name__ == '__main__':
    with Timer('Total'):
        Dec10().run_day()
