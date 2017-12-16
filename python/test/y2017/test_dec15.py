import unittest

from python.src.y2017 import dec15


class TestDuelGenerators(unittest.TestCase):
    def test_find_first_match(self):
        gen_a = dec15.Generator(factor=16807, start=65)
        gen_b = dec15.Generator(factor=48271, start=8921)
        j = dec15.Judge(gen_a, gen_b)
        j.run(2)
        self.assertEqual(0, j.count)
        j.run(1)
        self.assertEqual(1, j.count)

    def test_find_first_count_modulo(self):
        gen_a = dec15.Generator(factor=16807, start=65, multiplier=4)
        gen_b = dec15.Generator(factor=48271, start=8921, multiplier=8)
        j = dec15.Judge(gen_a, gen_b)
        j.run(1055)
        self.assertEqual(0, j.count)
        j.run(1)
        self.assertEqual(1, j.count)
