import unittest

from python.src.y2018.dec19 import Dec19


class TestDec19(unittest.TestCase):

    def test_device(self):
        program = [
            "#ip 0",
            "seti 5 0 1",
            "seti 6 0 2",
            "addi 0 1 0",
            "addr 1 2 3",
            "setr 1 0 0",
            "seti 8 0 4",
            "seti 9 0 5"
        ]

        d = Dec19(instructions=program)
        d.device.run(d.program)
        self.assertListEqual([7, 5, 6, 0, 0, 9],
                             d.device.reg)
