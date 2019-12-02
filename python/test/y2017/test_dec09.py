import unittest

from python.src.y2017 import dec09


class TestStreamProcessing(unittest.TestCase):

    def test_group_score(self):
        test_cases = [
            ("{}", 1),
            ("{{{}}}", 6),
            ("{{{},{},{{}}}}", 16),
            ("{<a>,<a>,<a>,<a>}", 1),
            ("{{<ab>},{<ab>},{<ab>},{<ab>}}", 9),
            ("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9),
            ("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3)
        ]
        for stream, expected in test_cases:
            tree = dec09.build_tree(stream)
            self.assertEqual(expected, tree.sum_tree()[0])

    def test_garbage_count(self):
        test_cases = [
            ("<>", 0),
            ("<random characters>", 17),
            ("<<<<>", 3),
            ("<{!>}>", 2),
            ("<!!>", 0),
            ("<!!!>>", 0),
            ('<{o"i!a,<[i<a>', 10)
        ]
        for stream, expected in test_cases:
            tree = dec09.build_tree(stream)
            self.assertEqual(expected, tree.sum_tree()[1])
