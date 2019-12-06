import unittest

from python.src.y2019 import dec06


class TestDec06(unittest.TestCase):

    def atest_total_number_of_orbits(self):
        orbits = ['COM)B',
                  'B)C',
                  'C)D',
                  'D)E',
                  'E)F',
                  'B)G',
                  'G)H',
                  'D)I',
                  'E)J',
                  'J)K',
                  'K)L']

        self.assertEqual(42, dec06.Dec06(instructions=orbits).part_1())

    def test_orbits_between_you_and_san(self):
        orbits = ['COM)B',
                  'B)C',
                  'C)D',
                  'D)E',
                  'E)F',
                  'B)G',
                  'G)H',
                  'D)I',
                  'E)J',
                  'J)K',
                  'K)L',
                  'K)YOU',
                  'I)SAN']
        self.assertEqual(4, dec06.Dec06(instructions=orbits).part_2())
