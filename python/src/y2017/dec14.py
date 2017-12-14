from python.src.y2017.dec10 import KnotHash


class Defragger(object):

    @staticmethod
    def hash_to_bits(knot_hash):
        rv = []
        for x in knot_hash:
            xx = int(x, 16)
            rv.append("{:0>4}".format(bin(xx)[2:]))
        return "".join(rv)

    def __init__(self, puzzle_input, max_length=128):
        self.puzzle_input = puzzle_input
        self.squares = None
        self.regions = dict()
        self.max_length = 128

    def get_squares(self):
        if self.squares is None:
            self.squares = list()
            for x in range(128):
                line = "{}-{}".format(self.puzzle_input, x)
                kh = KnotHash.from_bytes_input(line)
                kh.run()
                self.squares.append(self.hash_to_bits(kh.checksum()))
        return self.squares

    def find_squares_used(self):
        return sum(s.count('1') for s in self.get_squares())

    def get_state(self):
        return "\n".join(["".join(str(x) for x in self.regions[line]) for line in range(self.max_length)])

    def find_regions(self):
        self.get_squares()
        max_group = 1
        for ri, row in enumerate(self.squares[:self.max_length]):
            self.regions[ri] = list()
            for ci, col in enumerate(row[:self.max_length]):
                val = 0
                if col == '1':
                    val = max_group
                    max_group += 1
                self.regions[ri].append(val)

        state = self.get_state()
        prev_state = ""

        # merge regions
        prev_row = None
        while state != prev_state:
            for row in range(self.max_length):
                for col in range(self.max_length):
                    me = self.regions[row][col]
                    if me > 0:
                        fill_region = me
                        if row > 0:
                            prev_region = prev_row[col]
                            if prev_region > 0:
                                fill_region = prev_region
                        self.fill(row, col, fill_region)
                prev_row = self.regions[row]

            prev_state = state
            state = self.get_state()

        m = set()
        for line in self.regions.values():
            m = m.union(line)

        return len(m)-1   # Remove the 0

    def fill(self, row, col, fill_region):
        self.regions[row][col] = fill_region
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            r2 = row + dx
            c2 = col + dy
            if 0 <= r2 < self.max_length and 0 <= c2 < self.max_length:
                if self.regions[r2][c2] > 0 and self.regions[r2][c2] != fill_region:
                    self.fill(r2, c2, fill_region)


def main():
    puzzle_input = "jzgqcdpd"
    d = Defragger(puzzle_input)
    print("Part 1:", d.find_squares_used())
    print("Part 2:", d.find_regions())


if __name__ == '__main__':
    main()
