import unittest

from python.src.y2023.dec12 import Dec12


class TestDec12(unittest.TestCase):
    data = [
        "???.### 1,1,3",
        ".??..??...?##. 1,1,3",
        "?#?#?#?#?#?#?#? 1,3,1,6",
        "????.#...#... 4,1,1",
        "????.######..#####. 1,6,5",
        "?###???????? 3,2,1"
    ]

    def test_part_1(self):
        self.assertEqual(21, Dec12(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(525152, Dec12(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
