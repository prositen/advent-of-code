from python.src.common import Day, timer, Timer


def brute_force(number):
    """
    Kept for posterity, this is how I reasoned out the stack mechanisms.
    """
    inputs = list(map(int, str(number)))
    if 0 in inputs:
        return False
    w = inputs[0]
    z = w + 6

    w = inputs[1]
    z *= 26
    z += w + 7

    w = inputs[2]
    z *= 26
    z += w + 10

    w = inputs[3]
    z *= 26
    z += w + 2

    w = inputs[4]
    z, x = divmod(z, 26)
    x -= 7
    if x != w:
        return False

    w = inputs[5]
    z *= 26
    z += w + 8

    w = inputs[6]
    z *= 26
    z += w + 1

    w = inputs[7]
    z, x = divmod(z, 26)
    x -= 5
    if x != w:
        return False

    w = inputs[8]
    z *= 26
    z += w + 5

    w = inputs[9]
    z, x = divmod(z, 26)
    x -= 3
    if x != w:
        return False

    w = inputs[10]
    z, x = divmod(z, 26)
    if x != w:
        return False

    w = inputs[11]
    z, x = divmod(z, 26)
    x -= 5
    if x != w:
        return False

    w = inputs[12]
    z, x = divmod(z, 26)
    x -= 9
    if x != w:
        return False

    w = inputs[13]
    z, x = divmod(z, 26)
    if x != w:
        return False

    return z == 0


class Dec24(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 24, instructions, filename)
        self.ranges = self.find_ranges()

    def find_ranges(self):
        stack = list()
        ranges = list()
        for i, group in enumerate(self.instructions):
            z_div = int(group[4][2])
            x_add = int(group[5][2])
            y_add = int(group[15][2])
            if z_div == 1:
                stack.append((i, y_add))
            else:
                ranges.append(sorted(((i, x_add), stack.pop())))
        return sorted(ranges)

    @staticmethod
    def parse_instructions(instructions):
        groups = [
            [
                line.split(' ')
                for line in instructions[i * 18:i * 18 + 18]
            ]
            for i in range(14)
        ]
        return groups

    def solve_for_ranges(self, largest):
        n_range = range(9, 0, -1) if largest else range(1, 10)
        output = [0] * 14
        for w0, w1 in self.ranges:
            diff = w0[1] + w1[1]
            for n in n_range:
                if 1 <= n + diff <= 9:
                    output[w0[0]] = n
                    output[w1[0]] = n + diff
                    break
        return int(''.join(str(c) for c in output))

    @timer(part=1)
    def part_1(self):
        n = self.solve_for_ranges(largest=True)
        assert(brute_force(n))
        return n

    @timer(part=2)
    def part_2(self):
        n = self.solve_for_ranges(largest=False)
        assert(brute_force(n))
        return n


if __name__ == '__main__':
    with Timer('Arithmetic Logic Unit'):
        Dec24().run_day()
