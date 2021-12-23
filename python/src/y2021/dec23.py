from collections import defaultdict
from heapq import heappush, heappop

from python.src.common import Day, timer, Timer


class PodBurrow(object):
    COSTS = {
        'A': 1,
        'B': 10,
        'C': 100,
        'D': 1000
    }

    def __init__(self, grid, pods, rooms):
        self.rooms = defaultdict(list)
        self.max_x = max(grid, key=lambda c: c[1])[1]
        self.room_x = dict()
        for pos, pod_type in rooms.items():
            self.rooms[pod_type].append(pos)
            self.room_x[pod_type] = pos[1]
        self.pods = tuple((pos, pod_type, False) for pos, pod_type in pods.items())

    def cost_distance(self, pod_type, pos1, pos2):
        return self.COSTS[pod_type] * (abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]))

    def distance_home(self, pod):
        return abs(pod[0][1] - self.room_x[pod[1]]) + abs(pod[0][0] - 2)

    def move_to_corridor(self, pod, grid):
        (py, px), pod_type, left_room = pod
        for r in (range(px, 0, -1), range(px, self.max_x)):
            for x in r:
                if grid[(1, x)] != '.':
                    break
                if x not in self.room_x.values():
                    yield self.cost_distance(pod_type, (py, px), (1, x)), (1, x)

    def possible_moves(self, grid, pod):
        pos, pod_type, left_room = pod
        if left_room:
            if pos[0] > 1:
                return []
            # Only possible positions are the target room positions
            target = self.rooms[pod_type]
            target_x = self.room_x[pod_type]
            if any((grid[(1, x)] != '.')
                   for x in range(target_x, pos[1], 1 if pos[1] < target_x else -1)):
                # There's someone in the way in the corridor
                return []
            elif any((grid.get(t, '.') not in (pod_type, '.')) for t in target):
                # There's someone of the wrong type in the room
                return []
            else:
                new_pos = max(t for t in target if grid.get(t, '.') == '.')
                return [(self.cost_distance(pod_type, pos, new_pos), new_pos)]
        elif pos[0] > 1:
            if pos[1] == self.room_x[pod_type] and pos[0] == 3:
                return []

            if grid.get((pos[0] - 1, pos[1]), '.') != '.':
                # Someone in the way above me
                return []
            return [p for p in self.move_to_corridor(pod, grid)]

    def all_home(self, pods):
        for (pos, pod_type, left_room) in pods:
            if pos[0] == 1 or pos[1] != self.room_x[pod_type]:
                return False
        return True

    def print_grid(self, grid):
        r = [''.join(grid[(1, x)] for x in range(1, self.max_x))]
        r.extend(
            '  ' + '#'.join(grid.get((y, x), '.') for x in (3, 5, 7, 9))
            for y in (2, 3)
        )
        return '\n'.join(r)

    def organize(self):
        to_visit = [((sum(self.distance_home(pod) for pod in self.pods), 0), self.pods, [])]
        cache = set()
        while to_visit:
            grid = {(1, x): '.' for x in range(1, 12)}
            (step, cost), pods, path = heappop(to_visit)
            for pos, pod_type, _ in pods:
                grid[pos] = pod_type
            if self.all_home(pods):
                return cost

            for i, pod in enumerate(pods):
                moves = self.possible_moves(grid, pod)
                for step_cost, pos in moves:
                    new_pods = pods[:i] + ((pos, pod[1], True),) + pods[i + 1:]
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
