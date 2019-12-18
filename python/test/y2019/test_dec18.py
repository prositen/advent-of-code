import unittest

from python.src.y2019.dec18 import Dec18


class TestDec16(unittest.TestCase):
    def test_part_1_a(self):
        maze = ["#########",
                "#b.A.@.a#",
                "#########"]
        self.assertEqual(8, Dec18(instructions=maze).part_1())

    def test_part_1_b(self):
        maze = ["########################",
                "#f.D.E.e.C.b.A.@.a.B.c.#",
                "######################.#",
                "#d.....................#",
                "########################"]
        self.assertEqual(86, Dec18(instructions=maze).part_1())

    def test_part_1_c(self):
        maze = ["########################",
                "#...............b.C.D.f#",
                "#.######################",
                "#.....@.a.B.c.d.A.e.F.g#",
                "########################"]
        self.assertEqual(132, Dec18(instructions=maze).part_1())

    def test_part_1_d(self):
        maze = ["#################",
                "#i.G..c...e..H.p#",
                "########.########",
                "#j.A..b...f..D.o#",
                "########@########",
                "#k.E..a...g..B.n#",
                "########.########",
                "#l.F..d...h..C.m#",
                "#################"]
        self.assertEqual(136, Dec18(instructions=maze).part_1())

    def test_part_1_e(self):
        maze = ["########################",
                "#@..............ac.GI.b#",
                "###d#e#f################",
                "###A#B#C################",
                "###g#h#i################",
                "########################"]
        self.assertEqual(81, Dec18(instructions=maze).part_1())


if __name__ == '__main__':
    unittest.main()
