import unittest

from python.src.y2020.dec09 import Dec09


class TestDec09(unittest.TestCase):
    instructions = [
        "35",
        "20",
        "15",
        "25",
        "47",
        "40",
        "62",
        "55",
        "65",
        "95",
        "102",
        "117",
        "150",
        "182",
        "127",
        "219",
        "299",
        "277",
        "309",
        "576"
    ]

    def test_find_invalid_number(self):
        self.assertEqual(127, Dec09(instructions=self.instructions).find_invalid_number(preamble=5))

    def test_find_weakness(self):
        self.assertEqual((15, 47),
                         Dec09(instructions=self.instructions).find_encryption_weakness(127))
