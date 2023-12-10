import unittest

from python.src.y2023.dec10 import Dec10


class TestDec10(unittest.TestCase):
    def test_part_1(self):
        data = [
            "-L|F7",
            "7S-7|",
            "L|7||",
            "-L-J|",
            "L|-JF"
        ]

        self.assertEqual(4, Dec10(instructions=data).part_1())

    def test_part_2(self):
        cases = (
            ([
                 "...........",
                 ".S-------7.",
                 ".|F-----7|.",
                 ".||.....||.",
                 ".||.....||.",
                 ".|L-7.F-J|.",
                 ".|..|.|..|.",
                 ".L--J.L--J.",
                 "..........."
             ], 4),
            ([
                 "..........",
                 ".S------7.",
                 ".|F----7|.",
                 ".||OOOO||.",
                 ".||OOOO||.",
                 ".|L-7F-J|.",
                 ".|II||II|.",
                 ".L--JL--J.",
                 ".........."
             ], 4),
            (
                [
                    ".F----7F7F7F7F-7....",
                    ".|F--7||||||||FJ....",
                    ".||.FJ||||||||L7....",
                    "FJL7L7LJLJ||LJ.L-7..",
                    "L--J.L7...LJS7F-7L7.",
                    "....F-J..F7FJ|L7L7L7",
                    "....L7.F7||L7|.L7L7|",
                    ".....|FJLJ|FJ|F7|.LJ",
                    "....FJL-7.||.||||...",
                    "....L---J.LJ.LJLJ..."
                ],
                8),
            (
                [
                    "FF7FSF7F7F7F7F7F---7",
                    "L|LJ||||||||||||F--J",
                    "FL-7LJLJ||||||LJL-77",
                    "F--JF--7||LJLJ7F7FJ-",
                    "L---JF-JLJ.||-FJLJJ7",
                    "|F|F-JF---7F7-L7L|7|",
                    "|FFJF7L7F-JF7|JL---7",
                    "7-L-JL7||F7|L7F-7F7|",
                    "L.L7LFJ|||||FJL7||LJ",
                    "L7JLJL-JLJLJL--JLJ.L"
                ],
                10)
        )
        for grid, contained in cases:
            self.assertEqual(contained, Dec10(instructions=grid).part_2())


if __name__ == '__main__':
    unittest.main()
