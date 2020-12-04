from collections import defaultdict, deque

from python.src.common import Day, timer
from python.src.y2019.intcode import IntCode


class Tile(object):
    Wall = 0
    Empty = 1
    Oxygen = 2
    Drone = 3

    SHOW = {
        Empty: ' ',
        Wall: '#',
        Oxygen: 'O',
        Drone: 'D'
    }


class Ship(object):

    def __init__(self, instructions):
        self.instructions = instructions
        self.grid = defaultdict(dict)
        self.drone = 0, 0
        self.oxygen = 0, 0
        self.min_x, self.max_x = 0, 0

    def fill_map(self):
        to_visit = deque()
        visited = set()
        x, y = self.drone
        min_path = None
        oxygen_pos = 0, 0
        ic = IntCode(instructions=self.instructions)
        for d in 1, 2, 3, 4:
            to_visit.append((ic.clone(), (x, y), d, []))
        self.grid[y][x] = Tile.Empty
        while to_visit:
            ic, (x, y), d, path = to_visit.popleft()
            visited.add((x, y))
            ic.add_input(d)
            ic.run_and_wait()
            status = ic.get_output()

            nx, ny = self.update_pos(x, y, direction=d)
            self.min_x = min(self.min_x, nx)
            self.max_x = max(self.max_x, nx)
            self.grid[ny][nx] = status
            if status != Tile.Wall:
                x, y = nx, ny
                if status == Tile.Oxygen:
                    if not min_path or len(min_path) > len(path):
                        min_path = path + [(x, y)]
                        oxygen_pos = x, y
                if (x, y) not in visited:
                    for d in 1, 2, 3, 4:
                        nx, ny = self.update_pos(x, y, d)
                        if (nx, ny) not in visited:
                            to_visit.append((ic.clone(), (x, y), d, path + [(x, y)]))

        self.oxygen = oxygen_pos
        return min_path

    @staticmethod
    def update_pos(x, y, direction):
        if direction == 1:
            return x, y - 1
        elif direction == 2:
            return x, y + 1
        elif direction == 3:
            return x - 1, y
        elif direction == 4:
            return x + 1, y

    def print(self):
        c = self.grid[0].get(0, 0)
        self.grid[0][0] = Tile.Drone
        for row in sorted(self.grid):
            print(''.join(Tile.SHOW[
                              self.grid[row].get(c, Tile.Empty)
                          ] for c in range(self.min_x, self.max_x + 1)))
        self.grid[0][0] = c

    def fill_with_oxygen(self):
        to_visit = deque()
        to_visit.append((self.oxygen, 0))
        visited = set()
        mt = 0
        while to_visit:
            pos, time = to_visit.popleft()
            mt = max(time, mt)
            visited.add(pos)
            self.grid[pos[1]][pos[0]] = Tile.Oxygen
            for d in 1, 2, 3, 4:
                nx, ny = self.update_pos(*pos, d)
                if self.grid[ny][nx] == Tile.Empty:
                    to_visit.appendleft(((nx, ny), time + 1))
        return mt


class Dec15(Day):
    def __init__(self, filename=None, instructions=None):
        super().__init__(2019, 15, filename=filename, instructions=instructions)
        self.ship = Ship(instructions=self.instructions)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)

    @timer(part=1, title='Minimum # of movement commands needed')
    def part_1(self):
        return len(self.ship.fill_map())

    @timer(part=2, title='Minutes to fill ship with oxygen')
    def part_2(self):
        return self.ship.fill_with_oxygen()


if __name__ == '__main__':
    Dec15().run_day()
