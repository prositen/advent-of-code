from python.src.common import Day, timer, Timer


class Dec25(Day, year=2022, day=25):

    @timer(part=1)
    def part_1(self):
        number = sum(self.convert_from_snafu(i) for i in self.instructions)
        return self.convert_to_snafu(number)


    @staticmethod
    def convert_from_snafu(snafu):
        lookup = {
            '1': 1,
            '2': 2,
            '0': 0,
            '-': -1,
            '=': -2
        }
        digits = [lookup[c] for c in snafu]
        t = 0
        for i, d in enumerate(digits[::-1]):
            t += d * 5**i
        return t
    @staticmethod
    def convert_to_snafu(number):
        digits = []
        lookup = {
            -2: '=',
            -1: '-',
            0: '0',
            1: '1',
            2: '2'
        }
        while number:
            number, rest = divmod(number, 5)
            if rest > 2:
                rest -= 5
                number += 1
            digits.append(lookup[rest])
        return ''.join(digits[::-1])

if __name__ == '__main__':
    with Timer('Total'):
        Dec25().part_1()
