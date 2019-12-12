import unittest

from python.src.y2019 import dec12


class TestDec12(unittest.TestCase):
    def test_part_1_a(self):
        positions = ["<x=-1, y=0, z=2>",
                     "<x=2, y=-10, z=-7>",
                     "<x=4, y=-8, z=8>",
                     "<x=3, y=5, z=-1>"]
        d = dec12.Dec12(instructions=positions)
        d.simulate(steps=10)
        self.assertEqual(179, d.get_energy())

    def test_part_2(self):
        positions = ["<x=-1, y=0, z=2>",
                     "<x=2, y=-10, z=-7>",
                     "<x=4, y=-8, z=8>",
                     "<x=3, y=5, z=-1>"]
        d = dec12.Dec12(instructions=positions)
        self.assertEqual(2772, d.part_2())

    def test_part_2_large(self):
        positions = ["<x=-8, y=-10, z=0>",
                     "<x=5, y=5, z=10>",
                     "<x=2, y=-7, z=3>",
                     "<x=9, y=-8, z=-3>"]
        d = dec12.Dec12(instructions=positions)
        self.assertEqual(4686774924, d.part_2())


if __name__ == '__main__':
    unittest.main()
