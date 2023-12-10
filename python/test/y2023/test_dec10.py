import unittest

from python.src.y2023.dec10 import Dec10


class TestDec10(unittest.TestCase):
    def test_part_1(self):
        data = [
            "-L|F7",
            "7S-7|",
            "L|7||",
            "-L-J|",
            "L|-JF"
        ]

        self.assertEqual(4, Dec10(instructions=data).part_1())

    # def test_part_2(self):
    #    self.assertEqual(2, Dec10(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
