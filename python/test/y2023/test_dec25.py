import unittest

from python.src.y2023.dec25 import Dec25


class TestDec25(unittest.TestCase):
    data = [
        "jqt: rhn xhk nvd",
        "rsh: frs pzl lsr",
        "xhk: hfx",
        "cmg: qnr nvd lhk bvb",
        "rhn: xhk bvb hfx",
        "bvb: xhk hfx",
        "pzl: lsr hfx nvd",
        "qnr: nvd",
        "ntq: jqt hfx bvb xhk",
        "nvd: lhk",
        "lsr: lhk",
        "rzs: qnr cmg lsr rsh",
        "frs: qnr lhk lsr"
    ]

    def test_part_1(self):
        self.assertEqual(54, Dec25(instructions=self.data).part_1())


if __name__ == '__main__':
    unittest.main()
