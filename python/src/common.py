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
                print(f'{header}: {result}  {(time.time() - start_time) * 1e3:.2f} ms')
            return result

        return wrapper

    return decorator


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

    def read_input(self, filename=None):
        """ If filename is given, use that. Otherwise default to data/<year>/input.<day>.txt """
        if filename is None:
            filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..',
                                    'data', str(self.year), 'input.{}.txt'.format(self.day))
        with open(filename) as fh:
            return fh.readlines()
