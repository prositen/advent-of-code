import unittest

from python.src.y2023.dec17 import Dec17


class TestDec17(unittest.TestCase):
    data = [
        "2413432311323",
        "3215453535623",
        "3255245654254",
        "3446585845452",
        "4546657867536",
        "1438598798454",
        "4457876987766",
        "3637877979653",
        "4654967986887",
        "4564679986453",
        "1224686865563",
        "2546548887735",
        "4322674655533"
    ]

    def test_part_1(self):
        self.assertEqual(102, Dec17(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(94, Dec17(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
