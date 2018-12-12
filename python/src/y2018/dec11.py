from python.src.common import Day


class Dec11(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 11, instructions, filename)
        self.serial = self.instructions
        self.grid = self.base_grid()

    @staticmethod
    def parse_instructions(instructions):
        return int(instructions[0])

    def power_level(self, x, y):
        rack_id = x + 10
        pl = (rack_id * y + self.serial) * rack_id
        pl = (pl % 1000) // 100
        return pl - 5

    def base_grid(self):
        return [
            [self.power_level(x, y) for x in range(1, 301)]
            for y in range(1, 301)
        ]

    def calc_grid(self, square_size=3):
        row_sums = [
            [sum(self.grid[y][:square_size])] + [0 for _ in range(square_size, 300)] for y in range(300)
        ]
        for y in range(300):
            for x in range(1, 300 - square_size):
                row_sums[y][x] = row_sums[y][x - 1] + self.grid[y][x + square_size - 1] - self.grid[y][x - 1]

        max_sum = (0, 1, 1)

        for x in range(square_size, 300 - square_size):
            block_sum = sum(row_sums[y][x] for y in range(square_size))
            max_sum = max((block_sum, x + 1, 1), max_sum)

            for y in range(square_size, 300):
                to_add = row_sums[y][x]
                to_remove = row_sums[y - square_size][x]
                block_sum = block_sum + to_add - to_remove
                max_sum = max((block_sum, x + 1, y + 2 - square_size), max_sum)
        return max_sum

    def part_1(self):
        m = self.calc_grid()
        return m[1], m[2]

    @property
    def part_2(self):
        max_val = (0, 0, 0), 0
        for s in range(1, 301):
            r = self.calc_grid(square_size=s)
            if r[0] == 0:
                break
            max_val = max((r, s), max_val)

        return max_val[0][1], max_val[0][2], max_val[1]


if __name__ == '__main__':
    d = Dec11(instructions=["5153"])
    print("Part 1:", d.part_1())
    print("Part 2:", d.part_2)
