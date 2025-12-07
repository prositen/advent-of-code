from collections import Counter

from python.src.common import Day, timer, Timer


class Manifold:
    def __init__(self, start, lines):
        self.start = start
        self.lines = lines

    def count_splits(self):
        beams = {self.start}
        splits = 0
        for line in self.lines:
            new_beams = set()
            for beam in beams:
                if line[beam] == '.':
                    new_beams.add(beam)
                else:
                    splits += 1
                    if beam > 0:
                        new_beams.add(beam - 1)
                    if beam < len(line) - 1:
                        new_beams.add(beam + 1)
            beams = new_beams
        return splits

    def count_timelines(self):
        beams = {self.start: 1}
        for line in self.lines:
            new_beams = Counter()
            for beam, count in beams.items():
                if line[beam] == '.':
                    new_beams[beam] += count
                else:
                    if beam > 0:
                        new_beams[beam - 1] += count
                    if beam < len(line) - 1:
                        new_beams[beam + 1] += count
            beams = new_beams
        return sum(beams.values())


class Dec07(Day, year=2025, day=7, title='Laboratories'):
    @staticmethod
    def parse_instructions(instructions):
        start = instructions[0].index('S')
        return start, instructions[1:]

    @timer(part=1)
    def part_1(self):
        return Manifold(self.instructions[0], self.instructions[1]).count_splits()

    @timer(part=2)
    def part_2(self):
        return Manifold(self.instructions[0], self.instructions[1]).count_timelines()


if __name__ == '__main__':
    with Timer('Total'):
        Dec07().run_day()
