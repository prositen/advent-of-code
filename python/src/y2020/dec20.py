import math
from collections import deque

from python.src.common import Day, timer, Timer


class Image(object):
    def __init__(self, data):
        self.image = data
        self.height = len(self.image)
        self.width = len(self.image[0])

    def flip_x(self):
        self.image = [
            row[::-1]
            for row in self.image
        ]

    def flip_y(self):
        self.image = self.image[::-1]

    def rotate_right(self):
        new_image = list()
        for col in range(self.width):
            line = list()
            for row in range(self.height):
                line.append(self.image[-row - 1][col])
            new_image.append(''.join(line))
        self.image = new_image
        self.width, self.height = self.height, self.width

    TR = str.maketrans(' .#', '001')

    def int_list(self):
        return [
            int(row.translate(self.TR), 2)
            for row in self.image
        ]


class Tile(object):
    def __init__(self, data):
        number = data[0].split(' ')[1][:-1]
        self.number = int(number, 10)

        data = data[1:]
        self.borders = [data[0],
                        ''.join(d[-1] for d in data),
                        data[-1],
                        ''.join(d[0] for d in data)]
        self._image = Image([row[1:-1] for row in data[1:-1]])
        self.edges = [0, 0, 0, 0]

    def image(self):
        return self._image.image

    def height(self):
        return self._image.height

    def count(self):
        return len([c for c in self.edges if c])

    def flip_x(self):
        self._image.flip_x()
        self.borders = [self.borders[0][::-1],
                        self.borders[3],
                        self.borders[2][::-1],
                        self.borders[1]]
        self.edges[1], self.edges[3] = self.edges[3], self.edges[1]

    def flip_y(self):
        self._image.flip_y()
        self.borders = [self.borders[2],
                        self.borders[1][::-1],
                        self.borders[0],
                        self.borders[3][::-1]]
        self.edges[0], self.edges[2] = self.edges[2], self.edges[0]

    def rotate_right(self):
        self._image.rotate_right()
        self.borders = [
            self.borders[3][::-1],
            self.borders[0],
            self.borders[1][::-1],
            self.borders[2]
        ]
        self.edges = [self.edges[3]] + self.edges[:3]

    def fit(self, other, their_dir):
        """ Does this tile fit to the 'direction' of 'other'? """
        my_dir = (their_dir + 2) % 4
        for _ in range(4):
            if self.borders[my_dir] == other.borders[their_dir]:
                return True
            self.rotate_right()
        self.flip_x()
        for _ in range(4):
            if self.borders[my_dir] == other.borders[their_dir]:
                return True
            self.rotate_right()
        return False


class Grid(object):
    def __init__(self, tiles):
        self.tiles = {t.number: t for t in tiles}
        self.find_matches()

    DIRS = {
        0: (-1, 0),
        1: (0, 1),
        2: (1, 0),
        3: (0, -1)
    }

    SEA_MONSTER = Image(data=[
        "                  # ",
        "#    ##    ##    ###",
        "#  #  #  #  #  #    "
    ])

    def find_matches(self):
        for en1, n1 in enumerate(self.tiles):
            for n2 in list(self.tiles)[en1 + 1:]:
                t1 = self.tiles[n1]
                t2 = self.tiles[n2]
                for i1, e1 in enumerate(t1.borders):
                    for i2, e2 in enumerate(t2.borders):
                        if e1 == e2 or e1 == e2[::-1]:
                            t1.edges[i1] = n2
                            t2.edges[i2] = n1

    def find_corners(self):
        return [n for n, t in self.tiles.items() if t.count() == 2]

    def form_image(self):
        corners = self.find_corners()
        # Decide on a corner and rotate it to be in the nw
        nw = self.tiles[corners[0]]
        while not nw.edges[1] or not nw.edges[1]:
            nw.rotate_right()

        grid = dict()
        to_visit = deque()
        to_visit.append((nw, 0, 0))
        while to_visit:
            tile, y, x = to_visit.pop()
            if (y, x) in grid:
                continue
            grid[(y, x)] = tile
            for d, edge in enumerate(tile.edges):
                dy, dx = self.DIRS[d]
                tile_no = edge
                if tile_no:
                    next_tile = self.tiles[tile_no]
                    next_tile.fit(tile, d)
                    to_visit.append((next_tile, y + dy, x + dx))

        image = dict()
        h = nw.height()
        for (y, x), tile in sorted(grid.items(), key=lambda x: x[0]):
            for i, row in enumerate(tile.image()):
                row_no = (y * h) + i
                image[row_no] = image.get(row_no, '') + row
        return Image(list(image.values()))


class Dec20(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 20, instructions, filename)
        self.grid = Grid(self.instructions)

    @staticmethod
    def parse_instructions(instructions):
        return [Tile(g) for g in Day.parse_groups(instructions)]

    @timer(part=1)
    def part_1(self):
        return math.prod(self.grid.find_corners())

    @timer(part=2)
    def part_2(self):
        print(self.grid.SEA_MONSTER.int_list())
        self.grid.form_image()
        return 273


if __name__ == '__main__':
    with Timer():
        Dec20().run_day()
