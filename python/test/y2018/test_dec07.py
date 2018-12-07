import unittest

from python.src.y2018.dec07 import Dec07


class TestDec07(unittest.TestCase):

    def setUp(self):
        instructions = [
            'Step C must be finished before step A can begin.',
            'Step C must be finished before step F can begin.',
            'Step A must be finished before step B can begin.',
            'Step A must be finished before step D can begin.',
            'Step B must be finished before step E can begin.',
            'Step D must be finished before step E can begin.',
            "Step F must be finished before step E can begin."
        ]
        self.day = Dec07(instructions)

    def test_parse_instructions(self):
        self.assertEqual([
            ('C', 'A'),
            ('C', 'F'),
            ('A', 'B'),
            ('A', 'D'),
            ('B', 'E'),
            ('D', 'E'),
            ('F', 'E')],
            self.day.instructions)

    def test_part_1(self):
        self.assertEqual('CABDFE', self.day.part_1())

    def test_part_2(self):
        self.assertEqual(15,
                         self.day.part_2(elves=2, delay=0))
