from functools import cache

from python.src.common import Day, timer, Timer


class Dec11(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 11, instructions, filename)
        self.grid, self.rows, self.cols = self.instructions

    @staticmethod
    def parse_instructions(instructions):
        return instructions, len(instructions), len(instructions[0])

    @cache
    def seat(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col]
        return ''

    def count_neighbours(self, r, c):
        return [self.seat(r - 1, c - 1), self.seat(r - 1, c), self.seat(r - 1, c + 1),
                self.seat(r, c - 1), self.seat(r, c + 1),
                self.seat(r + 1, c - 1), self.seat(r + 1, c), self.seat(r + 1, c + 1)].count('#')

    def count_visible_seats(self, r, c):
        def nearest_seat(dy, dx):
            for i in range(1, length):
                v = self.seat(r + dy * i, c + dx * i)
                if v in ('#', 'L', ''):
                    return v

        length = max(self.rows, self.cols)
        seats = [nearest_seat(-1, -1), nearest_seat(-1, 0), nearest_seat(-1, 1),
                 nearest_seat(0, -1), nearest_seat(0, 1),
                 nearest_seat(1, -1), nearest_seat(1, 0), nearest_seat(1, 1)]
        return seats.count('#')

    def run(self, look=None, clear=4):
        if not look:
            look = self.count_neighbours
        while True:
            next_grid = list()
            self.seat.cache_clear()
            for r in range(self.rows):
                row = list()
                for c in range(self.cols):
                    seat = self.seat(r, c)
                    nb = look(r, c)
                    if nb == 0 and seat == 'L':
                        row.append('#')
                    elif nb >= clear and seat == '#':
                        row.append('L')
                    else:
                        row.append(seat)
                next_grid.append(''.join(row))
            if self.grid == next_grid:
                return
            self.grid = next_grid

    @timer(part=1)
    def part_1(self):
        self.run(look=self.count_neighbours,
                 clear=4)
        return ''.join(self.grid).count('#')

    def print(self):
        print('\n'.join(row for row in self.grid))
        print('\n')

    @timer(part=2)
    def part_2(self):
        self.grid, _, _ = self.instructions
        self.run(look=self.count_visible_seats,
                 clear=5)
        return ''.join(self.grid).count('#')


if __name__ == '__main__':
    with Timer('Total'):
        d = Dec11()
        d.part_1()
        d.part_2()
