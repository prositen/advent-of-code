import unittest

from python.src.y2018.dec22 import Dec22


class TestDec22(unittest.TestCase):

    def test_part_1(self):
        instructions = [
            "depth: 510\n",
            "target: 10,10\n"
        ]

        d = Dec22(instructions=instructions)
        self.assertEqual(114, d.part_1())

    def test_part_2(self):
        instructions = [
            "depth: 510\n",
            "target: 10,10\n"
        ]

        d = Dec22(instructions=instructions)
        self.assertEqual(45, d.part_2())
