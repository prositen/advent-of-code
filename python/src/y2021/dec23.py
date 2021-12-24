import itertools
from collections import defaultdict, namedtuple
from functools import lru_cache
from heapq import heappush, heappop

from python.src.common import Day, timer, Timer

Pod = namedtuple('Pod', ['pos', 'type'])


class PodBurrow(object):
    def __init__(self, pods):
        self.max_x = 12
        room_size = len(pods) // 4
        self.room_y = range(2, 2 + room_size)
        self.burrow = {
            (1, x): '.' for x in range(1, self.max_x)
        }
        self.burrow.update({
            (ty, tx): '.'
            for ty in self.room_y
            for tx in (3, 5, 7, 9)
        })

        self.pods = tuple(Pod(pos=pos, type=pod_type)
                          for pos, pod_type in pods.items())

    def can_move_out(self, grid, pod: Pod):
        for ty in range(2, pod.pos[0]):
            if grid[(ty, pod.pos[1])] != '.':
                return False

        for ty in self.room_y:
            if grid[(ty, pod.pos[1])] not in ('.', pod.type):
                return True

        return pod.pos[1] != pod.type * 2 + 3

    def move_in(self, grid, pod: Pod):
        for ty in sorted(self.room_y, reverse=True):
            if grid[(ty, pod.pos[1])] == '.':
                return ty - 1, (ty, pod.pos[1])
        return None

    def try_move_home(self, grid, pod: Pod):
        py, px = pod.pos
        cost = 0
        room = (pod.type * 2) + 3
        for ty in self.room_y:
            if grid[(ty, (pod.type * 2) + 3)] not in ('.', pod.type):
                return None
        if py > 1:
            cost += py - 1

        sgn = -1 if px > room else 1
        for x in range(px + sgn, room, sgn):
            if grid[(1, x)] != '.':
                return None

        cost += sgn * (room - px)
        for ty in sorted(self.room_y, reverse=True):
            if grid[(ty, room)] == '.':
                cost += ty - 1
                return (10 ** pod.type) * cost, (ty, room)

    def possible_moves(self, grid, pod: Pod):
        if pod.pos[0] > 1 and not self.can_move_out(grid, pod):
            return []
        if new_pos := self.try_move_home(grid, pod):
            return [new_pos]
        if pod.pos[0] == 1:
            return []

        # return self.move_to_corridor(pod, grid)
        moves = list()
        for r in (range(pod.pos[1] - 1, 0, -1), range(pod.pos[1] + 1, self.max_x)):
            for x in r:
                if grid[(1, x)] != '.':
                    break
                if x not in (3, 5, 7, 9):
                    moves.append((
                        (10 ** pod.type) * (abs(pod.pos[0] - 1) + abs(pod.pos[1] - x)),
                        (1, x)))
        return moves

    def all_home(self, pods):
        return not any(pod.pos[0] == 1 or pod.pos[1] != (pod.type * 2) + 3
                       for pod in pods)

    def print_grid(self, grid):
        r = [''.join(grid[(1, x)] for x in range(1, self.max_x))]
        r.extend(
            '   ' + '#'.join(grid.get((y, x), '.') for x in (3, 5, 7, 9))
            for y in self.room_y
        )
        return '\n'.join(r)

    @lru_cache(None)
    def dist(self, pod):
        room = (pod.type * 2) + 3
        return ((pod.pos[1] != room) *
                (10 ** pod.type) * (abs(pod.pos[1] - room) + pod.pos[0]))

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
                    pods[(y, x)] = ord(ch) - ord('A')
        return pods

    @timer(part=1)
    def part_1(self):
        burrow = PodBurrow(pods=self.pods)
        return burrow.organize()

    @timer(part=2)
    def part_2(self):
        pods = {
            (3, 3): 3,
            (3, 5): 2,
            (3, 7): 1,
            (3, 9): 0,
            (4, 3): 3,
            (4, 5): 1,
            (4, 7): 0,
            (4, 9): 2
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
