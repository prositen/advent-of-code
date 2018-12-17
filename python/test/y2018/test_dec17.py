import unittest

from python.src.y2018.dec17 import Dec17


class TestDec17(unittest.TestCase):

    def test_part_1(self):
        scan = [
            "x=495, y=2..7",
            "y=7, x=495..501",
            "x=501, y=3..7",
            "x=498, y=2..4",
            "x=506, y=1..2",
            "x=498, y=10..13",
            "x=504, y=10..13",
            "y=13, x=498..504"
        ]

        d = Dec17(instructions=scan)
        d.render_veins()
        self.assertEqual(57, d.part_1())