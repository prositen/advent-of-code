import re

from python.src.common import Day, timer, Timer


class Dec03(Day, year=2024, day=3, title='Mull it over'):
    mul_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

    @staticmethod
    def parse_instructions(instructions):
        return ''.join(instructions)

    @timer(part=1)
    def part_1(self):
        return sum(int(m[0]) * int(m[1]) for m in self.mul_pattern.findall(self.instructions))

    @timer(part=2)
    def part_2(self):
        removed_dont_do = re.sub(r"don't\(\).*?do\(\)",
                                 '',
                                 self.instructions + 'do()')
        return sum(int(m[0]) * int(m[1]) for m in self.mul_pattern.findall(removed_dont_do))


if __name__ == '__main__':
    with Timer('Total'):
        Dec03().run_day()
