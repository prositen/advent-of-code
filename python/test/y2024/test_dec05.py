import unittest

from python.src.y2024.dec05 import Dec05


class TestDec05(unittest.TestCase):
    data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".split("\n")

    def test_part_1(self):
        """
        Valid:
        75,47,61,53,29
        97,61,53,29,13
        75,29,13
        """
        self.assertEqual(143, Dec05(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(123, Dec05(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
