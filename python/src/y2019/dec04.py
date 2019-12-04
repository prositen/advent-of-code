from python.src.common import Day


def is_valid_password(password, max_repeated=6):
    found_double = False
    rep_count = 0
    prev = password[0]
    for c in password[1:]:
        if c == prev:
            rep_count += 1
        elif prev > c:
            return False
        else:
            found_double |= (0 < rep_count < max_repeated)
            rep_count = 0
        prev = c
    return found_double or 0 < rep_count < max_repeated


class Dec04(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2019, 3, instructions, filename)

    def get_count(self, max_repeated=6):
        return len(list(filter(lambda x: is_valid_password(str(x), max_repeated),
                               range(self.instructions[0], self.instructions[1])
                               )))

    def part_1(self):
        return self.get_count()

    def part_2(self):
        return self.get_count(max_repeated=2)


if __name__ == '__main__':
    d = Dec04(instructions=(138307, 654504))
    print("Number of valid passwords", d.part_1())
    print("Passwords with extra check", d.part_2())
