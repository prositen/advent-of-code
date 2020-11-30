from python.src.common import Day, timer
from python.src.y2019.intcode import IntCode


class Dec19(Day):
    def __init__(self, filename=None, instructions=None):
        super().__init__(2019, 19, filename=filename, instructions=instructions)
        self.coords = dict()

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)

    @timer(part=1)
    def part_1(self):
        area = 0
        min_x = 0
        for y in range(0, 50):
            first_x = 0
            for x in range(min_x, 50):
                hit = self.scan_coordinate(x, y)
                if hit:
                    area += 1
                    if not first_x:
                        first_x = x
            min_x = first_x
        return area

    def scan_coordinate(self, x, y):
        if (y, x) not in self.coords:
            ic = IntCode(self.instructions)
            ic.add_input(x)
            ic.add_input(y)
            ic.run()
            self.coords[(y, x)] = ic.get_output()
        return self.coords[(y, x)]

    def try_line(self, y, width=1, x_start=0):
        x = x_start
        beam_start = 0
        while not beam_start:
            if self.scan_coordinate(x=x, y=y):
                beam_start = x
            x += 1
        x = beam_start + width - 1
        coord = self.scan_coordinate(x=x, y=y)
        if not coord:
            return beam_start, 0
        beam_end = 0
        while not beam_end and x < (beam_start + 3 * width):
            if not self.scan_coordinate(x=x, y=y):
                beam_end = x - 1
            x += 1
        return beam_start, beam_end

    def fits_ship(self, y, x, size=100):
        """
        :return (bottom left corner is in beam,
                 top right corner is in beam)
        """
        if self.scan_coordinate(y=y, x=x):
            if self.scan_coordinate(y=y - size + 1, x=x + size - 1):
                return True, True
            return True, False
        return False, False

    @timer(part=2)
    def part_2(self):
        x = 500
        y = 1000

        while True:
            bl, tr = self.fits_ship(y=y, x=x)
            if bl:
                if tr:
                    return (10000 * x) + y - 99
                else:
                    y += 1
            else:
                x += 1


if __name__ == '__main__':
    day = Dec19()
    day.part_1()
    day.part_2()
