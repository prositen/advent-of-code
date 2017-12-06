import unittest
from python.src.y2017 import dec06


class TestDec06(unittest.TestCase):

    def setUp(self):
        self.puzzle_input = "0 2 7 0"

    def test_memory_reallocation(self):
        memory = dec06.Memory(self.puzzle_input)
        self.assertEqual(5, memory.steps_until_loop())

    def test_loop_size(self):
        memory = dec06.Memory(self.puzzle_input)
        memory.steps_until_loop()
        self.assertEqual(4, memory.loop_size())
