import os
from python.src.y2017.common import DATA_DIR


class Virus(object):
    DIRS = {
        'up': (-1, 0),
        'right': (0, 1),
        'down': (1, 0),
        'left': (0, -1)
    }

    STATES = {
        'clean': False,
        'infected': True
    }

    R = {
        False: '.',
        True: '#'
    }

    def turn(self, turn_right):
        if self.d == 'up':
            self.d = 'right' if turn_right else 'left'
        elif self.d == 'right':
            self.d = 'down' if turn_right else 'up'
        elif self.d == 'down':
            self.d = 'left' if turn_right else 'right'
        else:
            self.d = 'up' if turn_right else 'down'

    def walk(self):
        self.p = self.p[0] + self.DIRS[self.d][0], self.p[1] + self.DIRS[self.d][1]
        self.ymin = min(self.ymin, self.p[0])
        self.ymax = max(self.ymax, self.p[0])
        self.xmin = min(self.xmin, self.p[1])
        self.xmax = max(self.xmax, self.p[1])

    def get(self, y=None, x=None):
        if y is None:
            y = self.p[0]
        if x is None:
            x = self.p[1]
        row = self.grid.get(y)
        if not row:
            self.grid[y] = dict()
            row = dict()
        return row.get(x, self.STATES['clean'])

    def set(self, sq):
        self.grid[self.p[0]][self.p[1]] = sq

    def work(self):
        sq = self.get()
        self.set(not sq)
        if not sq:
            self.infect += 1
        self.turn(sq)

    def step(self, count):
        for _ in range(count):
            self.work()
            self.walk()
            if self.show:
                self.pp()

    def __init__(self, puzzle_input, show=False):
        self.d = 'up'
        self.infect = 0
        self.grid = dict()
        self.set_grid(puzzle_input)
        m = (len(puzzle_input) // 2)
        self.p = (m, m)
        self.ymin = 0
        self.ymax = len(puzzle_input)
        self.xmin = 0
        self.xmax = self.ymax
        self.show = show

    def set_grid(self, puzzle_input):
        for ri, r in enumerate(puzzle_input):
            self.grid[ri] = {ci: c == '#' for ci, c in enumerate(r)}

    def pp(self):
        print("Infected:", self.infect)
        for y in range(self.ymin, self.ymax):
            row = []
            for x in range(self.xmin, self.xmax):
                c = self.R[self.get(y, x)]
                if self.p[0] == y and self.p[1] == x:
                    row.append("[{}]".format(c))
                else:
                    row.append(" {} ".format(c))
            print("".join(row))
        print()


class EvolvedVirus(Virus):
    state_CLEAN = 0
    state_WEAK = 1
    state_INFECTED = 2
    state_FLAGGED = 3

    STATES = {
        'clean': state_CLEAN,
        'weakened': state_WEAK,
        'infected': state_INFECTED,
        'flagged': state_FLAGGED
    }
    R = {
        state_CLEAN: '.',
        state_INFECTED: '#',
        state_WEAK: 'W',
        state_FLAGGED: 'F'
    }

    def turn(self, current_node):
        if current_node == self.state_CLEAN:
            Virus.turn(self, False)
        elif current_node == self.state_WEAK:
            pass
        elif current_node == self.state_INFECTED:
            Virus.turn(self, True)
        else:
            if self.d == 'up':
                self.d = 'down'
            elif self.d == 'right':
                self.d = 'left'
            elif self.d == 'down':
                self.d = 'up'
            else:
                self.d = 'right'

    def work(self):
        sq = self.get()
        self.turn(sq)
        if sq == self.state_WEAK:
            self.infect += 1
        sq = (sq + 1) % 4
        self.set(sq)

    def set_grid(self, puzzle_input):
        for ri, r in enumerate(puzzle_input):
            self.grid[ri] = {
                ci: self.state_INFECTED if c == '#' else self.state_CLEAN
                for ci, c in enumerate(r)
            }


def main():
    with open(os.path.join(DATA_DIR, 'input.22.txt')) as fh:
        puzzle_input = fh.readlines()

    v = Virus(puzzle_input)
    v.step(10000)
    print("Part 1: ", v.infect)

    v = EvolvedVirus(puzzle_input)
    v.step(10000000)
    print("Part 2: ", v.infect)


if __name__ == '__main__':
    main()
