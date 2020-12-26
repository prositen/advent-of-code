from python.src.common import Day, timer, Timer


class Dec05(Day, year=2020, day=5):
    @staticmethod
    def parse_instructions(instructions):
        return sorted([Dec05.seat_id(i) for i in instructions])

    @staticmethod
    def seat_id(boarding_pass):
        row = boarding_pass.translate(str.maketrans('FBLR', '0101'))
        return int(row, 2)

    @timer(part=1)
    def part_1(self):
        return self.instructions[-1]

    @timer(part=2)
    def part_2(self):
        seats = self.instructions
        all_seats = set(range(seats[0], seats[-1] + 1))
        return all_seats.difference(seats).pop()


if __name__ == '__main__':
    with Timer('Binary Boarding'):
        Dec05().run_day()
