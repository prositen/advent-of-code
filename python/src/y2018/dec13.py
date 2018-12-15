import copy
import re

from python.src.common import Day


class Cart(object):
    DIRECTIONS = {
        '<': (-1, 0),
        'v': (0, 1),
        '>': (1, 0),
        '^': (0, -1),
    }

    next_id = 1

    def turn_left(self):
        # print(self.id, "turn left")
        return self.dy, -self.dx

    def turn_right(self):
        # print(self.id, "turn right")
        return -self.dy, self.dx

    def turn_backslash(self):
        # print(self.id, "backslash")
        return self.dy, self.dx

    def turn_slash(self):
        # print(self.id, "slash")
        return -self.dy, -self.dx

    def intersection(self):
        # print(self.id, "intersection")
        self.next_intersection = (self.next_intersection + 1) % 3
        if self.next_intersection == 1:
            return self.turn_left()
        elif self.next_intersection == 2:
            # print(self.id, "straight ahead")
            return self.dx, self.dy
        else:
            return self.turn_right()

    def __init__(self, pos, direction):
        self.x, self.y = pos
        self.dx, self.dy = direction
        self.id = Cart.next_id
        Cart.next_id += 1
        self.next_intersection = 0

    def step(self, grid):
        self.x += self.dx
        self.y += self.dy
        # print(self.id, self.x, self.y)
        current_pos = grid[self.y][self.x]
        if current_pos == '+':
            self.dx, self.dy = self.intersection()
        elif current_pos == '\\':
            self.dx, self.dy = self.turn_backslash()
        elif current_pos == '/':
            self.dx, self.dy = self.turn_slash()

    def __str__(self):
        for k, v in self.DIRECTIONS.items():
            if (self.dx, self.dy) == v:
                return k
        return '$'

    def __repr__(self):
        return '<Cart {} {} {}>'.format(self.id, (self.x, self.y), str(self))


class Dec13(Day):
    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 13, instructions, filename)
        self.carts, self.grid = self.instructions

    @classmethod
    def parse_instructions(cls, instructions):
        re_cart = re.compile(r'([<^>v])')
        grid = list()
        carts = list()
        for ri, row in enumerate(instructions):
            row = row.rstrip()
            for m in re_cart.finditer(row):
                carts.append(Cart((m.start(), ri), Cart.DIRECTIONS.get(m.group(0))))
            row = row.replace('^', '|').replace('v', '|').replace('>', '-').replace('<', '-')
            grid.append(row)
        return carts, grid

    def part_1(self):
        return self.run(break_at_crash=True)

    def run(self, break_at_crash):
        carts = [copy.deepcopy(cart) for cart in self.carts]
        i = 0
        while True:
            if len(carts) == 1:
                return carts[0].x, carts[0].y
            i += 1
            carts.sort(key=lambda c: (c.y, c.x))
            for c in list(carts):
                if c not in carts:
                    continue
                c.step(self.grid)

                for cr in list(carts):
                    if c.id != cr.id and (c.x, c.y) == (cr.x, cr.y):
                        if break_at_crash:
                            return c.x, c.y
                        else:
                            carts.remove(c)
                            carts.remove(cr)
                            break

                # self.print(carts)

    def print(self, carts):
        c = [
            [ch for ch in y] for y in self.grid
        ]

        for cart in carts:
            if c[cart.y][cart.x] in ('^', 'v', '<', '>'):
                c[cart.y][cart.x] = 'X'
            else:
                c[cart.y][cart.x] = str(cart)

        width = max(len(r) for r in c)
        print('     ' + ''.join(str((i // 100)) if i > 100 else ' ' for i in range(width)))
        print('     ' + ''.join(str((i // 10) % 10) if i > 10 else ' ' for i in range(width)))
        print('     ' + ''.join(str(i % 10) for i in range(width)))
        for i, y in enumerate(c):
            print('{:>3}: {}'.format(i, ''.join(y)))
        print('\n')

    def part_2(self):
        return self.run(break_at_crash=False)


if __name__ == '__main__':
    d = Dec13()
    print("Location of first crash:", d.part_1())
    print("Location of final cart:", d.part_2())
