import unittest

from python.src.y2017 import dec22


class TestVirus(unittest.TestCase):
    def test_virus(self):
        puzzle_input = ['..#', '#..', '...']
        v = dec22.Virus(puzzle_input)
        v.step(7)
        self.assertEqual(5, v.infect)
        v.step(63)
        self.assertEqual(41, v.infect)
        v.step(9930)
        self.assertEqual(5587, v.infect)

    def test_evolved_virus(self):
        puzzle_input = ['..#', '#..', '...']
        v = dec22.EvolvedVirus(puzzle_input)
        v.step(100)
        self.assertEqual(26, v.infect)
