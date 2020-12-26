from python.src.common import Day, timer, Timer


class Dec04(Day, year=2020, day=4):
    PASSPORT_RULES = {
        'byr': lambda x: len(x) == 4 and 1920 <= int(x) <= 2020,
        'iyr': lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
        'eyr': lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
        'hgt': lambda x: (x.endswith('cm') and (150 <= int(x[:-2]) <= 193) or
                          x.endswith('in') and (59 <= int(x[:-2]) <= 76)),
        'hcl': lambda x: (len(x) == 7 and x[0] == '#' and
                          all(c in '0123456789abcdef' for c in x[1:])),
        'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        'pid': lambda x: len(x) == 9 and x.isnumeric(),
        'cid': lambda x: True
    }
    FIELDS = set(PASSPORT_RULES.keys()).difference({'cid'})

    @staticmethod
    def parse_instructions(instructions):
        passports = list()
        for group in Day.parse_groups(instructions):
            current = dict()
            for row in group:
                current |= (tuple(rr.split(':')) for rr in row.split(' '))
            passports.append(current)
        return passports

    @timer(part=1)
    def part_1(self):
        return sum(self.check_passport(passport) for passport in self.instructions)

    @classmethod
    def check_passport(cls, passport, check_validity=False):
        if not cls.FIELDS.intersection(passport.keys()) == cls.FIELDS:
            return False
        valid = True
        if check_validity:
            for k, v in passport.items():
                valid &= cls.PASSPORT_RULES[k](v)
        return valid

    @timer(part=2)
    def part_2(self):
        return sum(self.check_passport(passport, True) for passport in self.instructions)


if __name__ == '__main__':
    with Timer('Passport Processing'):
        Dec04().run_day()
