from turtledemo.sorting_animate import instructions1

from python.src.common import Day, timer, Timer


class ToiletGrid:
    def __init__(self, grid_map):
        self.delta = {(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)}
        self.rolls_of_paper = grid_map
        self.neighbours = {
            pos: set(
                (pos[0] + delta[0], pos[1] + delta[1])
                for delta in self.delta
            )
            for pos in self.rolls_of_paper
        }

    def accessible(self, pos):
        return len(self.neighbours[pos].intersection(self.rolls_of_paper)) < 4

    def count_accessible(self):
        return sum(
            self.accessible(pos)
            for pos in self.rolls_of_paper
        )

    def remove_all_we_can(self):
        starting_rolls = len(self.rolls_of_paper)
        changes = True
        while changes:
            changes = False
            for roll in list(self.rolls_of_paper):
                if self.accessible(roll):
                    self.rolls_of_paper.remove(roll)
                    changes = True

        return starting_rolls - len(self.rolls_of_paper)


class Dec04(Day, year=2025, day=4, title='Printing Department'):

    @staticmethod
    def parse_instructions(instructions):
        return {
            (y, x)
            for y, line in enumerate(instructions)
            for x, ch in enumerate(line)
            if ch == '@'
        }

    @timer(part=1)
    def part_1(self):
        return ToiletGrid(self.instructions).count_accessible()

    @timer(part=2)
    def part_2(self):
        return ToiletGrid(self.instructions).remove_all_we_can()


if __name__ == '__main__':
    with Timer('Total'):
        Dec04().run_day()
