import functools
import math
import operator
import re
from collections import Counter
from dataclasses import dataclass

from python.src.common import Day, timer, Timer


@dataclass
class Robot(object):
    pos_x: int
    pos_y: int
    vel_x: int
    vel_y: int
    max_x: int
    max_y: int

    @property
    def mid_x(self):
        return (self.max_x - 1) // 2

    @property
    def mid_y(self):
        return (self.max_y - 1) // 2

    def move(self, steps=1):
        self.pos_x = (self.pos_x + self.vel_x * steps) % self.max_x
        self.pos_y = (self.pos_y + self.vel_y * steps) % self.max_y

    @property
    def quadrant(self):
        if self.pos_x < math.floor(self.mid_x):
            if self.pos_y < math.floor(self.mid_y):
                return 'TL'
            elif self.pos_y > math.ceil(self.mid_y):
                return 'BL'
        elif self.pos_x > math.ceil(self.mid_x):
            if self.pos_y < math.floor(self.mid_y):
                return 'TR'
            elif self.pos_y > math.ceil(self.mid_y):
                return 'BR'
        return 'M'


class Bathroom(object):

    def __init__(self, robots, max_x, max_y):
        self.robots = [
            Robot(*l,
                  max_y=max_y, max_x=max_x)
            for l in robots]
        self.unique_positions = Counter((r.pos_x, r.pos_y) for r in self.robots)

    def move_robots(self, steps=1):
        for robot in self.robots:
            self.unique_positions[(robot.pos_x, robot.pos_y)] -= 1
            robot.move(steps)
            self.unique_positions[(robot.pos_x, robot.pos_y)] += 1

    def safety_factor(self):
        c = Counter(robot.quadrant for robot in self.robots)
        c.pop('M', None)
        return functools.reduce(operator.mul, c.values(), 1)

    def is_christmas_tree(self):
        # Check if all robots are on a unique position
        # This isn't necessarily the solution but for me it was
        return self.unique_positions.most_common(1)[0][1] == 1


class Dec14(Day, year=2024, day=14, title='Restroom Redoubt'):

    @staticmethod
    def parse_instructions(instructions):
        pattern = re.compile(r'(-?\d+)')
        return [
            tuple(map(int, pattern.findall(line)))
            for line in instructions
        ]

    @timer(part=1)
    def part_1(self, max_y=103, max_x=101):
        br = Bathroom(robots=self.instructions,
                      max_y=max_y, max_x=max_x)
        br.move_robots(steps=100)

        return br.safety_factor()

    @timer(part=2)
    def part_2(self):
        br = Bathroom(robots=self.instructions,
                      max_y=103, max_x=101)
        step = 0
        while not br.is_christmas_tree():
            step += 1
            br.move_robots()


        for y in range(103):
            row = list()
            for x in range(101):
                if br.unique_positions[(x, y)] > 0:
                    row.append('#')
                else:
                    row.append('.')
            print(''.join(row))
        return step

if __name__ == '__main__':
    with Timer('Total'):
        Dec14().run_day()
