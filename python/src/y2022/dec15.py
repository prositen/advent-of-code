import re

from python.src.common import Day, timer, Timer, distance


class SensorMap(object):

    def __init__(self, sensors):
        self.sensors = list()
        self.beacons = set()
        for (my_x, my_y, beacon_x, beacon_y) in sensors:
            dist = distance((my_x, my_y), (beacon_x, beacon_y))
            self.sensors.append(((my_x, my_y), dist))
            self.beacons.add((beacon_x, beacon_y))

    def scan_row(self, row):
        cells = set()
        ranges = list()
        for (sx, sy), dist in self.sensors:
            distance_to_row = abs(sy - row)
            if distance_to_row <= dist:
                ranges.append(range(sx - abs(dist - distance_to_row),
                                    sx + abs(dist - distance_to_row) + 1))
        for r in ranges:
            for c in r:
                cells.add(c)
        return cells



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
