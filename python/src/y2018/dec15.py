import re
from collections import deque

from python.src.common import Day


class Fighter(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.attack_strength = 3
        self.range = 1
        self.hp = 200
        self.enemies = None
        self.target = None

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def attacked(self, fighter):
        self.hp -= fighter.attack_strength
        return self.hp > 0

    def attack(self):
        if self.target and self.distance(self.target) <= self.range:
            if not self.target.attacked(self):
                self.enemies.remove(self.target)

    def calculate_target(self):
        adjacent = [e for e in self.enemies if e.hp > 0 and self.distance(e) <= self.range]
        if adjacent:
            self.target = sorted(adjacent, key=lambda e: (e.hp, e.y, e.x))[0]
            return True
        self.target = None
        return False

    def move(self, cave):
        if self.calculate_target():
            return

        squares = []
        for e in self.enemies:
            if e.hp > 0:
                squares += cave.open_square(e)
        if squares:
            squares = sorted(cave.distances(self.x, self.y, set(squares)),
                             key=lambda c: (len(c[2]), c[1], c[0]))
            if squares:
                closest = squares[0]
                path = closest[2]
                if len(path) > 1:
                    self.x, self.y = path[1]
                else:
                    self.x, self.y = closest[0], closest[1]
                    self.calculate_target()



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
        paths = {(start_x, start_y): []}
        visited = set()
        to_visit = deque()
        to_visit.append((start_x, start_y, []))
        while to_visit:
            (x, y, path) = to_visit.popleft()
            if (x, y) not in visited or len(paths.get((x, y))) > len(path):
                paths[(x, y)] = path
            visited.add((x, y))
            for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                xx, yy = x + dx, y + dy
                if 0 < yy < len(self.grid) \
                        and 0 < xx < len(self.grid[0]) \
                        and (xx,yy) not in path \
                        and (xx,yy) not in visited \
                        and self.grid[yy][xx] == '.':
                    to_visit.append((xx, yy, path + [(x, y)]))
        return [(x, y, dist) for x, y, dist in
                [(b[0], b[1], paths.get(b, None)) for b in blocks] if dist is not None]


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
                return False, False
            cave = self.cave_map.current_state(gobbos=self.gobbos, elves=self.elves)
            fighter.move(cave)
            fighter.attack()
        return True, self.any_alive(self.gobbos) and self.any_alive(self.elves)

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
            full_turn, both_teams_alive = self.game.play_turn()
            if not both_teams_alive:
                return self.game.score(turn + int(full_turn))
            x = self.game.cave_map.current_state(self.game.gobbos, self.game.elves)
            turn += 1


    def part_2(self):
        pass


if __name__ == '__main__':
    d = Dec15()
    print("Outcome:", d.part_1())
