from collections import deque

from python.src.common import Day, timer, Timer


class Cave(object):

    def __init__(self, valves):
        self.tunnels = {valve[0]: {v for v in valve[2]} for valve in valves}
        self.flow = {valve[0]: valve[1] for valve in valves if valve[1]}
        self.valves = {v: 1 << i for i, v in enumerate(vv for vv, flow in self.flow.items())}

    def run(self, max_time=30):
        to_visit = deque([(1, 0, 0, 'AA')])

        running_best = dict()
        best = dict()

        while to_visit:
            (time, pressure, open_valves, pos) = to_visit.popleft()
            state = (open_valves, pos)
            if time == max_time:
                best[open_valves] = max(best.get(open_valves, 0), pressure)
                continue
            elif running_best.get(state, -1) >= pressure:
                continue

            running_best[state] = pressure
            if (i := self.flow.get(pos, 0)) and not open_valves & self.valves[pos]:
                new_open = open_valves | self.valves[pos]
                to_visit.append(
                    (time + 1, pressure + (max_time-time)*i, new_open, pos))

            for tunnel in self.tunnels[pos]:
                to_visit.append(
                    (time + 1, pressure, open_valves, tunnel))

        return best


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
        pressure = Cave(self.instructions).run().values()
        return max(pressure)

    @timer(part=2)
    def part_2(self):
        pressure = Cave(self.instructions).run(max_time=26)
        return max(
            p1 + p2
            for v1, p1 in pressure.items()
            for v2, p2 in pressure.items()
            if not v1 & v2
        )


if __name__ == '__main__':
    with Timer('Total'):
        Dec16().run_day()
