import itertools

from python.src.common import Day, timer, Timer


class Dec02(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 2, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        rules = list()
        for i in instructions:
            rng, letter, pwd = i.split(' ')
            n1, n2 = (int(n) for n in rng.split('-'))
            rules.append(((n1, n2, letter[0]), pwd.strip()))
        return rules

    @staticmethod
    def is_valid_first(_from, _to, _letter, pwd):
        c = pwd.count(_letter)
        return _from <= c <= _to

    @staticmethod
    def is_valid_second(_i1, _i2, _letter, pwd):
        return (pwd[_i1 - 1] == _letter) ^ (pwd[_i2 - 1] == _letter)

    @timer(part=1)
    def part_1(self):
        return sum(self.is_valid_first(*rule, pwd) for rule, pwd in self.instructions)

    @timer(part=2)
    def part_2(self):
        return sum(self.is_valid_second(*rule, pwd) for rule, pwd in self.instructions)


if __name__ == '__main__':
    with Timer():
        d = Dec02()
        d.part_1()
        d.part_2()
