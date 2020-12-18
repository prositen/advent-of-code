import unittest

from python.src.y2020.dec18 import Dec18


class TestDec18(unittest.TestCase):

    def test_part_1_a(self):
        """
        1 + 2
              * 3
                  + 4
                      * 5
                         + 6
        """
        expressions = ["1 + 2 * 3 + 4 * 5 + 6"]
        self.assertEqual(71, Dec18(instructions=expressions).part_1())

    def test_part_1_b(self):
        """
        1
          + (2 * 3)
             + (4
                 * (5 + 6) )

        """

        expressions = ["1 + (2 * 3) + (4 * (5 + 6))"]
        self.assertEqual(51, Dec18(instructions=expressions).part_1())

    def test_part_1_c(self):
        expressions = ["2 * 3 + (4 * 5)"]
        self.assertEqual(26, Dec18(instructions=expressions).part_1())

    def test_part_1_d(self):
        expressions = ["5 + (8 * 3 + 9 + 3 * 4 * 3)"]
        self.assertEqual(437, Dec18(instructions=expressions).part_1())

    def test_part_1_e(self):
        expressions = ["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"]
        self.assertEqual(12240, Dec18(instructions=expressions).part_1())

    def test_part_1_f(self):
        expressions = ["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]
        self.assertEqual(13632, Dec18(instructions=expressions).part_1())
    """
    def test_part_2_a(self):
        expressions = ["1 + 2 * 3 + 4 * 5 + 6"]
        self.assertEqual(231, Dec18(instructions=expressions).part_1())

    def test_part_2_b(self):
        expressions = ["1 + (2 * 3) + (4 * (5 + 6))"]
        self.assertEqual(51, Dec18(instructions=expressions).part_1())

    def test_part_2_c(self):
        expressions = ["2 * 3 + (4 * 5)"]
        self.assertEqual(46, Dec18(instructions=expressions).part_1())

    def test_part_2_d(self):
        expressions = ["5 + (8 * 3 + 9 + 3 * 4 * 3)"]
        self.assertEqual(1445, Dec18(instructions=expressions).part_1())

    def test_part_2_e(self):
        expressions = ["5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"]
        self.assertEqual(669060, Dec18(instructions=expressions).part_1())

    def test_part_2_f(self):
        expressions = ["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]
        self.assertEqual(23340, Dec18(instructions=expressions).part_1())
        
    """