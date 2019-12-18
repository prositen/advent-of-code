from collections import deque

from python.src.common import Day


class Dec18(Day):
    def __init__(self, filename=None, instructions=None):
        super().__init__(2019, 18, filename=filename, instructions=instructions)
        start, self.keys, self.grid = self.instructions
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.pos_y, self.pos_x = divmod(start, self.width)

    @staticmethod
    def parse_instructions(instructions):
        _line = ''.join(instructions).strip()
        keys = ''.join(sorted(''.join(c for c in _line if c.islower())))
        return _line.index('@'), keys, [[c for c in row] for row in instructions]

    def can_go(self, pos_y, pos_x, keys):
        if 0 <= pos_y < self.height and 0 <= pos_x < self.width:
            c = self.grid[pos_y][pos_x]
            if c == '.' or c.islower() or c.lower() in keys:
                return True
        return False

    def part_1(self):
        to_visit = deque()
        to_visit.append((self.pos_y, self.pos_x, '', 0))
        best_path = {
            (self.pos_y, self.pos_x, ''): 0
        }
        self.grid[self.pos_y][self.pos_x] = '.'
        best_length = None
        while to_visit:
            y, x, keys, steps = to_visit.popleft()
            c = self.grid[y][x]
            if c.islower():
                keys = ''.join(sorted(set(keys + c)))
            if self.keys == keys:
                if (best_length is None) or (best_length > steps):
                    best_length = steps

            for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
                ny, nx = y + dy, x + dx
                if self.can_go(ny, nx, keys):
                    if best_path.get((ny, nx, keys), steps + 1000) > steps + 1:
                        best_path[(ny, nx, keys)] = steps + 1
                        to_visit.append((ny, nx, keys, steps + 1))
        return best_length

    def part_2(self):
        return 2


if __name__ == '__main__':
    day = Dec18()
    print("Part 1:", day.part_1())
    print("Part 2:", day.part_2())
