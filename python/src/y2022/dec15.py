import re

from python.src.common import Day, timer, Timer, distance


class SensorMap(object):
    SENSOR = 1
    BEACON = 2

    def __init__(self, sensors):
        self.sensors = dict()
        self.beacons = set()
        self.min_x = sensors[0][0]
        self.max_x = sensors[0][0]
        for (my_x, my_y, beacon_x, beacon_y) in sensors:
            dist = distance((my_x, my_y), (beacon_x, beacon_y))
            self.sensors[(my_x, my_y)] = dist
            self.beacons.add((beacon_x, beacon_y))
            self.min_x = min(self.min_x, my_x - dist)
            self.max_x = max(self.max_x, my_x + dist)

    def scan_row(self, row):
        cells = set()
        for (sx, sy), dist in self.sensors.items():
            distance_to_row = abs(sy - row)
            if distance_to_row <= dist:
                for dx in range(abs(dist - distance_to_row) + 1):
                    cells.add(sx + dx)
                    cells.add(sx - dx)
        return cells

    def find_beacon(self, max_x, max_y):
        cells = set()
        for row in range(max_x + 1):
            for (sx, sy), dist in self.sensors.items():
                distance_to_row = abs(sy - row)
                if distance_to_row <= dist:
                    for dx in range(abs(dist - distance_to_row) + 1):
                        cells.add((sx + dx, y))
                        cells.add((sx - dx, y))


class Dec15(Day, year=2022, day=15):

    def __init__(self, instructions=None, filename=None):
        super().__init__(instructions=instructions, filename=filename)
        self.sensor_map = SensorMap(self.instructions)

    @staticmethod
    def parse_instructions(instructions):
        exp = re.compile(r'-?\d+')
        return [
            tuple(map(int, exp.findall(line)))
            for line in instructions
        ]

    @timer(part=1)
    def part_1(self, row=2_000_000):
        row = self.sensor_map.scan_row(row=row)
        for bx, by in self.sensor_map.beacons:
            if by == row:
                row.remove(bx)
        return len(row)

    @timer(part=2)
    def part_2(self, max_x=4_000_000, max_y=4_000_000):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec15().run_day()
