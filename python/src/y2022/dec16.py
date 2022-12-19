import itertools
from collections import deque
from heapq import heappop, heappush

from python.src.common import Day, timer, Timer


class Cave(object):

    def __init__(self, valves):
        self.tunnels = {valve[0]: {v: 1 for v in valve[2]} for valve in valves}
        self.flow = {valve[0]: valve[1] for valve in valves}

    def run(self, max_time=30):
        to_visit = deque()
        to_visit.append((1, 0, 0, 'AA', 0))

        best = dict()
        final_paths = set()
        valves = {v: 1 << i for i, v in enumerate(vv for vv, flow in self.flow.items()
                                                  if flow)}

        while to_visit:
            (time, pressure, open_valves, pos, increase) = to_visit.popleft()
            state = (open_valves, pos)
            pressure += increase
            if time == max_time:
                final_paths.add((open_valves, pressure))
                continue
            elif best.get(state, -1) >= pressure:
                continue

            best[state] = pressure
            if (i := self.flow[pos]) and not open_valves & valves[pos]:
                new_open = open_valves | valves[pos]
                to_visit.append(
                    (time + 1, pressure, new_open, pos, increase + i))

            for tunnel, cost in self.tunnels[pos].items():
                to_visit.append(
                    (time + cost, pressure, open_valves, tunnel, increase))

        return final_paths


class Dec16(Day, year=2022, day=16):

    @staticmethod
    def parse_instructions(instructions):
        valves = list()
        for line in instructions:
            valve_data, tunnels = line.split(';')
            valve_name = valve_data[6:8]
            flow_rate = int(valve_data[23:])
            tunnels = [t.strip() for t in tunnels[23:].split(', ')]
            valves.append((valve_name, flow_rate, tunnels))
        return valves

    @timer(part=1)
    def part_1(self):
        paths = Cave(self.instructions).run()
        return max(v for (_, v) in paths)

    @timer(part=2)
    def part_2(self):
        # 2675
        paths = list(Cave(self.instructions).run(max_time=26))
        max_pressure = max(
            p1 + p2
            for v1, p1 in paths
            for v2, p2 in paths
            if not v1 & v2
        )
        return max_pressure


if __name__ == '__main__':
    with Timer('Total'):
        Dec16().run_day()
