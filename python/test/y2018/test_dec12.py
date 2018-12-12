import unittest

from python.src.y2018.dec12 import Dec12


class TestDec12(unittest.TestCase):

    def test_part_1(self):
        instructions = [
            "initial state: #..#.#..##......###...###\n",
            "\n",
            "...## => #\n",
            "..#.. => #\n",
            ".#... => #\n",
            ".#.#. => #\n",
            ".#.## => #\n",
            ".##.. => #\n",
            ".#### => #\n",
            "#.#.# => #\n",
            "#.### => #\n",
            "##.#. => #\n",
            "##.## => #\n",
            "###.. => #\n",
            "###.# => #\n",
            "####. => #\n"
        ]

        d = Dec12(instructions)
        self.assertEqual(325, d.part_1())
