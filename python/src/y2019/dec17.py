from python.src.common import Day
from python.src.y2019.intcode import IntCode


class Dec17(Day):
    def __init__(self, filename=None, instructions=None):
        super().__init__(2019, 17, filename=filename, instructions=instructions)
        self.width, self.height = 0, 0
        self.bot_x, self.bot_y = 0, 0

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)

    def part_1(self):
        ic = IntCode(self.instructions)
        ic.run()
        view = ''.join(chr(c) for c in ic.output).strip()
        bot_pos = view.index('^')
        print(view)
        view = view.split('\n')
        self.width = len(view[0])
        self.height = len(view)
        self.bot_y, self.bot_x = divmod(bot_pos, self.width)
        return self.alignment_parameters(view)

    def part_2(self):
        """
        F12,L,F8,L,F8,L,F12,R,F4,L,F12,R,F6,L,F12,L,F8,L,F8,R,F4,L,F12,L,F12,R,F6,L,F12,R,F6,L,F12,R,F6,L,F12,L,F8,L ,F8,R,F4,L,F12,L,F12,R,F6,L,F12,L,F8,L,F8,R,F4,L,F12,L,F12,R,F6,L,F12,R,F4,L,F12,R,F6
        """
        pass

    def alignment_parameters(self, view):
        alignment = 0
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                if view[y][x] == '#' and (
                        view[y - 1][x] == '#' and
                        view[y + 1][x] == '#' and
                        view[y][x - 1] == '#' and
                        view[y][x + 1] == '#'
                ):
                    alignment += y * x
        return alignment


if __name__ == '__main__':
    day = Dec17()
    print("Part 1:", day.part_1())
    print("Part 2:", day.part_2())
