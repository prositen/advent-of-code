import os
import time
from functools import wraps


def timer(part, show_result=True, title=''):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = f(*args, **kwargs)
            if show_result:
                header = title or f'Part {part}'
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


class Day(object):

    def __init__(self, year, day, instructions=None, filename=None):
        self.year = year
        self.day = day
        if not instructions:
            instructions = self.read_input(filename)
        self.instructions = self.parse_instructions(instructions)

    @staticmethod
    def parse_instructions(instructions):
        return instructions

    @staticmethod
    def parse_int_line(instructions):
        return [int(c) for c in instructions[0].split(',')]

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
            if len(row):
                g.append(row)
            else:
                result.append([r for r in g])
                g = []
        if g:
            result.append(g)
        return result

    def read_input(self, filename=None):
        """ If filename is given, use that. Otherwise default to data/<year>/input.<day>.txt """
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
        self.part_1()
        self.part_2()


def stringify(int_list, separator=','):
    return separator.join(str(c) for c in int_list)
