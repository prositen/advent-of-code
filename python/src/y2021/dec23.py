import itertools
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
        self.room_y = set()
        self.burrow = {
            Point(y=1, x=x): '.' for x in range(1, self.max_x)
        }
        for pos, pod_type in rooms.items():
            self.burrow[Point(y=pos[0], x=pos[1])] = '.'
            self.room_x[pod_type] = pos[1]
            self.room_y.add(pos[0])
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
        is_in_right_room = pod.pos.x == tx
        others_in_room = any(grid[Point(y=ty, x=tx)] not in ('.', pod.type)
                             for ty in self.room_y)
        empty_above = all(grid[Point(y=ty, x=tx)] == '.' for ty in range(2, pod.pos.y))

        return empty_above and (others_in_room or not is_in_right_room)

    def move_in(self, grid, pod: Pod):
        tx = self.room_x[pod.type]
        target = ((Point(y=ty, x=tx) for ty in self.room_y))
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
        for x in range(px + sgn, target_x, sgn):
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
            for y in self.room_y
        )
        return '\n'.join(r)

    def distance(self, pods):
        sorted_pods = dict()
        for pod in pods:
            if pod.type not in sorted_pods:
                sorted_pods[pod.type] = list()
            sorted_pods[pod.type].append(pod.pos)
        dist = 0
        for pod_type, ps in sorted_pods.items():
            tx = self.room_x[pod_type]
            diffs = {
                pd: [abs(pd.x - tx) + (abs(pd.y - ty) if pd.x == tx else (pd.y - 1 + ty))
                     for ty in self.room_y]
                for pd in ps
            }
            sums = tuple(
                sum(
                    diffs[pd][i]
                    for i, pd in enumerate(pod_list)
                )
                for pod_list in itertools.permutations(ps)
            )
            cost = min(sums)
            # cost = sum(pd.x == tx for pd in ps)
            dist += self.COSTS[pod_type] * cost
        return dist

    def organize(self):
        to_visit = [((self.distance(self.pods), 0), self.pods)]
        cache = dict()
        while to_visit:
            (_, cost), pods = heappop(to_visit)
            if pods in cache and cache[pods] < cost:
                continue
            cache[pods] = cost
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
        print("derp")
        return 0

    def reorganize(self):
        to_visit = {self.pods: (0, [])}
        while to_visit:
            next_visit = dict()
            for pods, cost in to_visit.items():
                if self.all_home(pods):
                    return cost
                grid = {**self.burrow}
                for pod in pods:
                    grid[pod.pos] = pod.type
                for i, pod in enumerate(pods):
                    moves = self.possible_moves(grid, pod)
                    for step_cost, pos in moves:
                        new_pods = pods[:i] + (Pod(pos=pos, type=pod.type),) + pods[i + 1:]
                        new_cost = cost[0] + step_cost
                        if new_pods in next_visit and next_visit[new_pods][0] <= new_cost:
                            continue
                        next_visit[new_pods] = (new_cost, cost[1] + [(pod.type, pod.pos, pos)])
            to_visit = next_visit
        return 0


class Dec23(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 23, instructions, filename)
        self.grid, self.pods, self.targets, self.original = self.instructions

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
        return grid, pods, rooms, instructions

    @timer(part=1)
    def part_1(self):
        burrow = PodBurrow(pods=self.pods,
                           grid=self.grid,
                           rooms=self.targets)
        return burrow.reorganize()

    @timer(part=2)
    def part_2(self):
        new_instructions = self.original[:3] + [
            "  #D#C#B#A#  ",
            "  #D#B#A#C#  "
        ] + self.original[3:]
        self.grid, self.pods, self.targets, _ = self.parse_instructions(new_instructions)
        burrow = PodBurrow(pods=self.pods,
                           grid=self.grid,
                           rooms=self.targets)
        return burrow.organize()


if __name__ == '__main__':
    with Timer('Amphipod'):
        Dec23().run_day()
