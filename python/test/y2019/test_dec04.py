import unittest

from python.src.y2019 import dec04


class TestDec03(unittest.TestCase):
    def test_valid_passwords(self):
        cases = [
            ('111111', True),
            ('223450', False),
            ('123789', False)
        ]

        for case in cases:
            self.assertEqual(case[1], dec04.is_valid_password(case[0]))

    def test_valid_passwords_part_2(self):
        cases = [
            ('112233', True),
            ('123444', False),
            ('111122', True)
        ]

        for case in cases:
            self.assertEqual(case[1], dec04.is_valid_password(case[0], max_repeated=2))
