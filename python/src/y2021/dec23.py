from collections import defaultdict, namedtuple
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

    def __init__(self, grid, pods, rooms):
        self.max_x = max(grid, key=lambda c: c[1])[1]
        self.room_x = dict()
        for pos, pod_type in rooms.items():
            self.room_x[pod_type] = pos[1]
        self.pods = tuple(Pod(pos=Point(x=pos[1], y=pos[0]), type=pod_type)
                          for pos, pod_type in pods.items())

    def cost_distance(self, pod_type, pos1: Point, pos2: Point):
        return self.COSTS[pod_type] * (abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y))

    def distance_home(self, pod: Pod):
        return abs(pod.pos.x - self.room_x[pod.type]) + abs(pod.pos.y - 2.5)

    def move_to_corridor(self, pod: Pod, grid):
        for r in (range(pod.pos.x-1, 0, -1), range(pod.pos.x + 1, self.max_x)):
            for x in r:
                if grid[Point(y=1, x=x)] != '.':
                    break
                if x not in self.room_x.values():
                    yield (self.cost_distance(pod.type, pod.pos, Point(y=1, x=x)),
                           Point(y=1, x=x))

    def can_move_in(self, grid, pod: Pod):
        tx = self.room_x[pod.type]
        return ((grid.get(Point(y=2, x=tx), '.') == '.') and
                grid.get(Point(y=3, x=tx), '.') in (pod.type, '.'))

    def can_move_out(self, grid, pod: Pod):
        if pod.pos.y == 2 and (
                (not pod.pos.x == self.room_x[pod.type])
                or grid.get(Point(y=3, x=self.room_x[pod.type]), '.') != pod.type):
            return True
        elif (pod.pos.y == 3
              and not pod.pos.x == self.room_x[pod.type]
              and grid.get(Point(y=2, x=pod.pos.x), '.') == '.'):
            return True
        return False

    def move_in(self, grid, pod: Pod):
        tx = self.room_x[pod.type]
        target = (Point(y=2, x=tx), Point(y=3, x=tx))
        new_pos = max(t for t in target if grid.get(t, '.') == '.')
        return self.cost_distance(pod.type, pod.pos, new_pos), new_pos

    def try_move_home(self, grid, pod: Pod):
        (py, px) = pod.pos.y, pod.pos.x
        cost = 0
        target_x = self.room_x[pod.type]
        if not self.can_move_in(grid, pod):
            return None
        if py > 1:
            if not self.can_move_out(grid, pod):
                return None
            cost = self.COSTS[pod.type] * (py - 1)
            py = 1

        sgn = -1 if px > target_x else 1
        for x in range(px+sgn, target_x, sgn):
            if grid[Point(y=1, x=x)] != '.':
                return None
        cost += self.cost_distance(pod.type, Point(y=py, x=px), Point(y=1, x=target_x))

        c2, pos = self.move_in(grid, Pod(pos=Point(y=py, x=target_x), type=pod.type))
        return cost + c2, pos

    def possible_moves(self, grid, pod: Pod):
        if new_pos := self.try_move_home(grid, pod):
            return [new_pos]

        if pod.pos.y == 1:
            return []
        else:
            if not self.can_move_out(grid, pod):
                return []
            return [p for p in self.move_to_corridor(pod, grid)]

    def all_home(self, pods):
        return not any(pod.pos.y == 1 or pod.pos.x != self.room_x[pod.type]
                       for pod in pods)

    def print_grid(self, grid):
        r = [''.join(grid[Point(y=1, x=x)] for x in range(1, self.max_x))]
        r.extend(
            '   ' + '#'.join(grid.get(Point(y=y, x=x), '.') for x in (3, 5, 7, 9))
            for y in (2, 3)
        )
        return '\n'.join(r)

    def organize(self):
        to_visit = [((sum(self.distance_home(pod) for pod in self.pods), 0), self.pods, [])]
        cache = set()
        while to_visit:
            grid = {Point(y=1, x=x): '.' for x in range(1, 12)}
            (step, cost), pods, path = heappop(to_visit)
            for pod in pods:
                grid[pod.pos] = pod.type
            if self.all_home(pods):
                return cost

            for i, pod in enumerate(pods):
                moves = self.possible_moves(grid, pod)
                for step_cost, pos in moves:
                    new_pods = pods[:i] + (Pod(pos=pos, type=pod.type),) + pods[i + 1:]
                    distance = sum(self.distance_home(pod) for pod in new_pods)
                    if (c_item := (cost + step_cost,) + new_pods) not in cache:
                        cache.add(c_item)
                        new_state = ((distance, cost + step_cost),
                                     new_pods,
                                     path + [(i, step_cost, pod[1], (pod[0], pos))])
                        heappush(to_visit, new_state)
        return 0


class Dec23(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 23, instructions, filename)
        self.grid, self.pods, self.targets = self.instructions

    @staticmethod
    def parse_instructions(instructions):
        pods = dict()
        rooms = dict()
        grid = dict()

        for y, line in enumerate(instructions):
            for x, ch in enumerate(line):
                if ch not in ('#', '.', ' '):
                    pods[(y, x)] = ch
                grid[(y, x)] = ch
        prev_x = None
        assignment = 'A'
        for (y, x) in sorted(pods.keys(), key=lambda c: c[1]):
            if prev_x and x != prev_x:
                assignment = chr(ord(assignment) + 1)
            rooms[(y, x)] = assignment
            prev_x = x
        return grid, pods, rooms

    @timer(part=1)
    def part_1(self):
        burrow = PodBurrow(pods=self.pods,
                           grid=self.grid,
                           rooms=self.targets)
        return burrow.organize()

    @timer(part=2)
    def part_2(self):
        return 2


if __name__ == '__main__':
    with Timer('Amphipod'):
        Dec23().run_day()
