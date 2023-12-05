import unittest

from python.src.y2023.dec05 import Dec05, SeedAlmanac


class TestDec05(unittest.TestCase):
    data = [
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "",
        "fertilizer-to-water map:",
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4",
        "",
        "water-to-light map:",
        "88 18 7",
        "18 25 70",
        "",
        "light-to-temperature map:",
        "45 77 23",
        "81 45 19",
        "68 64 13",
        "",
        "temperature-to-humidity map:",
        "0 69 1",
        "1 0 69",
        "",
        "humidity-to-location map:",
        "60 56 37",
        "56 93 4"
    ]

    def test_lookup_seed(self):
        day = Dec05(instructions=self.data)
        almanac = SeedAlmanac(*day.instructions)
        cases = [
            (79, 81),
            (14, 14),
            (55, 57),
            (13, 13)
        ]
        for seed, soil in cases:
            self.assertEqual(soil, almanac.lookup_in(seed, almanac.seed_to_soil))

    def test_part_1(self):
        self.assertEqual(35, Dec05(instructions=self.data).part_1())

    def test_part_2(self):
        self.assertEqual(46, Dec05(instructions=self.data).part_2())


if __name__ == '__main__':
    unittest.main()
