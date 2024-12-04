from collections import defaultdict

from python.src.common import Day, timer, Timer


class WordSearch(object):

    def __init__(self, data):
        self.rows = data

    def count(self):
        word = 'XMAS'

        rows = ','.join(self.rows)
        h_count = (rows.count(word) + rows.count(word[::-1]))

        columns = list(zip(*self.rows))
        columns = ','.join(''.join(chars) for chars in columns)
        v_count = (columns.count(word) + columns.count(word[::-1]))

        diag = defaultdict(list)
        bdiag = defaultdict(list)
        bmin = 1 - len(self.rows)
        for y, line in enumerate(self.rows):
            for x, char in enumerate(line):
                diag[x + y].append(char)
                bdiag[x - y - bmin].append(char)
        d_count = 0
        for line in diag.values():
            line = ''.join(line)
            d_count += line.count(word) + line.count(word[::-1])

        bd_count = 0
        for line in bdiag.values():
            line = ''.join(line)
            bd_count += line.count(word) + line.count(word[::-1])

        return h_count + v_count + d_count + bd_count

    def find_x(self):
        allowed_corners = {  # top left, top right, bottom left, bottom right
            ('S', 'S', 'M', 'M'),
            ('S', 'M', 'S', 'M'),
            ('M', 'M', 'S', 'S'),
            ('M', 'S', 'M', 'S')
        }
        count = 0
        for y, line in enumerate(self.rows[1:-1], start=1):
            for x, char in enumerate(line[1:-1], start=1):
                if char == 'A':
                    tl, tr = self.rows[y - 1][x - 1], self.rows[y - 1][x + 1]
                    bl, br = self.rows[y + 1][x - 1], self.rows[y + 1][x + 1]
                    if (tl, tr, bl, br) in allowed_corners:
                        count += 1
        return count


class Dec04(Day, year=2024, day=4, title='Ceres Search'):

    @timer(part=1)
    def part_1(self):
        ws = WordSearch(self.instructions)
        return ws.count()

    @timer(part=2)
    def part_2(self):
        ws = WordSearch(self.instructions)
        return ws.find_x()


if __name__ == '__main__':
    with Timer('Total'):
        Dec04().run_day()
