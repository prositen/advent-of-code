import unittest

from python.src.y2017 import dec08


class TestDecc08(unittest.TestCase):

    def setUp(self):
        puzzle_input = ["b inc 5 if a > 1",
                        "a inc 1 if b < 5",
                        "c dec -10 if a >= 1",
                        "c inc -20 if c == 10"]
        self.context = dec08.Context(puzzle_input)

    def test_max_value(self):
        self.context.pp()
        self.context.run()
        self.assertEqual(1, self.context.max())

        self.assertEqual(10, self.context.all_time_max)
