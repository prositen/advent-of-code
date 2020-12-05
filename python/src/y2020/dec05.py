from python.src.common import Day, timer, Timer


class Dec05(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 5, instructions, filename)

    @staticmethod
    def parse_instructions(instructions):
        return [Dec05.seat_id(i) for i in instructions]

    @staticmethod
    def seat_id(boarding_pass):
        row = boarding_pass[0:7].replace('F', '0').replace('B', '1')
        row_id = int(row, 2)
        seat = boarding_pass[7:].replace('L', '0').replace('R', '1')
        seat_id = int(seat, 2)
        return row_id * 8 + seat_id

    @timer(part=1)
    def part_1(self):
        return max(self.instructions)

    @timer(part=2)
    def part_2(self):
        seats = sorted(self.instructions)
        all_seats = set(range(seats[0], seats[-1] + 1))
        return all_seats.difference(seats).pop()


if __name__ == '__main__':
    with Timer():
        Dec05().run_day()
