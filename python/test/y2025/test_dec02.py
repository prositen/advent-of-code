import unittest

from python.src.y2025.dec02 import Dec02, GiftShopDatabase


class TestDec02(unittest.TestCase):
    data = ["11-22,95-115,998-1012,1188511880-1188511890,"
            "222220-222224,1698522-1698528,446443-446449,"
            "38593856-38593862,565653-565659,824824821-824824827,"
            "2121212118-2121212124"]

    def test_part_1(self):
        self.assertEqual(1227775554, Dec02(instructions=self.data).part_1())

    def test_part_1_mini(self):
        gs = GiftShopDatabase([('2', '18')])
        self.assertEqual(11, gs.identify_repeated_twice())

    def test_part_2(self):
        self.assertEqual(4174379265, Dec02(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
