import re
from collections import deque

from python.src.common import Day, timer, Timer, distance


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
        no_pos = sum(r[1]-r[0] for r in ranges)
        for bx, by in self.sensor_map.beacons:
            if by == row:
                no_pos -= 1
        return no_pos

    @timer(part=2)
    def part_2(self, max_x=4_000_000, max_y=4_000_000):
        for row in range(0, max_y):
            ranges = self.sensor_map.scan_row(row=row, max_x=max_x)
            if len(ranges) > 1:
                return (ranges[1][0]-1)*4000000 + row
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec15().run_day()
