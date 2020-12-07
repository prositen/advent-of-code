from python.src.common import Day, timer
from python.src.y2019.intcode import IntCode


class Dec19(Day):
    def __init__(self, filename=None, instructions=None):
        super().__init__(2019, 19, filename=filename, instructions=instructions)
        self.coords = dict()
        self.line_equations = list()

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)

    @timer(part=1, title='Points affected')
    def part_1(self):
        area = 0
        min_x = 0
        xs = list()
        for y in range(0, 50):
            first_x = 0
            last_x = 0
            for x in range(min_x, 50):
                hit = self.scan_coordinate(x, y)
                if hit:
                    area += 1
                    if not first_x:
                        first_x = x
                elif first_x:
                    last_x = x - 1
                    break
            if y in (20, 40):
                xs.append((first_x, last_x))

            min_x = first_x

        slopes = tuple((40 - 20) / (xs[1][n] - xs[0][n]) for n in (0, 1))
        ms = [20 - slopes[n] * xs[n][0] for n in (0, 1)]
        self.line_equations = [(slopes[n], ms[n]) for n in (0, 1)]
        return area

    def scan_coordinate(self, x, y):
        if (y, x) not in self.coords:
            ic = IntCode(self.instructions)
            ic.add_input(x)
            ic.add_input(y)
            ic.run()
            self.coords[(y, x)] = ic.get_output()
        return self.coords[(y, x)]

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

    @timer(part=2, title='X * 10000 + Y for closest point that fits the ship')
    def part_2(self):
        """
        At which distance from the emitter do we have a width large enough
        to fit the ship? Start scanning here!
        
        In part 1 we calculated the slopes of the emitter beam. Now find
        the y where the distance between the lines is at least 100.
        
        (y-m1)/k1 - (y-m2)/k2 = 100
        
        k1*k2*100 = k2(y-m1) - k1(y-m2)
        k1*k2*100 = y*k2 - m1*k2 - y*k1 + k1*m2
        y(k2-k1) - m1*k2 + k1*m2 = k1*k2*100
        y(k2-k1) = k1*k2*100 - m1*k2 + k1*m2
        y = (k1*k2*100 - m1*k2 + k1*m2)/(k2 - k1)                
        x = (y-m)/k
        """
        k_2, m_2 = self.line_equations[1]
        k_1, m_1 = self.line_equations[0]
        y = int((k_2*k_1*110 - k_1*m_2 + k_2*m_1)/(k_1-k_2))
        x = int((y-m_1)/k_1)

        while True:
            bottom_left, top_right = self.fits_ship(y=y, x=x)
            if bottom_left:
                if top_right:
                    return (10000 * x) + y - 99
                else:  # Move down
                    y += 1
            else:  # Move right
                x += 1


if __name__ == '__main__':
    Dec19().run_day()
