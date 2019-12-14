from collections import Counter, defaultdict

from python.src.common import Day
from python.src.y2019.intcode import IntCode


class Tile(object):
    Empty = 0
    Wall = 1
    Block = 2
    Paddle = 3
    Ball = 4

    SHOW = {
        Empty: ' ',
        Wall: 'X',
        Block: '#',
        Paddle: '-',
        Ball: 'o'
    }


class Game(object):

    def __init__(self, display):
        self.score = 0
        self.ball = None
        self.paddle = None
        self.grid = defaultdict(dict)
        self.parse(display)

    def parse(self, data):

        for i in range(0, len(data), 3):
            x, y, value = data[i:i + 3]
            if x == -1 and y == 0:
                self.score = value
            else:
                if value == Tile.Ball:
                    self.ball = x, y
                elif value == Tile.Paddle:
                    self.paddle = x, y
                self.grid[y][x] = value

    def print(self):
        for row in self.grid.values():
            print(''.join(Tile.SHOW[c] for c in row.values()))
        print("Score:", self.score)

    def move(self):
        if self.ball[0] < self.paddle[0]:
            return -1
        elif self.ball[0] == self.paddle[0]:
            return 0
        else:
            return 1

    def input(self):
        self.print()
        c = input("<(a) (s) (d)>")
        if c == 'a':
            return -1
        elif c == 's':
            return 0
        elif c == 'd':
            return 1

class Dec13(Day):
    def __init__(self, filename=None, instructions=None):
        super().__init__(2019, 13, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)

    def part_1(self):
        ic = IntCode(self.instructions)
        ic.run()
        tiles = Counter()
        for i in range(0, len(ic.output), 3):
            _, _, tile_id = ic.output[i:i + 3]
            tiles[tile_id] += 1
        return tiles[2]

    def part_2(self):
        ic = IntCode(self.instructions)
        ic.data[0] = 2
        game = Game(ic.output)
        while not ic.run_and_wait():
            game.parse(ic.output)
            ic.output = []
            ic.add_input(game.move())
            # ic.add_input(game.input())
        game.parse(ic.output)
        return game.score


if __name__ == '__main__':
    d = Dec13()
    print("Part 1:", d.part_1())
    print("Part 2:", d.part_2())
