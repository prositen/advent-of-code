from collections import defaultdict
from enum import StrEnum
from typing import List

from python.src.common import Day, timer, Timer, get_points_between


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
        self.visited = defaultdict(set)
        self.facing = Facing.North
        self.max_y = len(lab_map)
        self.max_x = len(lab_map[0])
        self.obstacles_by_row = defaultdict(lambda: {-2, self.max_y + 1})
        self.obstacles_by_col = defaultdict(lambda: {-2, self.max_x + 1})
        self.added_obstacle = None
        for y, row in enumerate(lab_map):
            for x, col in enumerate(row):
                if col == '^':
                    self.start_pos = self.pos = (y, x)
                    self.visited[self.pos].add(self.facing)
                elif col == '#':
                    self.obstacles_by_row[y].add(x)
                    self.obstacles_by_col[x].add(y)

    def in_bounds(self, pos):
        return 0 <= pos[0] < self.max_y and 0 <= pos[1] < self.max_x

    def patrol(self):
        while self.in_bounds(pos := self.teleport(self.pos, self.facing)):
            for p in get_points_between(pos, self.pos):
                self.visited[p].add(self.facing)
            self.facing = self.facing.turn_right()
            self.pos = pos
        for p in get_points_between(pos, self.pos):
            if self.in_bounds(p):
                self.visited[p].add(self.facing)
        return len(self.visited)

    def is_loop(self, add_pos):
        self.reset_and_set_pos(add_pos=add_pos)
        while self.in_bounds(pos := self.teleport(self.pos, self.facing)):
            if self.facing in self.visited.get(pos, set()):
                return pos != self.start_pos
            self.visited[pos].add(self.facing)
            self.facing = self.facing.turn_right()
            self.pos = pos
        return 0

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

    def reset_and_set_pos(self, add_pos):
        self.visited = defaultdict(set)
        self.facing = Facing.North
        self.pos = self.start_pos
        if self.added_obstacle:
            self.obstacles_by_row[self.added_obstacle[0]].discard(self.added_obstacle[1])
            self.obstacles_by_col[self.added_obstacle[1]].discard(self.added_obstacle[0])

        self.obstacles_by_row[add_pos[0]].add(add_pos[1])
        self.obstacles_by_col[add_pos[1]].add(add_pos[0])
        self.added_obstacle = add_pos


class Dec06(Day, year=2024, day=6, title='Guard Gallivant'):

    @timer(part=1)
    def part_1(self):
        gp = GuardPatrol(self.instructions)
        return gp.patrol()

    @timer(part=2)
    def part_2(self):
        gp = GuardPatrol(self.instructions)
        gp.patrol()
        gp.visited.pop(gp.start_pos)
        return sum(gp.is_loop(add_pos=pos) for pos in gp.visited)


if __name__ == '__main__':
    with Timer('Total'):
        Dec06().run_day()
