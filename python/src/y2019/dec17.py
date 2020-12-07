from python.src.common import Day, timer
from python.src.y2019.intcode import IntCode


class Dec17(Day):
    deltas = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]

    def __init__(self, filename=None, instructions=None):
        super().__init__(2019, 17, filename=filename, instructions=instructions)
        self.width, self.height = 0, 0
        self.bot_x, self.bot_y = 0, 0
        self.grid = list()

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)

    @timer(part=1, title='Sum of alignment parameters')
    def part_1(self):
        ic = IntCode(self.instructions)
        ic.run()
        view = ''.join(chr(c) for c in ic.output).strip().split('\n')
        # print(view)
        self.width = len(view[0])
        self.height = len(view)

        self.grid = [
            [c for c in line.strip()]
            for line in view
        ]

        bot_pos = ''.join(view).index('^')
        self.bot_y, self.bot_x = divmod(bot_pos, self.width)

        return self.alignment_parameters(view)

    @timer(part=2, title='Amount of dust collected')
    def part_2(self):
        path = self.find_path()
        main, a, b, c = self.compress_path(path)
        ic = IntCode(instructions=self.instructions)
        ic.data[0] = 2
        for prog in (main, a, b, c):
            for i in prog:
                ic.add_input(ord(i))
            ic.add_input(10)
        ic.add_input(ord('n'))
        ic.add_input(10)
        ic.run()
        return ic.output[-1]

    def move(self, pos_y, pos_x, direction):
        return pos_y + self.deltas[direction][0], pos_x + self.deltas[direction][1]

    def can_go(self, pos_y, pos_x, direction):
        y, x = self.move(pos_y, pos_x, direction)
        return 0 <= y < self.height and 0 <= x < self.width and self.grid[y][x] == '#'

    def turn(self, direction, turn):
        if turn == 'F':
            return direction
        elif turn == 'L':
            return (direction - 1) % 4
        else:
            return (direction + 1) % 4

    def find_path(self):
        pos_y, pos_x = self.bot_y, self.bot_x
        direction = 0
        path = list()
        steps = 0
        while True:
            for turn in ('F', 'L', 'R'):
                if self.can_go(pos_y, pos_x, self.turn(direction, turn)):
                    direction = self.turn(direction, turn)
                    pos_y, pos_x = self.move(pos_y, pos_x, direction)
                    if turn == 'F':
                        steps += 1
                    else:
                        if steps > 0:
                            path.append(str(steps))
                        path.append(turn)
                        steps = 1
                    break
            else:
                return path + [str(steps)]

    def compress_path(self, path):
        compressed = ','.join(path)
        for a in range(10, 0, -1):
            a_try = ','.join(path[0:a])
            if len(a_try) > 20:
                continue
            a_compressed = compressed.replace(a_try, 'A').split(',')
            start = 0
            for start, x in enumerate(a_compressed):
                if x != 'A':
                    break
            for b in range(10, 0, -1):
                b_try = ','.join(a_compressed[start:start + b])
                if len(b_try) > 20 or 'A' in b_try:
                    continue
                b_compressed = ','.join(a_compressed).replace(b_try, 'B').split(',')
                for start, x in enumerate(b_compressed):
                    if x not in ('A', 'B'):
                        break
                for c in range(10, 0, -1):
                    c_try = ','.join(b_compressed[start:start + c])
                    if len(c_try) > 20 or 'A' in c_try or 'B' in c_try:
                        continue
                    c_compressed = ','.join(b_compressed).replace(c_try, 'C')
                    if not all([c in ',ABC' for c in c_compressed]):
                        continue

                    return c_compressed, a_try, b_try, c_try

    def alignment_parameters(self, view):
        alignment = 0
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                if view[y][x] == '#' and (
                        view[y - 1][x] == '#' and
                        view[y + 1][x] == '#' and
                        view[y][x - 1] == '#' and
                        view[y][x + 1] == '#'
                ):
                    alignment += y * x
        return alignment


if __name__ == '__main__':
    Dec17().run_day()
