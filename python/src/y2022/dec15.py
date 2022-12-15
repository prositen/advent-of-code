import re

from python.src.common import Day, timer, Timer, distance


def get_points_on_radius(point, radius):
    x, y = point

    for i in range(1, radius + 1):
        yield x + i, y + radius - i
        yield x + radius - i, -(y + i)
        yield -(x+i), y + radius - i
        yield -(x+i), -(y+radius-i)


def combine_ranges(ranges):
    updated_ranges = list()
    non_matching_ranges = list()
    p_start, p_end = ranges[0]
    for r_start, r_end in ranges[1:]:
        if r_start <= p_end and p_start <= r_end:
            updated_ranges.append((min(r_start, p_start), max(r_end, p_end)))
        else:
            non_matching_ranges.append((r_start, r_end))
    if updated_ranges:
        return combine_ranges(updated_ranges + non_matching_ranges)
    elif non_matching_ranges:
        return [(p_start, p_end)] + combine_ranges(non_matching_ranges)
    else:
        return [(p_start, p_end)]


class SensorMap(object):

    def __init__(self, sensors):
        self.sensors = list()
        self.beacons = set()
        for (my_x, my_y, beacon_x, beacon_y) in sensors:
            dist = distance((my_x, my_y), (beacon_x, beacon_y))
            self.sensors.append(((my_x, my_y), dist))
            self.beacons.add((beacon_x, beacon_y))

    def scan_row(self, row, max_x=None):
        ranges = list()
        for (sx, sy), dist in self.sensors:
            distance_to_row = abs(sy - row)
            if distance_to_row <= dist:
                ranges.append((sx - abs(dist - distance_to_row),
                               sx + abs(dist - distance_to_row) + 1))
        if max_x:
            ranges = [
                (max(0, r[0]), min(r[1], max_x))
                for r in ranges
            ]

        return combine_ranges(sorted(ranges))

    def in_sensor_range(self, point):
        return any(distance(point, sensor) <= dist
                   for (sensor, dist) in self.sensors)

    def find_beacon(self, max_x, max_y):
        for sensor, dist in sorted(self.sensors, key=lambda c: c[1]):
            for (px, py) in get_points_on_radius(sensor, dist + 1):
                if 0 <= px <= max_x and 0 <= py <= max_y:
                    if not self.in_sensor_range((px, py)):
                        return px, py
        return 0, 0

    def find_beacon_2(self, max_x, max_y):
        for s1, d1 in self.sensors:
            for s2, d2 in self.sensors[1:]:
                if any(distance()):
                    pass

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
        ranges = self.sensor_map.scan_row(row=row)
        no_pos = sum(r[1] - r[0] for r in ranges)
        for bx, by in self.sensor_map.beacons:
            if by == row:
                no_pos -= 1
        return no_pos

    @timer(part=2)
    def part_2(self, max_x=4_000_000, max_y=4_000_000):
        x, y = self.sensor_map.find_beacon(max_x=max_x,
                                           max_y=max_y)
        print("should be 12555527364986 for 3138881 3364986")
        return x * 4_000_000 + y
        # for row in range(0, max_y):
        #    ranges = self.sensor_map.scan_row(row=row, max_x=max_x)
        #    if len(ranges) > 1:
        #        return (ranges[1][0]-1)*4000000 + row
        # return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec15().run_day()
