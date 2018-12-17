import copy
import re

from python.src.common import Day

READING_ORDER = [(-1, 0), (0, -1), (0, 1), (1, 0)]


class Fighter(object):
    def __init__(self, x, y, attack_strength=3):
        self.x = x
        self.y = y
        self.attack_strength = attack_strength
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
        if self.target:
            if not self.target.attacked(self):
                self.enemies.remove(self.target)

    def open_squares(self, cave):
        return [(self.y+dy, self.x+dx)
                for dy, dx in READING_ORDER
                if cave.grid[self.y+dy][self.x+dx] == '.']

    def calculate_target(self):
        adjacent = [e for e in self.enemies if e.hp > 0 and self.distance(e) <= self.range]
        if adjacent:
            self.target = sorted(adjacent, key=lambda e: (e.hp, e.y, e.x))[0]
        else:
            self.target = None

    def move(self, cave):
        self.calculate_target()
        if self.target:
            return
        open_squares = []
        for e in self.enemies:
            open_squares.extend(e.open_squares(cave))

        if open_squares:
            closest_path = cave.distances(self.y, self.x, set(open_squares))
            if closest_path:
                self.y, self.x = closest_path[1]
                self.calculate_target()

    def __repr__(self):
        return '<{} pos={} hp={}>'.format(self.__class__.__name__,
                                          (self.y, self.x), self.hp)


class Gobbo(Fighter):
    pass


class Elf(Fighter):
    pass


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

    def distances(self, y_pos, x_pos, blocks):
        """ Calculate the nearest of the goal blocks from the start position"""
        visited = {(y_pos, x_pos)}
        to_visit = list()
        to_visit.append([(y_pos, x_pos)])
        while to_visit:
            path = to_visit.pop(-1)
            y, x = path[-1]
            if (y, x) in blocks:
                return path
            for dy, dx in READING_ORDER:
                xx, yy = x + dx, y + dy
                if self.grid[yy][xx] == '.' \
                        and (yy, xx) not in visited:
                    to_visit.append(path + [(yy, xx)])
                    visited.add((yy, xx))
            to_visit = sorted(to_visit, key=lambda path: (len(path), path[-1]), reverse=True)
        return []


class Game(object):
    def __init__(self, cave_map, gobbos, elves, elf_power=3):
        self.cave_map = Cave(cave_map)
        self.gobbos, self.elves = copy.deepcopy(gobbos), copy.deepcopy(elves)
        for e in self.elves:
            e.attack_strength = elf_power

        for g in self.gobbos:
            g.enemies = self.elves
        for e in self.elves:
            e.enemies = self.gobbos

    def play_turn(self):
        fighters = sorted(self.gobbos + self.elves, key=lambda f: (f.y, f.x))
        for fighter in fighters:
            if fighter.hp <= 0:
                continue
            if not fighter.enemies:
                return fighters.index(fighter) == 0, False
            cave = self.cave_map.current_state(gobbos=self.gobbos, elves=self.elves)
            fighter.move(cave)
            fighter.attack()
        return True, self.gobbos and self.elves

    def score(self, turn):
        return turn * sum(f.hp for f in self.gobbos + self.elves if f.hp > 0)


class Dec15(Day):
    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 15, instructions, filename)
        self.cavemap, self.gobbos, self.elves = self.instructions

    @staticmethod
    def parse_instructions(instructions):
        gobbos = list()
        elves = list()
        cave_map = list()
        for y, line in enumerate(instructions):
            line = line.strip()
            for m in re.finditer('[GE]', line):
                if m.group(0) == 'G':
                    gobbos.append(Gobbo(x=m.start(), y=y))
                else:
                    elves.append(Elf(x=m.start(), y=y))
            cave_map.append(line.replace('G', '.').replace('E', '.'))
        return cave_map, gobbos, elves

    def run(self, power=3):
        turn = 0
        game = Game(self.cavemap, self.gobbos, self.elves, elf_power=power)
        while True:
            full_turn, both_teams_alive = game.play_turn()
            if not both_teams_alive:
                return game.score(turn + int(full_turn)), len(game.elves) == len(self.elves), turn
            turn += 1

    def part_1(self):
        return self.run()[0]

    def part_2(self):
        elf_strength = 4
        while True:
            score, elves_won, turns = self.run(elf_strength)
            if elves_won:
                return score
            else:
                elf_strength += 1


if __name__ == '__main__':
    d = Dec15()
    print("Outcome:", d.part_1())
    print("Outcome for stronger elves", d.part_2())
