import itertools

from python.src.common import Day, timer, Timer


class StarMap(object):

    def __init__(self, image, expansion):
        self.galaxies = set()

        max_y = len(image)
        max_x = len(image[0])
        columns = [
            ''.join(image[y][x] for y in range(max_y))
            for x in range(max_x)
        ]
        empty_columns = [n for n, row in enumerate(columns) if '#' not in row]


        y = 0
        for row in image:
            x = 0
            if '#' not in row:
                y += (expansion-1)
            else:
                for x_index, ch in enumerate(row):
                    if ch == '#':
                        self.galaxies.add((y, x))
                    elif x_index in empty_columns:
                        x += (expansion-1)
                    x += 1
            y += 1

    def sum_shortest_pairs(self):
        path_sum = 0
        for g1, g2 in itertools.combinations(self.galaxies, 2):
            path_sum += abs(g1[0]-g2[0]) + abs(g1[1]-g2[1])
        return path_sum

class Dec11(Day, year=2023, day=11):

    @timer(part=1)
    def part_1(self):
        g = StarMap(self.instructions, expansion=2)
        return g.sum_shortest_pairs()

    @timer(part=2)
    def part_2(self):
        g = StarMap(self.instructions, expansion=1000000)
        return g.sum_shortest_pairs()


if __name__ == '__main__':
    with Timer('Total'):
        Dec11().run_day()
