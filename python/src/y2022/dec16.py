from collections import deque, namedtuple

from python.src.common import Day, timer, Timer

CaveState = namedtuple('CaveState', ['pos', 'open'])
State = namedtuple('State', ['cave', 'time', 'pressure'])


class Cave(object):

    def __init__(self, valves):
        self.tunnels = {valve[0]: (valve[1], valve[2]) for valve in valves}
        self.open_valves = set()
        self.position = 'AA'
        self.pressure = 0
        self.time = 0

    def release_pressure(self, open_valves=None):
        return sum(self.tunnels[v][0] for v in open_valves)

    MOVE = 0
    OPEN = 1

    def run(self, time=30):
        to_visit = deque()
        to_visit.append((State(time=0, pressure=0, cave=CaveState(pos='AA',
                                                                  open=frozenset())),
                         ))
        best = dict()
        max_pressure = 0
        while to_visit:
            state = to_visit.popleft()[0]
            cave: CaveState = state.cave
            pressure = state.pressure + self.release_pressure(cave.open or set())
            if state.time == time:
                continue

            max_pressure = max(max_pressure, pressure)
            if cave in best and best.get(cave) >= pressure:
                continue

            best[cave] = pressure

            if cave.pos not in cave.open and self.tunnels[cave.pos][0]:
                cv = CaveState(pos=cave.pos,
                               open=frozenset(cave.open.union({cave.pos})))
                to_visit.append((State(cave=cv,
                                       time=state.time + 1,
                                       pressure=pressure),
                                 ))
            for tunnel in self.tunnels[cave.pos][1]:
                cv = CaveState(pos=tunnel, open=cave.open)
                to_visit.append((State(cave=cv,
                                       time=state.time + 1,
                                       pressure=pressure),
                                 ))

        return max_pressure


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
        c = Cave(self.instructions)
        return c.run()

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec16().run_day()
