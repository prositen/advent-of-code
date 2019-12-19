import unittest

from python.src.y2019.dec18 import Dec18


class TestDec18(unittest.TestCase):
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

    def test_part_2_a(self):
        maze = ["#######",
                "#a.#Cd#",
                "##...##",
                "##.@.##",
                "##...##",
                "#cB#Ab#",
                "#######"]
        self.assertEqual(8, Dec18(instructions=maze).part_2())

    def test_part_2_b(self):
        maze = ["###############",
                "#d.ABC.#.....a#",
                "######...######",
                "######.@.######",
                "######...######",
                "#b.....#.....c#",
                "###############"]
        self.assertEqual(24, Dec18(instructions=maze).part_2())

    def test_part_2_c(self):
        maze = ["#############",
                "#DcBa.#.GhKl#",
                "#.###...#I###",
                "#e#d#.@.#j#k#",
                "###C#...###J#",
                "#fEbA.#.FgHi#",
                "#############"]
        self.assertEqual(32, Dec18(instructions=maze).part_2())

    def test_part_2_d(self):
        maze = ["#############",
                "#g#f.D#..h#l#",
                "#F###e#E###.#",
                "#dCba...BcIJ#",
                "#####.@.#####",
                "#nK.L...G...#",
                "#M###N#H###.#",
                "#o#m..#i#jk.#",
                "#############"]
        self.assertEqual(72, Dec18(instructions=maze).part_2())

if __name__ == '__main__':
    unittest.main()
