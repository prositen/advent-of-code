import os
import re
import time
from functools import wraps


def timer(part, show_result=True, title=''):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = f(*args, **kwargs)
            if show_result:
                header = title or f'  - Part {part}'
                print(f'{header}: {result if result else ""}  '
                      f'{(time.time() - start_time) * 1e3:.2f} ms')
            return result

        return wrapper

    return decorator


class Timer(object):
    def __init__(self, title=''):
        self.start_time = 0
        self.title = f'{title}: ' if title else ''

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, *exc_info):
        elapsed_time = time.time() - self.start_time
        print(f'{self.title}{elapsed_time * 1e3:.2f} ms')


def input_for(year, day):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..',
                        'data', str(year), 'input.{}.txt'.format(day))


_registry = dict()


class Day(object):

    @staticmethod
    def get_all_days(year):
        return _registry.get(year, dict())

    def __init_subclass__(cls, year=None, day=None, title=None, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.year = year
        cls.day = day or 0
        cls.title = title
        if year not in _registry:
            _registry[year] = dict()
        _registry[year][day] = cls

    def __init__(self, year=None, day=None, instructions=None, filename=None):
        if day:
            self.day = day
        if year and not self.year:
            self.year = year
            self.title = f'{self.year}-12-{self.day:02}'
        if not instructions:
            instructions = self.read_input(filename)
        self.instructions = self.parse_instructions(instructions)

    @staticmethod
    def parse_instructions(instructions):
        return instructions

    @staticmethod
    def parse_int_line(instructions, separator=','):
        return [int(c) for c in instructions[0].split(separator)]

    @staticmethod
    def parse_multiple_ints_per_line(instructions, separator=','):
        return [
            [int(c) for c in re.split(separator, line)]
            for line in instructions
        ]

    @staticmethod
    def parse_digits(instructions):
        return [int(c) for c in instructions[0]]

    @staticmethod
    def parse_int_lines(instructions):
        return [int(row) for row in instructions]

    @staticmethod
    def parse_groups(instructions):
        result = list()
        g = list()
        for row in instructions:
            if len(row.strip()):
                g.append(row)
            else:
                result.append([r for r in g])
                g = []
        if g:
            result.append(g)
        return result

    def read_input(self, filename=None):
        """ If filename is given, use that. Otherwise,  default to data/<year>/input.<day>.txt """
        if filename is None:
            filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..',
                                    'data', str(self.year), 'input.{}.txt'.format(self.day))
        with open(filename) as fh:
            return [x.rstrip('\n') for x in fh.readlines()]

    def part_1(self):
        return 0

    def part_2(self):
        return 0

    def run_day(self):
        print(f'{self.year}-12-{self.day:02}{" - " if self.title else ""}{self.title}')
        self.part_1()
        self.part_2()


def stringify(int_list, separator=','):
    return separator.join(str(c) for c in int_list)


def sgn(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


def get_int_at(line, pos=-1):
    return int(line.split()[pos])


def distance(point, other):
    return sum(abs(p - o) for p, o in zip(point, other))
