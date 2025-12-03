from python.src.common import Day, timer, Timer


class Bank:
    def __init__(self, batteries):
        self.batteries = batteries
        self.max_from_right = []

    def brute_joltage(self):
        max_so_far = 0
        for battery in self.batteries[::-1]:
            max_so_far = max(max_so_far, battery)
            self.max_from_right.append(max_so_far)
        self.max_from_right = self.max_from_right[::-1]

        max_so_far = 0
        for pos, battery in enumerate(self.batteries[:-1]):
            joltage = 10 * battery + self.max_from_right[pos + 1]
            max_so_far = max(max_so_far, joltage)

        return max_so_far

    def smart_joltage(self, batteries: int, joltage_so_far: int = 0, start_index: int = 0):
        if batteries > 1:
            largest = max(self.batteries[start_index:-batteries + 1])
        else:
            largest = max(self.batteries[start_index:])
        start_index += self.batteries[start_index:].index(largest) + 1
        joltage_so_far += largest
        if batteries > 1:
            return self.smart_joltage(batteries - 1, joltage_so_far * 10, start_index)
        return joltage_so_far


class Dec03(Day, year=2025, day=3, title='Lobby'):

    @staticmethod
    def parse_instructions(instructions):
        return [
            Bank([int(c) for c in line])
            for line in instructions
        ]

    @timer(part=1)
    def part_1(self):
        return sum(bank.smart_joltage(batteries=2) for bank in self.instructions)

    @timer(part=2)
    def part_2(self):
        return sum(bank.smart_joltage(batteries=12) for bank in self.instructions)


if __name__ == '__main__':
    with Timer('Total'):
        Dec03().run_day()
