import itertools
from functools import cache

from python.src.common import Day, timer, Timer, get_points_between

"""
Thoughts: 

- Maximize the number of subsequent key-presses of the same kind, i.e.
  prefer ">>>^^^" over ">^>^>^" as this will mean fewer moves for the next level
  keypad.

- I don't think I need a BFS/DFS for this; I know where all the keys are. Best path
  should use as few "turns" as possible.
  
"""


class KeyPad(object):
    def __init__(self, target_keypad):
        self.keys = dict()
        self.blank = (0, 0)
        for y, row in enumerate(target_keypad):
            for x, ch in enumerate(row):
                if ch == ' ':
                    self.blank = (x, y)
                else:
                    self.keys[ch] = (x, y)

    @cache
    def path_between(self, key_1, key_2):
        """
        Maximize the number of subsequent key-presses of the same kind, i.e.
        prefer ">>>^^^" over ">^>^>^" as this will mean fewer moves for the next level
        keypad.

        Prefer long streaks of < since it's more expansive to reach.
        """
        pos_1, pos_2 = self.keys[key_1], self.keys[key_2]
        if pos_1 == pos_2:
            return 'A'
        dy = pos_2[1] - pos_1[1]
        cy = '^' if dy < 0 else 'v'

        if (dx := (pos_2[0] - pos_1[0])) < 0:
            cx = '<'
            if self.blank not in get_points_between(pos_1, (pos_1[0] + dx, pos_1[1])):
                code = cx * abs(dx) + cy * abs(dy)
            else:
                code = cy * abs(dy) + cx * abs(dx)
        else:
            cx = '>'
            if self.blank not in get_points_between(pos_1, (pos_1[0], pos_1[1] + dy)):
                code = cy * abs(dy) + cx * abs(dx)
            else:
                code = cx * abs(dx) + cy * abs(dy)

        return code + 'A'


class NumericalKeyPad(KeyPad):

    def __init__(self):
        super().__init__(['789', '456', '123', ' 0A'])


class DirectionalKeyPad(KeyPad):
    def __init__(self):
        super().__init__([' ^A', '<v>'])


class ReindeerStarship(object):

    def __init__(self):
        self.directional = DirectionalKeyPad()
        self.numerical = NumericalKeyPad()

    @cache
    def get_code_length(self, code, levels):
        if levels == 0:
            return len(code)
        return sum(
            self.get_code_length(
                self.directional.path_between(_from, _to),
                levels - 1
            )
            for _from, _to in zip('A' + code, code)
        )

    def complexity(self, code, levels):
        numerical = ''.join(self.numerical.path_between(_from, _to)
                            for _from, _to in zip('A' + code, code))
        return int(code[:-1]) * self.get_code_length(numerical, levels)


class Dec21(Day, year=2024, day=21, title='Keypad Conundrum'):

    @timer(part=1)
    def part_1(self):
        rs = ReindeerStarship()
        return sum(rs.complexity(code, levels=2) for code in self.instructions)

    @timer(part=2)
    def part_2(self):
        rs = ReindeerStarship()
        return sum(rs.complexity(code, levels=25) for code in self.instructions)


if __name__ == '__main__':
    with Timer('Total'):
        Dec21().run_day()
