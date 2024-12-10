from python.src.common import Day, timer, Timer


class Dec10(Day, year=2024, day=10):

    @timer(part=1)
    def part_1(self):
        return 0

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec10().run_day()
