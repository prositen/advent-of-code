import itertools
from collections import defaultdict, namedtuple
from functools import lru_cache
from heapq import heappush, heappop

from python.src.common import Day, timer, Timer

Pod = namedtuple('Pod', ['pos', 'type'])
Point = namedtuple('Point', ['x', 'y'])


class PodBurrow(object):
    COSTS = {
        'A': 1,
        'B': 10,
        'C': 100,
        'D': 1000
    }

    def __init__(self, pods):
        self.max_x = 12
        self.room_x = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
        room_size = len(pods) // 4
        self.room_y = range(2, 2 + room_size)
        self.burrow = {
            Point(y=1, x=x): '.' for x in range(1, self.max_x)
        }
        self.burrow.update({
            Point(y=ty, x=tx): '.'
            for ty in self.room_y
            for tx in (3, 5, 7, 9)
        })

        self.pods = tuple(Pod(pos=Point(x=pos[1], y=pos[0]), type=pod_type)
                          for pos, pod_type in pods.items())

    def cost_distance(self, pod_type, pos1: Point, pos2: Point):
        return self.COSTS[pod_type] * (abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y))

    def move_to_corridor(self, pod: Pod, grid):
        for r in (range(pod.pos.x - 1, 0, -1), range(pod.pos.x + 1, self.max_x)):
            for x in r:
                if grid[Point(y=1, x=x)] != '.':
                    break
                if x not in self.room_x.values():
                    yield (self.cost_distance(pod.type, pod.pos, Point(y=1, x=x)),
                           Point(y=1, x=x))

    def can_move_in(self, grid, pod: Pod):
        tx = self.room_x[pod.type]
        occupants = (grid[Point(y=ty, x=tx)] for ty in sorted(self.room_y))
        return all(o in ('.', pod.type) for o in occupants)

    def can_move_out(self, grid, pod: Pod):
        tx = self.room_x[pod.type]
        empty_above = all(grid[Point(y=ty, x=pod.pos.x)] == '.'
                          for ty in range(2, pod.pos.y))
        if not empty_above:
            return False

        others_in_room = any(grid[Point(y=ty, x=pod.pos.x)] not in ('.', pod.type)
                             for ty in self.room_y)
        if others_in_room:
            return True

        return pod.pos.x != tx

    def move_in(self, grid, pod: Pod):
        tx = self.room_x[pod.type]
        target = ((Point(y=ty, x=tx) for ty in self.room_y))
        new_pos = max(t for t in target if grid.get(t, '.') == '.')
        return abs(pod.pos.y - new_pos.y), new_pos

    def try_move_home(self, grid, pod: Pod):
        py, px = pod.pos.y, pod.pos.x
        cost = 0
        target_x = self.room_x[pod.type]
        if not self.can_move_in(grid, pod):
            return None
        if py > 1:
            cost += py - 1

        sgn = -1 if px > target_x else 1
        if any(grid[Point(y=1, x=x)] != '.' for x in range(px + sgn, target_x, sgn)):
            return None

        cost += abs(px - target_x)
        c2, pos = self.move_in(grid, Pod(pos=Point(y=1, x=target_x), type=pod.type))

        return self.COSTS[pod.type] * (cost + c2), pos

    def possible_moves(self, grid, pod: Pod):
        if pod.pos.y > 1 and not self.can_move_out(grid, pod):
            return []
        if new_pos := self.try_move_home(grid, pod):
            return [new_pos]
        if pod.pos.y == 1:
            return []
        return self.move_to_corridor(pod, grid)

    def all_home(self, pods):
        return not any(pod.pos.y == 1 or pod.pos.x != self.room_x[pod.type]
                       for pod in pods)

    def print_grid(self, grid):
        r = [''.join(grid[Point(y=1, x=x)] for x in range(1, self.max_x))]
        r.extend(
            '   ' + '#'.join(grid.get(Point(y=y, x=x), '.') for x in (3, 5, 7, 9))
            for y in self.room_y
        )
        return '\n'.join(r)

    @lru_cache(None)
    def dist(self, pod):
        if pod.pos.x == self.room_x[pod.type]:
            return 0
        return self.COSTS[pod.type] * (abs(pod.pos.x - self.room_x[pod.type]) + pod.pos.y)

    @lru_cache(None)
    def distance(self, pods):
        return sum(self.dist(pod) for pod in pods)

    def organize(self):
        to_visit = [((self.distance(self.pods), 0), self.pods)]
        cache = dict()
        while to_visit:
            (_, cost), pods = heappop(to_visit)
            if self.all_home(pods):
                return cost

            grid = {**self.burrow}
            for pod in pods:
                grid[pod.pos] = pod.type
            for i, pod in enumerate(pods):
                moves = self.possible_moves(grid, pod)
                for step_cost, pos in moves:
                    new_pods = pods[:i] + (Pod(pos=pos, type=pod.type),) + pods[i + 1:]
                    new_cost = cost + step_cost
                    if new_pods in cache and cache[new_pods] < new_cost:
                        continue
                    cache[new_pods] = new_cost
                    distance = self.distance(new_pods)
                    new_state = ((distance + new_cost, new_cost), new_pods)
                    heappush(to_visit, new_state)
        return 0


class Dec23(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 23, instructions, filename)
        self.pods = self.instructions

    @staticmethod
    def parse_instructions(instructions):
        pods = dict()
        for y, line in enumerate(instructions):
            for x, ch in enumerate(line):
                if ch not in ('#', '.', ' '):
                    pods[(y, x)] = ch
        return pods

    @timer(part=1)
    def part_1(self):
        burrow = PodBurrow(pods=self.pods)
        return burrow.organize()

    @timer(part=2)
    def part_2(self):
        pods = {
            (3, 3): 'D',
            (3, 5): 'C',
            (3, 7): 'B',
            (3, 9): 'A',
            (4, 3): 'D',
            (4, 5): 'B',
            (4, 7): 'A',
            (4, 9): 'C'
        }
        for (y, x), pod in self.pods.items():
            if y > 2:
                pods[(y + 2, x)] = pod
            else:
                pods[(y, x)] = pod
        burrow = PodBurrow(pods=pods)
        return burrow.organize()


if __name__ == '__main__':
    with Timer('Amphipod'):
        Dec23().run_day()
