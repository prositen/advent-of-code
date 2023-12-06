import math

from python.src.common import Day, timer, Timer


class Dec06(Day, year=2023, day=6):

    @staticmethod
    def parse_instructions(instructions):
        space_separated_times = [int(c) for c in (instructions[0][5:].split())]
        space_separated_distances = [int(c) for c in (instructions[1][9:].split())]
        one_time = ''.join(c for c in instructions[0] if '0' <= c <= '9')
        one_distance = ''.join(c for c in instructions[1] if '0' <= c <= '9')
        return {
            1: list(zip(space_separated_times, space_separated_distances)),
            2: (int(one_time), int(one_distance))
        }

    @staticmethod
    def brute_wins(time, distance):
        distances = [x * (time - x) for x in range(time)]
        return sum([c > distance for c in distances])

    @staticmethod
    def square_root_wins(time, distance):
        """
        x(time -x) - distance = 0
        x^2 - time*x + distance = 0

        x = (time/2) +- sqrt((time/2)^2 - distance)
        """
        sq = math.sqrt((time / 2) ** 2 - distance)
        root_1 = (time / 2) + sq
        root_2 = (time / 2) - sq
        return math.floor(root_1) - math.ceil(root_2) + 1

    @timer(part=1)
    def part_1(self):
        ways = 1
        for (time, record) in self.instructions[1]:
            ways *= self.brute_wins(time=time, distance=record)
        return ways

    @timer(part=2)
    def part_2(self):
        time, record = self.instructions[2]
        return self.square_root_wins(time=time, distance=record)


if __name__ == '__main__':
    with Timer('Total'):
        Dec06().run_day()
