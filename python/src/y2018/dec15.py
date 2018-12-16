import re
from collections import deque

from python.src.common import Day


class Fighter(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.attack = 3
        self.range = 1
        self.hp = 200
        self.enemies = None
        self.target = None

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def attacked(self, fighter):
        self.hp -= fighter.attack

    def adjacent_enemies(self):
        adjacent = [e for e in self.enemies if e.hp > 0 and self.distance(e) <= self.range]
        if adjacent:
            return sorted(adjacent, key=lambda e: (e.hp, e.y, e.x))

    def move(self, cave):
        adjacent = self.adjacent_enemies()
        if adjacent:
            self.target = adjacent[0]
            return
        squares = []
        for e in self.enemies:
            if e.hp > 0:
                squares += cave.open_square(e)
        if squares:
            a = sorted(cave.distances(self.x, self.y, set(squares)),
                       key=lambda c: len(c[2]))
            print(a)


class Gobbo(Fighter):
    def __repr__(self):
        return '<Gobbo pos={} hp={}>'.format((self.x, self.y), self.hp)


class Elf(Fighter):
    def __repr__(self):
        return '<Elf pos={} hp={}>'.format((self.x, self.y), self.hp)


class Cave(object):

    def __init__(self, grid):
        self.grid = grid

    def current_state(self, gobbos, elves):
        current = [[c for c in row] for row in self.grid]
        for gobbo in gobbos:
            current[gobbo.y][gobbo.x] = 'G'
        for elf in elves:
            current[elf.y][elf.x] = 'E'
        return Cave(current)

    def open_square(self, fighter):
        squares = [(fighter.x, fighter.y - 1),
                   (fighter.x + 1, fighter.y),
                   (fighter.x, fighter.y + 1),
                   (fighter.x - 1, fighter.y)]
        return [(x, y) for (x, y) in squares if self.grid[y][x] == '.']

    def distances(self, start_x, start_y, blocks):
        """ Calculate the distance from the start position to all other non-wall positions """
        paths = {(start_x, start_y): 0}
        visited = set()
        to_visit = deque()
        to_visit.append((start_x, start_y, []))
        while to_visit:
            (x, y, path) = to_visit.pop()
            if (x, y) not in visited or len(paths.get((x, y), path + 1)) > len(path):
                paths[(x, y)] = path
            visited.add((x, y))
            for dx, dy in [(0, -1), (-1, 0), (0, 1), (0, 1)]:
                xx, yy = x + dx, y + dy
                if self.grid[yy][xx] == '.':
                    to_visit.append((xx, yy, path + [(x, y)]))
        return [(x, y, dist) for x, y, dist in
                [(b[0], b[1], paths.get(b, None)) for b in blocks] if d is not None]


class Game(object):
    def __init__(self, cave_map, gobbos, elves):
        self.cave_map = Cave(cave_map)
        self.gobbos, self.elves = gobbos, elves
        for g in self.gobbos:
            g.enemies = self.elves
        for e in self.elves:
            e.enemies = self.gobbos

    @staticmethod
    def any_alive(fighters):
        return any(fighter for fighter in fighters if fighter.hp > 0)

    def play_turn(self):
        fighters = sorted(self.gobbos + self.elves, key=lambda f: (f.y, f.x))
        for fighter in fighters:
            if fighter.hp <= 0:
                continue
            if not self.any_alive(fighter.enemies):
                return False
            cave = self.cave_map.current_state(gobbos=self.gobbos, elves=self.elves)
            fighter.move(cave)
            self.attack(fighter)
        return self.any_alive(self.gobbos) and self.any_alive(self.elves)

    def attack(self, fighter):
        pass

    def score(self, turn):
        return turn * sum(f.hp for f in self.gobbos + self.elves if f.hp > 0)


class Dec15(Day):
    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 15, instructions, filename)
        cavemap, gobbos, elves = self.instructions
        self.game = Game(cavemap, gobbos, elves)

    @staticmethod
    def parse_instructions(instructions):
        gobbos = list()
        elves = list()
        cave_map = list()
        for y, line in enumerate(instructions):
            for m in re.finditer('[GE]', line):
                if m.group(0) == 'G':
                    gobbos.append(Gobbo(x=m.start(), y=y))
                else:
                    elves.append(Elf(x=m.start(), y=y))
            cave_map.append(line.replace('G', '.').replace('E', '.'))
        return cave_map, gobbos, elves

    def part_1(self):
        turn = 0
        while True:
            turn += 1
            if not self.game.play_turn():
                return self.game.score(turn)

    def part_2(self):
        pass


if __name__ == '__main__':
    d = Dec15()
    print("Outcome:", d.part_1())
