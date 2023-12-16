from collections import defaultdict

from python.src.common import Day, timer, Timer


class LensBoxes(object):

    def __init__(self):
        self.boxes = defaultdict(list)

    @staticmethod
    def parse_lens(value):
        for i, ch in enumerate(value):
            match ch:
                case '-':
                    return value[:i], '-', None
                case '=':
                    return value[:i], '=', int(value[i + 1:])
                case _:
                    continue
        return None

    def add_lens(self, lens):
        lens = self.parse_lens(lens)
        box_no = HASH(lens[0])
        if lens[1] == '=':
            for i, old_lens in enumerate(self.boxes[box_no]):
                if old_lens[0] == lens[0]:
                    self.boxes[box_no][i] = lens[0], lens[2]
                    break
            else:
                self.boxes[box_no].append((lens[0], lens[2]))
        else:
            for i, old_lens in enumerate(self.boxes[box_no]):
                if old_lens[0] == lens[0]:
                    self.boxes[box_no].remove(old_lens)

    def focusing_power(self):
        total = 0
        for box_no, lenses in self.boxes.items():
            for i, lens in enumerate(lenses, start=1):
                lens_power = (box_no + 1) * i * lens[1]
                total += lens_power
        return total


def HASH(value):
    cv = 0
    for ch in value:
        cv = (17 * (cv + ord(ch))) % 256
    return cv


class Dec15(Day, year=2023, day=15):

    @staticmethod
    def parse_instructions(instructions):
        return instructions[0].split(',')

    @timer(part=1)
    def part_1(self):
        return sum(HASH(value) for value in self.instructions)

    @timer(part=2)
    def part_2(self):
        lb = LensBoxes()
        for value in self.instructions:
            lb.add_lens(value)
        return lb.focusing_power()


if __name__ == '__main__':
    with Timer('Total'):
        Dec15().run_day()
