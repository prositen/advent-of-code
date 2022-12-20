import unittest

from python.src.y2022.dec19 import Dec19


class TestDec19(unittest.TestCase):
    data = [
        """Blueprint 1:
  Each ore robot costs 4 ore.
  Each clay robot costs 2 ore.
  Each obsidian robot costs 3 ore and 14 clay.
  Each geode robot costs 2 ore and 7 obsidian.""".replace('\n', ''),
        """Blueprint 2:
  Each ore robot costs 2 ore.
  Each clay robot costs 3 ore.
  Each obsidian robot costs 3 ore and 8 clay.
  Each geode robot costs 3 ore and 12 obsidian.""".replace('\n', '')
    ]

    def test_part_1(self):
        self.assertEqual(33, Dec19(instructions=self.data).part_1())
