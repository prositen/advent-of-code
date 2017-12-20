import os

from python.src.y2017.common import DATA_DIR

class Routing(object):

    def __init__(self, puzzle_input):
        self.diagram = puzzle_input
        self.path = []
        self.pos = (0,0)
        self.d = (1,0)
        self.steps = 0
        self.max_x = len(self.diagram[0])
        self.max_y = len(self.diagram)

    def walk_left_right(self):
        aa = self.diagram[self.pos[0]][self.pos[1]]
        while aa in ('|', '-'):
            self.pos = self.pos[0] + self.d[0], self.pos[1] + self.d[1]
            self.steps += 1
            aa = self.diagram[self.pos[0]][self.pos[1]]
        if aa == '+':
            if self.pos[0] > 0 and self.diagram[self.pos[0]-1][self.pos[1]] != ' ':
                self.pos = self.pos[0] - 1, self.pos[1]
                self.d = (-1, 0)
            else:
                self.pos = self.pos[0] + 1, self.pos[1]
                self.d = (1, 0)
            self.steps += 1
            return self.walk_up_down()
        elif aa.isalpha():
            self.steps += 1
            self.path.append(aa)
            self.pos = self.pos[0] + self.d[0], self.pos[1] + self.d[1]
            return self.walk_left_right()
        else:
            return "".join(self.path)

    def walk_up_down(self):
        aa = self.diagram[self.pos[0]][self.pos[1]]
        while aa in ('|', '-'):
            self.pos = self.pos[0] + self.d[0], self.pos[1] + self.d[1]
            self.steps += 1
            aa = self.diagram[self.pos[0]][self.pos[1]]
        if aa == '+':
            if self.pos[1] > 0 and self.diagram[self.pos[0]][self.pos[1]-1] != ' ':
                self.pos = self.pos[0], self.pos[1] - 1
                self.d = (0, -1)
            else:
                self.pos = self.pos[0], self.pos[1] + 1
                self.d = (0, 1)
            self.steps += 1
            return self.walk_left_right()
        elif aa.isalpha():
            self.steps += 1
            self.path.append(aa)
            self.pos = self.pos[0] + self.d[0], self.pos[1] + self.d[1]
            return self.walk_up_down()
        else:
            return "".join(self.path)
    #def walk(self):
    #    aa = self.square()
    #    while aa in ('|', '-'):
    #        self.move()
    #        self.steps += 1
    #    if aa == '+'

    def move(self):
        self.pos = self.pos[0] + self.d[0], self.pos[1] + self.d[1]

    def square(self, dy=0, dx=0):
        y = self.pos[0] + dy
        x = self.pos[1] + dx
        if 0 <= y < self.max_y and 0 <= x <= self.max_x:
            return self.diagram[y][x]
        else:
            return ' '


    def part_1(self):
        self.pos = (0, self.diagram[0].index('|'))
        self.d = (1,0)
        return self.walk_up_down()

    def part_2(self):
        return self.steps
def main():
    with open(os.path.join(DATA_DIR, 'input.19.txt')) as fh:
        puzzle_input = ["{:205}".format(line) for line in fh.readlines()]
    """
    puzzle_input = [
        "     |          ",
        "     |  +--+    ",
        "     A  |  C    ",
        " F---|----E|--+ ",
        "     |  |  |  D ",
        "     +B-+  +--+ "]
    """
    r = Routing(puzzle_input)
    print("Part 1:", r.part_1())
    print("Part 2:", r.part_2())

if __name__ == '__main__':
    main()
