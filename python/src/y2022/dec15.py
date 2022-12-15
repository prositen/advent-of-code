import re

from python.src.common import Day, timer, Timer, distance


def get_points_on_radius(point, radius):
    x, y = point
    for i in range(1, radius + 1):
        # BR
        yield x + i, y + radius - i
    for i in range(0, radius):
        # TR
        yield x + i, y - radius + i
    for i in range(0, radius):
        # BL
        yield x - i, y + radius - i
    for i in range(1, radius + 1):
        # TL
        yield x - i, y - radius + i


def line_intersection(line1, line2):
    # Stolen from stack overflow
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return round(x), round(y)


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

    def scan_row(self, row):
        ranges = list()
        for (sx, sy), dist in self.sensors:
            distance_to_row = abs(sy - row)
            if distance_to_row <= dist:
                ranges.append((sx - abs(dist - distance_to_row),
                               sx + abs(dist - distance_to_row) + 1))
        return combine_ranges(sorted(ranges))

    def in_sensor_range(self, point):
        for (sensor, dist) in self.sensors:
            if distance(point, sensor) <= dist:
                return True
        return False

    def find_beacon_1(self, max_x, max_y):
        for sensor, dist in sorted(self.sensors, key=lambda c: c[1]):
            for (px, py) in get_points_on_radius(sensor, dist + 1):
                if 0 <= px <= max_x and 0 <= py <= max_y:
                    if not self.in_sensor_range((px, py)):
                        return px, py
        return 0, 0

    def find_beacon(self):
        candidates = list()
        # If two sensor diamonds are adjacent but not touching, there might be
        # something fishy going on between them. This means their manhattan distance == 2
        # since we're using diagonals.
        for sensor_1 in self.sensors:
            for sensor_2 in self.sensors[1:]:
                s1, d1 = sensor_1
                s2, d2 = sensor_2
                if distance(s1, s2) == d1 + d2 + 2:
                    candidates.append(sorted([sensor_1, sensor_2], key=lambda c: c[0][0]))
        for ((s1, d1), (s2, d2)) in candidates:
            for ((s3, d3), (s4, d4)) in candidates[1:]:
                # Suspicious border between s1 and s2
                line_1 = (
                    (s2[0] - d2 + 1, s2[1]),
                    (s1[0] + d1 - 1, s1[1])
                )
                # Suspicious border between s3 and s4
                line_2 = (
                    (s4[0] - d4 - 1, s4[1]),
                    (s3[0] + d3 + 1, s3[1])
                )
                if x := line_intersection(line_1, line_2):
                    # If all these borders intersect, there are 4 sensors that quite can't
                    # reach this position - that should be our beacon!
                    return x


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
        x, y = self.sensor_map.find_beacon()
        return x * 4_000_000 + y


if __name__ == '__main__':
    with Timer('Total'):
        Dec15().run_day()
