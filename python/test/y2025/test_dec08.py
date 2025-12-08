import unittest

from python.src.y2025.dec08 import Dec08
from src.y2025.dec08 import Decoration


class TestDec08(unittest.TestCase):
    data = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689""".splitlines()

    def test_part_1(self):
        boxes = Dec08.parse_instructions(instructions=self.data)
        d = Decoration(boxes)

        self.assertEqual(40, d.largest_circuits(connections=10))

    def test_part_2(self):
        self.assertEqual(0, Dec08(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
