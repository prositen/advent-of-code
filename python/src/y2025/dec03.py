from python.src.common import Day, timer, Timer

class Bank:
    def __init__(self, batteries):
        self.batteries = batteries
        self.max_from_right = []

    def largest_joltage(self):
        max_so_far = 0
        for battery in self.batteries[::-1]:
            max_so_far = max(max_so_far, battery)
            self.max_from_right.append(max_so_far)
        self.max_from_right = self.max_from_right[::-1]

        max_so_far = 0
        for pos, battery in enumerate(self.batteries[:-1]):
            joltage = 10 * battery + self.max_from_right[pos+1]
            max_so_far = max(max_so_far, joltage)

        # print(self.batteries, max_so_far)
        return max_so_far

class Dec03(Day, year=2025, day=3, title='Lobby'):

    @staticmethod
    def parse_instructions(instructions):
        return [
            Bank([int(c) for c in line])
            for line in instructions
        ]

    @timer(part=1)
    def part_1(self):
        return sum(bank.largest_joltage() for bank in self.instructions)

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        Dec03().run_day()
