import unittest

from python.src.y2022.dec06 import Dec06


class TestDec06(unittest.TestCase):
    data = [
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7, 19),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5, 23),
        ('nppdvjthqldpwncqszvftbrmjlhg', 6, 23),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10, 29),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11, 26)
    ]

    def test_find_start_of_packet(self):
        for message, part1, _ in self.data:
            self.assertEqual(part1, Dec06(instructions=[message]).part_1())

    def test_find_start_of_message(self):
        for message, _, part2 in self.data:
            self.assertEqual(part2, Dec06(instructions=[message]).part_2())
