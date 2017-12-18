import unittest
from python.src.y2017 import dec18


class TestDuet(unittest.TestCase):
    def test_part_1(self):
        puzzle_input = [
            "set a 1",
            "add a 2",
            "mul a a",
            "mod a 5",
            "snd a",
            "set a 0",
            "rcv a",
            "jgz a -1",
            "set a 1",
            "jgz a -2"]
        d = dec18.Duet(puzzle_input)
        d.run()
        self.assertEqual(4, d.recovered)
        self.assertDictEqual({'a': 1}, d.registers)

    def test_part_2(self):
        puzzle_input = [
            "snd 1",
            "snd 2",
            "snd p",
            "rcv a",
            "rcv b",
            "rcv c",
            "rcv d"
        ]
        c = dec18.Coordinator(puzzle_input)
        c.run()
        self.assertEqual(3, c.result())
        self.assertDictEqual({'p': 0, 'a': 1, 'b': 2, 'c': 1}, c.d1.registers)
        self.assertDictEqual({'p': 1, 'a': 1, 'b': 2, 'c': 0}, c.d2.registers)
