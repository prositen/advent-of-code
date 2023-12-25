from collections import deque, defaultdict
from heapq import heappop, heappush

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

        self.target = len(trail_map) - 1, len(trail_map[0]) - 2

    def find_straight_path(self, pos, came_from, with_slopes=False):
        to_visit = deque()
        to_visit.append((pos, set(came_from), 0))
        y, x = pos
        while to_visit:
            (y, x), visited, length = to_visit.popleft()
            length += 1
            if (y, x) == self.target:
                return (y, x), length, set()

            valid_nbs = set()
            if with_slopes and self.map[y][x] in self.delta:
                dy, dx = self.delta[(self.map[y][x])]
                ny, nx = dy + y, dx + x
                if (ny, nx) not in visited:
                    valid_nbs = {(ny, nx)}
            else:
                for dy, dx in self.delta.values():
                    ny, nx = y + dy, x + dx
                    if (0 <= ny < len(self.map)
                            and (ny, nx) not in visited
                            and self.map[ny][nx] != '#'):
                        valid_nbs.add((ny, nx))
            visited.add((y, x))

            if len(valid_nbs) > 1:
                return (y, x), length, valid_nbs
            else:
                to_visit.extend(
                    (nb, set(visited), length) for nb in valid_nbs if nb not in visited)
        return (y, x), 0, set()

    def make_graph(self, with_slopes=False):
        nodes = dict()

        to_visit = deque()
        to_visit.append(((0, 1), set()))

        while to_visit:
            start_pos, came_from = to_visit.popleft()
            if start_pos not in nodes:
                end_pos, length, nbs = self.find_straight_path(pos=start_pos,
                                                               came_from=came_from,
                                                               with_slopes=with_slopes)
                nodes[start_pos] = (length, end_pos, nbs)

                to_visit.extend(((nb, {end_pos}) for nb in nbs))


        to_visit = [(-nodes[(0,1)][0], (0, 1), set())]
        longest = 0

        while to_visit:
            length, start_pos, visited = heappop(to_visit)
            _, end_pos, nbs = nodes[start_pos]
            new_visited = visited.union((end_pos,))
            for nb in nbs:
                n_length, n_end, _ = nodes[nb]
                n_length = length - n_length
                if n_end == self.target:
                    longest = min(n_length, longest)
                elif n_end not in visited:
                    heappush(to_visit, (n_length, nb, new_visited))

        return -longest - 1


class Dec23(Day, year=2023, day=23):

    @timer(part=1, title='Longest hike')
    def part_1(self):
        return HikingTrails(self.instructions).make_graph(with_slopes=True)

    @timer(part=2)
    def part_2(self):
        # 6442
        return HikingTrails(self.instructions).make_graph(with_slopes=False)


if __name__ == '__main__':
    with Timer('Total'):
        Dec23().run_day()
