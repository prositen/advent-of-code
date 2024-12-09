from collections import defaultdict
from enum import StrEnum
from typing import List

from python.src.common import Day, timer, Timer


class Facing(StrEnum):
    North = 'north'
    East = 'east'
    South = 'south'
    West = 'west'

    def turn_right(self):
        match self.value:
            case Facing.North:
                return Facing.East
            case Facing.East:
                return Facing.South
            case Facing.South:
                return Facing.West
            case Facing.West:
                return Facing.North

    def position_ahead(self, pos):
        match self.value:
            case Facing.North:
                return pos[0] - 1, pos[1]
            case Facing.East:
                return pos[0], pos[1] + 1
            case Facing.South:
                return pos[0] + 1, pos[1]
            case Facing.West:
                return pos[0], pos[1] - 1


class GuardPatrol(object):
    def __init__(self, lab_map: List[str]):
        self.map = [[c for c in row] for row in lab_map]
        self.visited = defaultdict(set)
        self.facing = Facing.North
        max_y = len(self.map)
        max_x = len(self.map[0])
        self.obstacles_by_row = defaultdict(lambda: {-1, max_y + 1})
        self.obstacles_by_col = defaultdict(lambda: {-1, max_x + 1})
        for y, row in enumerate(lab_map):
            for x, col in enumerate(row):
                if col == '^':
                    self.pos = (y, x)
                    self.start_pos = (y, x)
                    self.map[y][x] = '.'
                    self.visited[self.pos].add(self.facing)
                elif col == '#':
                    self.obstacles_by_row[y].add(x)
                    self.obstacles_by_col[x].add(y)

    def patrol(self, add_obstacles=False, detect_loops=False):
        next_pos = self.pos
        obstacles = 0
        while 0 <= next_pos[0] < len(self.map) and 0 <= next_pos[1] < len(self.map[0]):
            if '.' != self.map[next_pos[0]][next_pos[1]]:
                self.facing = self.facing.turn_right()
            else:
                if detect_loops and self.facing in self.visited.get(next_pos, set()):
                    return next_pos != self.start_pos
                self.pos = next_pos
                if add_obstacles and self.scan_ahead():
                    obstacles += 1
                self.visited[next_pos].add(self.facing)
            next_pos = self.facing.position_ahead(self.pos)

        if add_obstacles:
            return obstacles
        elif detect_loops:
            return False
        else:
            return len(self.visited)

    def patrol2(self):
        next_pos = self.pos
        while 0 <= next_pos[0] < len(self.map) and 0 <= next_pos[1] < len(self.map[0]):
            if '.' != self.map[next_pos[0]][next_pos[1]]:
                self.facing = self.facing.turn_right()
            else:
                if self.facing in self.visited.get(next_pos, set()):
                    return True
                self.pos = next_pos
                self.visited[next_pos].add(self.facing)
            next_pos = self.facing.position_ahead(self.pos)
        return False

    def is_loop(self):
        next_pos = self.pos
        while 0 <= next_pos[0] < len(self.map) and 0 <= next_pos[1] < len(self.map[0]):
            next_pos = self.teleport(next_pos, self.facing)
            if self.facing in self.visited.get(next_pos, set()):
                return next_pos != self.start_pos
            self.visited[next_pos].add(self.facing)
            self.facing = self.facing.turn_right()

    def teleport(self, pos, facing):
        obs_y, obs_x = pos
        match facing:
            case Facing.North:
                obs_y = max(y for y in self.obstacles_by_col[pos[1]]
                            if y < pos[0]) + 1
            case Facing.East:
                obs_x = min(x for x in self.obstacles_by_row[pos[0]]
                            if x > pos[1]) - 1
            case Facing.South:
                obs_y = min(y for y in self.obstacles_by_col[pos[1]]
                            if y > pos[0]) - 1
            case Facing.West:
                obs_x = max(x for x in self.obstacles_by_row[pos[0]]
                            if x < pos[1]) + 1
        return obs_y, obs_x

    def scan_ahead(self):
        next_facing = self.facing.turn_right()
        next_pos = self.teleport(self.pos, next_facing)
        return next_facing in self.visited.get(next_pos, set())

    def reset_and_set_pos(self, add_pos, remove_pos=None):
        self.visited = defaultdict(set)
        self.facing = Facing.North
        self.pos = self.start_pos
        if remove_pos:
            self.obstacles_by_row[remove_pos[0]].discard(remove_pos[1])
            self.obstacles_by_col[remove_pos[1]].discard(remove_pos[0])
            self.map[remove_pos[0]][remove_pos[1]] = '.'

        self.obstacles_by_row[add_pos[0]].add(add_pos[1])
        self.obstacles_by_col[add_pos[1]].add(add_pos[0])
        self.map[add_pos[0]][add_pos[1]] = '#'


class Dec06(Day, year=2024, day=6, title='Guard Gallivant'):

    @timer(part=1)
    def part_1(self):
        gp = GuardPatrol(self.instructions)
        return gp.patrol()

    @timer(part=2)
    def part_2_breezy(self):
        gp = GuardPatrol(self.instructions)
        return gp.patrol(add_obstacles=True)

    def part_2(self):
        return self.part_2_brute()

    @timer(part=2)
    def part_2_brute(self):
        gp = GuardPatrol(self.instructions)
        gp.patrol()
        remove_pos = None
        num_obstacles = 0
        gp.visited.pop(gp.start_pos)
        for pos in list(gp.visited):
            gp.reset_and_set_pos(add_pos=pos, remove_pos=remove_pos)
            if gp.patrol2():  # gp.is_loop():
                num_obstacles += 1
            remove_pos = pos
        return num_obstacles


if __name__ == '__main__':
    with Timer('Total'):
        Dec06().run_day()
