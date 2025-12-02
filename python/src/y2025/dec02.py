import math

from python.src.common import Day, timer, Timer


class GiftShopDatabase:
    def __init__(self, product_ids):
        self.product_ids = product_ids
        self.longest_id = max(len(x[1]) for x in self.product_ids)
        self.invalid_sum = 0

    def identify_repeated_twice(self):
        for id_range in self.product_ids:
            self.invalidate_part_1(id_range)
        return self.invalid_sum

    def identify_repeated_at_least_twice(self):
        for id_range in self.product_ids:
            self.invalidate(id_range)
        return self.invalid_sum

    def invalidate(self, id_range):
        """
        :param id_range:
        :return:
        """
        start, end = id_range
        n_start, n_end = int(start), int(end)
        l_start, l_end = len(start), len(end)

        invalid_digits = set()
        for id_length in range(1, 1 + l_end // 2):
            if l_start % id_length and l_start == l_end:
                # No invalid IDs of this length
                continue

            for repeat in range(l_start // id_length, 1 + l_end // id_length):
                for id_part in range(10 ** (id_length - 1), 10 ** id_length):
                    possibly_silly = int(repeat * str(id_part))
                    if possibly_silly < 10:
                        continue
                    if n_start <= possibly_silly <= n_end:
                        invalid_digits.add(possibly_silly)

                    elif possibly_silly > n_end:
                        break
        self.invalid_sum += sum(invalid_digits)


    def invalidate_part_1(self, id_range):
        """
        :param id_range:
        :return:
        """
        start, end = id_range
        n_start, n_end = int(start), int(end)

        l_start, l_end = len(start), len(end)
        if l_start < l_end:
            start = start[:-1] + '0'

        if l_start % 2 and l_start == l_end:
            return
        l_start = max(l_start // 2, 1)

        if l_end % 2:
            l_end = 1 + l_end // 2
        else:
            l_end = l_end // 2

        iter_start = max(int(start[:l_start]), 1)
        iter_end = int(end[:l_end])

        for num in range(iter_start, iter_end + 1):
            p = math.floor(math.log10(num) + 1)
            possibly_silly = num * (10 ** p) + num
            if n_start <= possibly_silly <= n_end:
                self.invalid_sum += possibly_silly
            elif possibly_silly > n_end:
                break


class Dec02(Day, year=2025, day=2, title='Gift Shop'):

    @staticmethod
    def parse_instructions(instructions):
        return [
            line.split('-', 1)
            for line in instructions[0].split(',')
        ]

    @timer(part=1)
    def part_1(self):
        gs = GiftShopDatabase(self.instructions)
        return gs.identify_repeated_twice()

    @timer(part=2)
    def part_2(self):
        gs = GiftShopDatabase(self.instructions)
        # 48631959042 too high
        return gs.identify_repeated_at_least_twice()


if __name__ == '__main__':
    with Timer('Total'):
        Dec02().run_day()
