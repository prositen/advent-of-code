import unittest

from python.src.y2023.dec20 import Dec20


class TestDec20(unittest.TestCase):
    example_1 = [
        "broadcaster -> a, b, c",
        "%a -> b",
        "%b -> c",
        "%c -> inv",
        "&inv -> a"
    ]

    example_2 = [
        "broadcaster -> a",
        "%a -> inv, con",
        "&inv -> b",
        "%b -> con",
        "&con -> output"
    ]

    def test_part_1(self):
        self.assertEqual(32000000,
                         Dec20(instructions=self.example_1).part_1())
        self.assertEqual(11687500,
                         Dec20(instructions=self.example_2).part_1())


if __name__ == '__main__':
    unittest.main()
