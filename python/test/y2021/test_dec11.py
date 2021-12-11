import unittest

from python.src.y2021.dec11 import Dec11


class TestDec11(unittest.TestCase):

    data = [
        "5483143223",
        "2745854711",
        "5264556173",
        "6141336146",
        "6357385478",
        "4167524645",
        "2176841721",
        "6882881134",
        "4846848554",
        "5283751526"
    ]

    def test_number_of_flashes(self):
        self.assertEqual(1656, Dec11(instructions=self.data).part_1())

    def test_syncronize_at(self):
        self.assertEqual(195, Dec11(instructions=self.data).part_2())
