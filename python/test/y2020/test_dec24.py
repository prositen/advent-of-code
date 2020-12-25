import unittest

from python.src.y2020.dec24 import Dec24


class TestDec24(unittest.TestCase):

    def test_part_1(self):
        paths = ['esew']
        d = Dec24(instructions=paths)
        self.assertEqual(1, d.part_1())
        self.assertTrue(d.grid.at((0.5, 0.5)))

    paths = [
        "sesenwnenenewseeswwswswwnenewsewsw",
        "neeenesenwnwwswnenewnwwsewnenwseswesw",
        "seswneswswsenwwnwse",
        "nwnwneseeswswnenewneswwnewseswneseene",
        "swweswneswnenwsewnwneneseenw",
        "eesenwseswswnenwswnwnwsewwnwsene",
        "sewnenenenesenwsewnenwwwse",
        "wenwwweseeeweswwwnwwe",
        "wsweesenenewnwwnwsenewsenwwsesesenwne",
        "neeswseenwwswnwswswnw",
        "nenwswwsewswnenenewsenwsenwnesesenew",
        "enewnwewneswsewnwswenweswnenwsenwsw",
        "sweneswneswneneenwnewenewwneswswnese",
        "swwesenesewenwneswnwwneseswwne",
        "enesenwswwswneneswsenwnewswseenwsese",
        "wnwnesenesenenwwnenwsewesewsesesew",
        "nenewswnwewswnenesenwnesewesw",
        "eneswnwswnwsenenwnwnwwseeswneewsenese",
        "neswnwewnwnwseenwseesewsenwsweewe",
        "wseweeenwnesenwwwswnew"]

    def test_part_1_longer(self):
        self.assertEqual(10, Dec24(instructions=self.paths).part_1())

    def test_part_2(self):
        self.assertEqual(2208, Dec24(instructions=self.paths).part_2())
