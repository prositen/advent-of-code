from collections import defaultdict

from python.src.common import Day, timer, Timer


class Sheet(object):

    def __init__(self, dots):
        self.dots = defaultdict(set)
        for x, y in dots:
            self.dots[x].add(y)

    def fold_left(self, position):
        for x, ys in list(self.dots.items()):
            if x >= position:
                new_x = 2 * position - x
                self.dots[new_x].update(ys)
                del self.dots[x]

    def fold_up(self, position):
        for x, ys in list(self.dots.items()):
            for y in list(ys):
                if y >= position:
                    new_y = 2 * position - y
                    self.dots[x].add(new_y)
                    self.dots[x].remove(y)

    def fold(self, folds):
        for direction, position in folds:
            if direction == 'x':
                self.fold_left(position)
            else:
                self.fold_up(position)

    def count(self):
        return sum(len(self.dots[x]) for x in self.dots)

    def __repr__(self):
        min_x = min(self.dots)
        max_x = max(self.dots)
        text = ['']
        for y in range(max(self.dots[min_x])+1):
            line = list()
            for x in range(max_x+1):
                line.append('X' if x in self.dots and y in self.dots[x] else ' ')
            text.append(''.join(line))
        return '\n'.join(text)


class Dec13(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 13, instructions, filename)
        self.dots, self.folds = self.instructions

    @staticmethod
    def parse_instructions(instructions):
        dots = list()
        i = 0
        for i, line in enumerate(instructions):
            if not line.strip():
                break
            part = line.split(',')
            dots.append((int(part[0], 10), int(part[1], 10)))

        folds = [
            ((part := line[11:].split('='))[0], int(part[1]))
            for line in instructions[i + 1:]
        ]
        return dots, folds

    @timer(part=1)
    def part_1(self):
        s = Sheet(self.dots)
        s.fold([self.folds[0]])
        return s.count()

    @timer(part=2)
    def part_2(self):
        s = Sheet(self.dots)
        s.fold(self.folds)
        return s


if __name__ == '__main__':
    with Timer('Transparent Origami'):
        Dec13().run_day()
