import math
from collections import defaultdict

from python.src.common import Day, timer, Timer


class StoneCorridor(object):

    def __init__(self, stones):
        self.stones = stones
        self.lookup: dict[(int, int):int] = dict()

    def blink_stone(self, stone: int) -> list[int]:
        if stone == 0:
            result = [1]
        else:
            p = math.floor(math.log10(stone) + 1)
            if p % 2 == 0:
                half = p // 2
                left, right = divmod(stone, 10 ** half)
                result = [left, right]
            else:
                result = [stone * 2024]
        self.lookup[(stone, 1)] = len(result)
        return result

    def dp(self, stone: int, times):
        if (stone, times) in self.lookup:
            return self.lookup[(stone, times)]
        else:
            stone_result = self.blink_stone(stone)
            if times > 1:
                self.lookup[(stone, times)] = sum(self.dp(s, times - 1) for s in stone_result)
            return self.lookup[(stone, times)]

    def blink(self, times=1):
        return sum(self.dp(stone, times) for stone in self.stones)


class Dec11(Day, year=2024, day=11, title='Plutonian Pebbles'):

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_int_line(instructions, separator=' ')

    @timer(part=1)
    def part_1(self):
        return StoneCorridor(self.instructions).blink(25)

    @timer(part=2)
    def part_2(self):
        return StoneCorridor(self.instructions).blink(75)


if __name__ == '__main__':
    with Timer('Total'):
        Dec11().run_day()
