from collections import deque
from heapq import heappush, heappop

from python.src.common import Day, timer, Timer


class ServerRack:
    def __init__(self, devices):
        self.devices = devices

    def find_paths_from_you_to_out(self):

        visited = dict()
        def traverse(node):
            if node == 'out':
                return 1
            if node not in visited:
                visited[node] = sum(traverse(next_node)
                                    for next_node in self.devices[node])
            return visited[node]
        return traverse('you')


    def find_all_paths_with_dac_and_fft(self):

        visited = dict()

        def traverse(node):
            (name, dac, fft) = node
            if name == 'out':
                return dac and fft
            if node not in visited:
                visited[node] = sum(traverse((next_device,
                                              dac or name == 'dac',
                                              fft or name == 'fft'))
                                    for next_device in self.devices[name])

            return visited[node]

        return traverse(('svr', False, False))


class Dec11(Day, year=2025, day=11, title='Reactor'):

    @staticmethod
    def parse_instructions(instructions):
        result = dict()
        for line in instructions:
            k, v = line.split(':', 1)
            outputs = [vv.strip() for vv in v.split()]
            result[k] = outputs

        return result

    @timer(part=1)
    def part_1(self):
        return ServerRack(self.instructions).find_paths_from_you_to_out()

    @timer(part=2)
    def part_2(self):
        return ServerRack(self.instructions).find_all_paths_with_dac_and_fft()


if __name__ == '__main__':
    with Timer('Total'):
        Dec11().run_day()
