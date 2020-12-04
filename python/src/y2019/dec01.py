from python.src.common import Day, timer


class Dec01(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2019, 1, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_lines(instructions)

    @timer(part=1, title='Fuel requirements')
    def part_1(self):
        return sum([self.fuel_cost(x) for x in self.instructions])

    @staticmethod
    def fuel_cost(mass):
        return max((mass // 3) - 2, 0)

    @timer(part=2, title='Total requirements')
    def part_2(self):
        total_weight = 0
        for module in self.instructions:
            fc = module
            while fc > 0:
                fc = self.fuel_cost(fc)
                total_weight += fc
        return total_weight


if __name__ == '__main__':
    Dec01().run_day()
