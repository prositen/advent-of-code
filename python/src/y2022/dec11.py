import logging
from collections import defaultdict

from python.src.common import Day, timer, Timer, get_int_at

logging.basicConfig(filename='monkeys.log', level=logging.WARNING)


class Monkey(object):

    def __init__(self, instructions, relief):
        self.number = get_int_at(instructions[0][:-1])
        self.items = [int(i) for i in instructions[1].split(':')[1].split(',')]

        self.relief = relief
        self.no_relief = 0
        op = instructions[2].split()
        self.operation = self.get_operation(op[-2], op[-1])
        self.test_and_throw = self.get_test_and_throw(*instructions[3:6])
        self.inspections = 0

    def step(self):
        logging.info(f'Monkey {self.number}')
        throw_to = defaultdict(list)
        while self.items:
            item = self.items.pop()
            self.inspections += 1
            logging.info(f'  Monkey inspects an item with a worry level of {item}')
            item = self.operation(item)
            logging.info(f'  New worry level is {item}')

            if self.relief:
                item = item // self.relief
                logging.info(
                    f'  Monkey gets bored with item. Worry level is divided by 3 to {item}')
            else:
                item = item % self.no_relief
                logging.info(
                    f'  Monkey gets bored with item. Worry level modulo {self.no_relief} is {item}'
                )

            new_monkey = self.test_and_throw(item)
            throw_to[new_monkey] += [item]
            logging.info(f'  Item with worry level {item} is thrown to monkey {new_monkey}')
        return throw_to

    @staticmethod
    def get_operation(operator, operand):
        match (operator, operand):
            case ('*', 'old'):
                return lambda c: c * c
            case ('*', number):
                return lambda c: c * int(number)
            case ('+', 'old'):
                return lambda c: c + c
            case ('+', number):
                return lambda c: c + int(number)

    def get_test_and_throw(self, test_line, true_line, false_line):
        divisible_by = get_int_at(test_line)
        self.no_relief = divisible_by
        throw_true = get_int_at(true_line)
        throw_false = get_int_at(false_line)
        return lambda c: throw_true if (c % divisible_by == 0) else throw_false


class Dec11(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2022, 11, instructions, filename)
        self.monkeys = None

    def reset_monkeys(self, relief=3):
        self.monkeys = [
            Monkey(group, relief=relief) for group in self.instructions
        ]
        if not relief:
            no_relief = 1
            for m in self.monkeys:
                no_relief *= m.no_relief
            for m in self.monkeys:
                m.no_relief = no_relief

    @staticmethod
    def parse_instructions(instructions):
        return Dec11.parse_groups(instructions)

    def run(self, steps):
        for _ in range(steps):
            logging.info(f'Step {_}')
            for monkey in self.monkeys:
                throw_to = monkey.step()
                for mi, items in throw_to.items():
                    self.monkeys[mi].items.extend(items)

        s = sorted(self.monkeys, key=lambda k: -k.inspections)
        return s[0].inspections * s[1].inspections

    @timer(part=1)
    def part_1(self):
        self.reset_monkeys(relief=3)
        return self.run(20)

    @timer(part=2)
    def part_2(self):
        self.reset_monkeys(relief=0)
        return self.run(10000)


if __name__ == '__main__':
    with Timer('Total'):
        Dec11().run_day()
