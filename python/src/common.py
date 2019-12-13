import os


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

    def read_input(self, filename=None):
        """ If filename is given, use that. Otherwise default to data/<year>/input.<day>.txt """
        if filename is None:
            filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..',
                                    'data', str(self.year), 'input.{}.txt'.format(self.day))
        with open(filename) as fh:
            return fh.readlines()
