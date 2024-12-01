import unittest

from python.src.y2022.dec25 import Dec25


class TestDec25(unittest.TestCase):
    data = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122""".split('\n')

    snafu = [
        (1, '1'),
        (2, '2'),
        (3, '1='),
        (4, '1-'),
        (5, '10'),
        (6, '11'),
        (7, '12'),
        (8, '2='),
        (9, '2-'),
        (10, '20'),
        (15, '1=0'),
        (20, '1-0'),
        (2022, '1=11-2'),
        (12345, '1-0---0'),
        (314159265, '1121-1110-1=0')
    ]

    def test_convert_from_snafu(self):
        for expected, snafu in self.snafu:
            self.assertEqual(expected, Dec25.convert_from_snafu(snafu))

    def test_convert_to_snafu(self):
        for snafu, expected in self.snafu:
            self.assertEqual(expected, Dec25.convert_to_snafu(snafu))

    def test_part_1(self):
        self.assertEqual('2=-1=0', Dec25(instructions=self.data).part_1())
