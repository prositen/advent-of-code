from collections import deque

from python.src.common import Day, timer, Timer


class HikingTrails(object):

    def __init__(self, trail_map):
        self.map = [
            [ch for ch in row]
            for row in trail_map
        ]
        self.delta = {
            'v': (1, 0),
            '>': (0, 1),
            '^': (-1, 0),
            '<': (0, -1)
        }

        self.target = len(trail_map)-1, len(trail_map[0]) - 2

    def move(self,ignore_slopes=False):
        to_visit = deque()
        if ignore_slopes:
            to_visit.append((self.target, None))
            self.target = (0,1)
        else:
            to_visit.append(((0, 1), None))

        longest = 0
        while to_visit:
            (y, x), visited = to_visit.popleft()
            if visited is None:
                visited = set()
            if (y, x) == self.target:
                longest = max(longest, len(visited))
                continue

            visited = visited.union({(y, x)})
            if not ignore_slopes and self.map[y][x] in self.delta:
                dy, dx = self.delta[(self.map[y][x])]
                ny, nx = dy + y, dx + x
                if (ny, nx) not in visited:
                    to_visit.append(((ny, nx), set(visited)))
            else:
                for dy, dx in self.delta.values():
                    ny, nx = y + dy, x + dx
                    if 0<= ny < len(self.map) and (ny, nx) not in visited and self.map[ny][nx] != '#':
                        to_visit.append(((ny, nx), set(visited)))
        return longest


class Dec23(Day, year=2023, day=23):

    @timer(part=1, title='Longest hike')
    def part_1(self):
        ht = HikingTrails(self.instructions)
        return ht.move()

    @timer(part=2)
    def part_2(self):
        ht = HikingTrails(self.instructions)
        return ht.move(ignore_slopes=True)


if __name__ == '__main__':
    with Timer('Total'):
        Dec23().run_day()
