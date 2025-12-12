import unittest

from python.src.y2025.dec12 import Dec12


class TestDec12(unittest.TestCase):
    data = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2""".splitlines()

    def test_part_1(self):
        self.assertEqual(2, Dec12(instructions=self.data).part_1())



if __name__ == '__main__':
    unittest.main()
