import unittest

from python.src.y2020.dec13 import Dec13


class TestDec13(unittest.TestCase):
    instructions = [
        "939",
        "7,13,x,x,59,x,31,19"
    ]

    def test_part_1(self):
        self.assertEqual(295, Dec13(instructions=self.instructions).part_1())

    def test_part_2(self):
        self.assertEqual(1068781, Dec13(instructions=self.instructions).part_2())

    def test_part_2_more_examples(self):
        cases = [
            (3417, "17,x,13,19"),
            (754018, "67,7,59,61"),
            (779210, "67,x,7,59,61"),
            (1261476, "67,7,x,59,61"),
            (1202161486, "1789,37,47,1889")
        ]
        for expected_response, constraints in cases:
            self.assertEqual(expected_response,
                             Dec13(instructions=["0", constraints]).part_2())
