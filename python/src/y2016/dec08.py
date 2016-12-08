import re


class Screen(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.rows = [['.'] * self.width for _ in range(self.height)]

    def rect(self, x, y):
        for _y in range(y):
            self.rows[_y][:x] = ['#'] * x

    def rotate_column(self, x, pixels):
        cols = [list(x) for x in zip(*self.rows)]
        cols[x] = cols[x][-pixels:] + cols[x][:-pixels]
        self.rows = [list(x) for x in zip(*cols)]

    def rotate_row(self, y, pixels):
        self.rows[y] = self.rows[y][-pixels:] + self.rows[y][:-pixels]

    def get_rows(self):
        return [''.join(row) for row in self.rows]

    def count_lit(self):
        return ''.join(''.join(row) for row in self.rows).count('#')


re_RECT = re.compile(r"rect (\d+)x(\d+)")
re_ROTATE_ROW = re.compile(r"rotate row y=(\d+) by (\d+)")
re_ROTATE_COLUMN = re.compile(r"rotate column x=(\d+) by (\d+)")


def parse(instruction_list):
    screen = Screen(50, 6)
    for instruction in instruction_list:
        result = re_RECT.match(instruction)
        if result:
            screen.rect(int(result.group(1)), int(result.group(2)))
            continue
        result = re_ROTATE_ROW.match(instruction)
        if result:
            screen.rotate_row(int(result.group(1)), int(result.group(2)))
            continue
        result = re_ROTATE_COLUMN.match(instruction)
        if result:
            screen.rotate_column(int(result.group(1)), int(result.group(2)))
            continue
    return screen


if __name__ == '__main__':
    with open('../../../data/2016/input.8.txt', 'r') as fh:
        instructions = fh.readlines()
        screen = parse(instructions)
        print("Lit pixels", screen.count_lit())
        print('\n'.join(screen.get_rows()).replace('.', ' '))
