import os

from python.src.y2017.common import DATA_DIR


class FractalArt(object):

    def __init__(self, puzzle_input):
        self.rules = [self.parse_line(line) for line in puzzle_input]
        self.squares = [".#.", "..#", "###"]

    @staticmethod
    def parse_line(line):

        def get_rotations(pattern):
            rv = [[line for line in pattern]]
            for i in range(3):
                pc = rv[i]
                p2 = zip(*pc[::-1])
                rv.append(["".join(line) for line in p2])
            return rv

        def get_flip(pattern):
            return [pattern[y][::-1] for y in range(len(pattern))]

        line = line.strip()
        f, p = line.split(' => ', 2)

        # Precompute all flips and rotations
        f = get_rotations(f.split('/'))
        f2 = []
        for f1 in f:
            f2 += ["/".join(f1), "/".join(get_flip(f1))]
        f2 = [f.split('/') for f in list(set(f2))]

        p = p.split('/')
        return f2, p

    def split(self, size):
        value = []
        for y in range(0, len(self.squares), size):
            row = []
            for x in range(0, len(self.squares), size):
                square = []
                for m in range(size):
                    square.append(self.squares[y + m][x:x + size])
                row.append(square)
            value.append(row)
        return value

    def step(self):
        size = len(self.squares)
        if size % 2 == 0:
            split_size = 2
        else:
            split_size = 3
        s = self.split(split_size)

        output = list()
        for y in s:
            square = list()
            for x in y:
                square.append(self.transform(x))
            output.append(square)
        self.squares = []
        for i, y in enumerate(output):
            self.squares.extend(["" for _ in range(split_size + 1)])
            for j, x in enumerate(y):
                for k, square in enumerate(x):
                    n = i * (split_size + 1) + k
                    self.squares[n] += square

    def transform(self, square):
        for patterns, output in self.rules:
            for p in patterns:
                if p == square:
                    return output
        return square

    def lit_pixels(self):
        return sum(line.count('#') for line in self.squares)


def main():
    with open(os.path.join(DATA_DIR, 'input.21.txt')) as fh:
        puzzle_input = fh.readlines()

    FA = FractalArt(puzzle_input)
    for _ in range(5):
        FA.step()

    print("Part 1:", FA.lit_pixels())

    for _ in range(5, 18):
        FA.step()
    print("Part 2:", FA.lit_pixels())


if __name__ == '__main__':
    main()
