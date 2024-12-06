from collections import defaultdict
from enum import auto, IntEnum
from typing import List

from python.src.common import Day, timer, Timer


class Facing(IntEnum):
    North = auto()
    East = auto()
    South = auto()
    West = auto()

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
        self.possible_obstacles = set()
        for y, row in enumerate(lab_map):
            if (x := row.find('^')) > -1:
                self.pos = (y, x)
                self.start_pos = (y, x)
                self.map[y][x] = '.'
                self.visited[self.pos].add(self.facing)
                break

    def patrol(self, add_obstacles=False, detect_loops=False):
        next_pos = self.pos
        while 0 <= next_pos[0] < len(self.map) and 0 <= next_pos[1] < len(self.map[0]):
            if '.' != self.map[next_pos[0]][next_pos[1]]:
                self.facing = self.facing.turn_right()
            else:
                if detect_loops and self.facing in self.visited.get(next_pos, set()):
                    return True
                self.pos = next_pos
                if add_obstacles and self.scan_ahead():
                    self.possible_obstacles.add(self.facing.position_ahead(next_pos))
                self.visited[next_pos].add(self.facing)
            next_pos = self.facing.position_ahead(self.pos)

        if add_obstacles:
            self.possible_obstacles.discard(self.start_pos)
            return len(self.possible_obstacles)
        elif detect_loops:
            return False
        else:
            return len(self.visited)

    def scan_ahead(self):
        possible_turn = self.facing.turn_right()
        next_pos = possible_turn.position_ahead(self.pos)
        while 0 <= next_pos[0] < len(self.map) and 0 <= next_pos[1] < len(self.map[0]):
            if '.' != self.map[next_pos[0]][next_pos[1]]:
                return False
            if possible_turn in self.visited.get(next_pos, set()):
                return True
            next_pos = possible_turn.position_ahead(next_pos)

    def reset_and_set_pos(self, add_pos, remove_pos=None):
        self.visited = defaultdict(set)
        self.facing = Facing.North
        self.pos = self.start_pos
        self.map[add_pos[0]][add_pos[1]] = '#'
        if remove_pos:
            self.map[remove_pos[0]][remove_pos[1]] = '.'


class Dec06(Day, year=2024, day=6, title='Guard Gallivant'):

    @timer(part=1)
    def part_1(self):
        gp = GuardPatrol(self.instructions)
        return gp.patrol()

    @timer(part=2)
    def part_2(self):
        gp = GuardPatrol(self.instructions)
        gp.patrol()
        remove_pos = None
        num_obstacles = 0
        gp.visited.pop(gp.start_pos, None)
        for pos in list(gp.visited):
            gp.reset_and_set_pos(add_pos=pos, remove_pos=remove_pos)
            if gp.patrol(detect_loops=True):
                num_obstacles += 1
            remove_pos = pos
        return num_obstacles


if __name__ == '__main__':
    with Timer('Total'):
        Dec06().run_day()
