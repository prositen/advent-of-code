import unittest

from python.src.y2017 import dec25


class TestTuring(unittest.TestCase):
    def test_count_ones(self):
        puzzle_input = ["Begin in state A.",
                        "Perform a diagnostic checksum after 6 steps.",
                        "",
                        "In state A:",
                        "  If the current value is 0:",
                        "    - Write the value 1.",
                        "    - Move one slot to the right.",
                        "    - Continue with state B.",
                        "  If the current value is 1:",
                        "    - Write the value 0.",
                        "    - Move one slot to the left.",
                        "    - Continue with state B.",
                        "",
                        "In state B:",
                        "  If the current value is 0:",
                        "    - Write the value 1.",
                        "    - Move one slot to the left.",
                        "    - Continue with state A.",
                        "  If the current value is 1:",
                        "    - Write the value 1.",
                        "    - Move one slot to the right.",
                        "    - Continue with state A."]
        puzzle_input = [line[:-1] for line in puzzle_input]
        s_m = dec25.StateMachine(puzzle_input)
        s_m.run()
        self.assertEquals(3, s_m.part1())
