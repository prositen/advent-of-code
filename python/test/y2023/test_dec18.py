import unittest

from python.src.y2023.dec18 import Dec18


class TestDec18(unittest.TestCase):
    data = [
        "R 6 (#70c710)",
        "D 5 (#0dc571)",
        "L 2 (#5713f0)",
        "D 2 (#d2c081)",
        "R 2 (#59c680)",
        "D 2 (#411b91)",
        "L 5 (#8ceee2)",
        "U 2 (#caa173)",
        "L 1 (#1b58a2)",
        "U 2 (#caa171)",
        "R 2 (#7807d2)",
        "U 3 (#a77fa3)",
        "L 2 (#015232)",
        "U 2 (#7a21e3)"
    ]

    def test_part_1(self):
        self.assertEqual(62, Dec18(instructions=self.data).part_1())

    #def test_part_2(self):
    #    self.assertEqual(952408144115, Dec18(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
