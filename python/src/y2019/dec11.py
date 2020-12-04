from collections import defaultdict
from python.src.common import Day
from python.src.y2019.intcode import IntCode


class PaintBot(object):

    def __init__(self):
        self.panels = defaultdict(bool)
        self.pos = (0, 0)
        self.d = (0, -1)

    def turn(self, turn_right):
        if turn_right:
            self.d = -self.d[1], self.d[0]
        else:
            self.d = self.d[1], -self.d[0]
        self.pos = self.pos[0] + self.d[0], self.pos[1] + self.d[1]

    def cam(self):
        return self.panels.get(self.pos, False)

    def paint(self, color):
        self.panels[self.pos] = color

    def print(self):
        minx = min(self.panels)[0]
        maxx = max(self.panels)[0]
        miny = min(self.panels, key=lambda x: x[1])[1]
        maxy = max(self.panels, key=lambda x: x[1])[1]
        output = [[' '] * (1 + maxx - minx) for _ in range(1 + maxy - miny)]
        for k, v in self.panels.items():
            posy = k[1] - miny
            posx = k[0] - minx
            output[posy][posx] = '#' if v else ' '

        for row in output:
            print(''.join(row))


class Dec11(Day):

    def __init__(self, filename=None, instructions=None):
        super().__init__(2019, 11, instructions, filename)
        self.panels = defaultdict(bool)
        self.pos = (0, 0)
        self.cur_dir = (0, -1)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions)

    @staticmethod
    def turn(current_dir, turn_right):
        if turn_right:
            return -current_dir[1], current_dir[0]
        else:
            return current_dir[1], -current_dir[0]

    def paint(self, ic, pb, start):
        ic.add_input(start)
        while not ic.run_and_wait():
            color = ic.get_output(pos=0)
            if color is not None:
                pb.paint(color)
                turn_right = ic.get_output(pos=0)
                pb.turn(turn_right=turn_right)

            cam = int(pb.cam())
            ic.add_input(cam)

        color = ic.get_output(pos=0)
        if color:
            pb.paint(color)

    def part_1(self):
        ic = IntCode(instructions=self.instructions)
        pb = PaintBot()
        self.paint(ic, pb, start=0)
        return len(pb.panels)

    def part_2(self):
        ic = IntCode(instructions=self.instructions)
        pb = PaintBot()
        self.paint(ic, pb, start=1)
        pb.print()


if __name__ == '__main__':
    d = Dec11()
    print("Part 1:", d.part_1())
    print("Part 2:")
    d.part_2()
