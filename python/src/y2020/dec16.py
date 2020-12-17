from python.src.common import Day, timer, Timer


class Dec16(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 16, instructions, filename)
        groups = self.instructions
        self.rules = dict()
        for line in groups[0]:
            name, numbers = line.split(':')
            self.rules[name] = list()
            for pair in numbers.strip().split(' or '):
                a, b = map(int, pair.split('-'))
                self.rules[name].append((a, b))
        self.my_ticket = list(map(int, groups[1][1].split(',')))
        self.other_tickets = [tuple(map(int, line.split(',')))
                              for line in groups[2][1:]]

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_groups(instructions)

    def check_rule(self, rule, number):
        return any(a <= number <= b for a, b in self.rules[rule])

    @timer(part=1)
    def part_1(self):
        errors = 0
        for ticket in self.other_tickets:
            for number in ticket:
                if not any(self.check_rule(r, number) for r in self.rules):
                    errors += number
        return errors

    @timer(part=2)
    def part_2(self):
        return 0


if __name__ == '__main__':
    with Timer('Total'):
        d = Dec16()
        d.part_1()
        d.part_2()
