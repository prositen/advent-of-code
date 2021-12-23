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
        self.pods = [(
            pos, pod_type, False
        ) for pos, pod_type in pods.items()]

        self.grid = grid

    def can_move(self, grid, pod):
        return bool(self.possible_moves(grid, pod))

    def possible_moves(self, grid, pod):
        def distance(pos1, pos2):
            return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

        pos, pod_type, left_room = pod
        cost = self.COSTS[pod_type]
        if left_room:
            if pos[0] > 1:
                return []
            # Only possible positions are the target room positions
            target = self.rooms[pod_type]
            target_x = target[0][0]
            if any((grid[(1, x)] != '.')
                   for x in range(target_x, pos[1], 1 if pos[1] < target_x else -1)):
                # There's someone in the way in the corridor
                return []
            elif any((grid[t] not in (pod_type, '.')) for t in target):
                # There's someone of the wrong type in the room
                return []
            else:
                new_pos = max(t for t in target if grid[t] == '.')
                return [(cost * distance(pos, new_pos), new_pos)]
        elif pos[0]:
            if grid[(pos[0] - 1, pos[1])] != '.':
                # Someone in the way above me
                return []
            positions = list()
            for x in range(pos[1], 0, -1):
                if grid[(1, x)] == '.':
                    if x not in self.room_x.values():
                        positions.append((cost * distance(pos, (1, x)), (1, x)))
                else:
                    break
            for x in range(pos[1], self.max_x):
                if grid[(1, x)] == '.':
                    if x not in self.room_x.values():
                        positions.append((cost * distance(pos, (1, x)), (1, x)))
                else:
                    break
            return positions

    def all_home(self, grid):
        for k, v in self.rooms.items():
            for pos in v:
                if grid[pos] != k:
                    return False
        return True


    def organize(self):
        to_visit = [(0, self.pods.copy(), self.grid.copy())]
        cache = set()
        while to_visit:
            cost, pods, grid = heappop(to_visit)
            if self.all_home(grid):
                return cost
            for i, pod in enumerate(pods):
                for step_cost, pos in self.possible_moves(grid, pod):
                    new_grid = grid.copy()
                    new_grid[pod[0]] = '.'
                    new_grid[pos] = pod[1]
                    new_pods = pods.copy()
                    new_pods[i] = (pos, pod[1], True)
                    state = f'{new_pods}'
                    if state not in cache:
                        cache.add(state)
                        heappush(to_visit, (cost + step_cost, new_pods, new_grid))
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
