import unittest
from python.src.y2017 import dec03


class TestDec03(unittest.TestCase):
    def test_spiral_steps_without_filling(self):
        sm = dec03.SpiralMemoryAlgoritm()
        self.assertEqual(0, sm.spiral_steps(1))
        self.assertEqual(3, sm.spiral_steps(12))
        self.assertEqual(2, sm.spiral_steps(23))
        self.assertEqual(31, sm.spiral_steps(1024))

    def test_spiral_steps(self):
        sm = dec03.SpiralMemory()
        self.assertEqual(3, sm.spiral_steps(12))
        self.assertEqual(2, sm.spiral_steps(23))
        self.assertEqual(31, sm.spiral_steps(1024))

    def test_stress(self):
        sm = dec03.SpiralMemory()
        sm.stress_test(23)
        self.assertEqual(4, sm.cell(0, 1))
        self.assertEqual(147, sm.cell(-2, 2))
