from heapq import heappush, heappop
from python.src.common import Day


class Dec22(Day):
    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 22, instructions, filename)
        self.depth, self.ty, self.tx = self.instructions
        self.geos = self.geo_type()

    @staticmethod
    def parse_instructions(instructions):
        depth = int(instructions[0].split()[1])
        x, y = map(int, instructions[1].split()[1].split(','))
        return depth, y, x

    def part_1(self):
        return sum(self.geos[y][x] for x in range(0, self.tx + 1)
                   for y in range(0, self.ty + 1))

    ROCKY, WET, NARROW = 0, 1, 2
    NONE, TORCH, CLIMBING_GEAR = 0, 1, 2

    TYPE = {
        ROCKY: '.',
        WET: '=',
        NARROW: '|'
    }

    def show_map(self):
        for y in range(0, self.ty + 1):
            print(''.join(self.TYPE[self.geos[y][x]] for x in range(0, self.tx + 1)))

    def geo_type(self):
        maxy = self.ty + 300
        maxx = self.tx + 300
        geo = [[0 for _ in range(maxx + 1)] for _ in range(maxy + 1)]
        geo[0] = [((x * 16807) + self.depth) % 20183 for x in range(maxx + 1)]

        for y in range(1, maxy):
            for x in range(maxx):
                if x == 0:
                    geo[y][x] = ((y * 48271) + self.depth) % 20183
                else:
                    geo[y][x] = ((geo[y - 1][x] * geo[y][x - 1]) + self.depth) % 20183

        geo[0][0] = 0
        geo[self.ty][self.tx] = 0

        return [[v % 3 for v in y] for y in geo]

    def part_2(self):

        # time estimate, time spent, y, x, equipment
        to_visit = [(self.ty+self.tx, 0, 0, 0, self.TORCH)]
        time_to_region = {
            (0,0,1): 0
        }
        while to_visit:
            _, time, y, x, eq = heappop(to_visit)
            if y == self.ty and x == self.tx and eq == self.TORCH:
                return time

            # Move to neighbour with existing equipment
            for yy, xx in (y, x + 1), (y + 1, x), (y, x - 1), (y - 1, x):
                if 0 <= yy and 0 <= xx and eq != self.geos[yy][xx]:
                    if time_to_region.get((yy, xx, eq), time + 10000) > time + 1:
                        estimate = (abs(self.ty - yy) + abs(self.tx - xx))
                        if eq != self.TORCH:
                            estimate += 7
                        heappush(to_visit, (estimate + time + 1,
                                            time + 1,
                                            yy, xx, eq))
                        time_to_region[(yy, xx, eq)] = time + 1
            # Or change equipment

            other_eq = 3 - (eq + self.geos[y][x])
            if time_to_region.get((y, x, other_eq), time + 999) > time + 7:
                estimate = abs(self.ty - y) + abs(self.tx - x)
                if other_eq != self.TORCH:
                    estimate += 7
                heappush(to_visit, (estimate + time + 7, time + 7, y, x, other_eq))
                time_to_region[(y, x, other_eq)] = time + 7


if __name__ == '__main__':
    d = Dec22()
    print('Risk level: ', d.part_1())
    print('Time to rescue:', d.part_2())
