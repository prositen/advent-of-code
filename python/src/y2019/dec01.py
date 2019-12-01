from python.src.common import Day


class Dec01(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2019, 1, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return [
            int(row) for row in instructions
        ]

    def part_1(self):
        return sum([self.fuel_cost(x) for x in self.instructions])

    @staticmethod
    def fuel_cost(mass):
        return max((mass // 3) - 2, 0)

    def part_2(self):
        total_weight = 0
        for module in self.instructions:
            fc = module
            while fc > 0:
                fc = self.fuel_cost(fc)
                total_weight += fc
        return total_weight


if __name__ == '__main__':
    d = Dec01()
    print("Fuel requirements: ", d.part_1())
    print("Total requirements: ", d.part_2())
