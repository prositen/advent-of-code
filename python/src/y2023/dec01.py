from python.src.common import Day, timer, Timer


class Dec01(Day, year=2023, day=1):

    @staticmethod
    def first_digit(line):
        for c in line:
            if '0' <= c <= '9':
                return int(c)

    @timer(part=1)
    def part_1(self):
        return sum(10 * self.first_digit(line) + self.first_digit(line[::-1])
                   for line in self.instructions)

    digits = {
        'z': {'zero': 0},
        'o': {'one': 1},
        't': {'two': 2, 'three': 3},
        'f': {'four': 4, 'five': 5},
        's': {'six': 6, 'seven': 7},
        'e': {'eight': 8},
        'n': {'nine': 9}
    }

    @classmethod
    def tokenize(cls, line):
        tokens = list()
        for i in range(len(line)):
            c = line[i]
            if '0' <= c <= '9':
                tokens.append(int(c))
            elif c in cls.digits:
                for num, dig in cls.digits[c].items():
                    if line[i:].startswith(num):
                        tokens.append(dig)
                        break
            i += 1
        return tokens

    @timer(part=2)
    def part_2(self):
        calibration_value = 0
        for line in self.instructions:
            tokens = self.tokenize(line)
            calibration_value += (10 * tokens[0] + tokens[-1])
        return calibration_value


if __name__ == '__main__':
    with Timer('Total'):
        Dec01().run_day()
