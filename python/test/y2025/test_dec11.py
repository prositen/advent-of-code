import unittest

from python.src.y2025.dec11 import Dec11


class TestDec11(unittest.TestCase):
    data = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out""".splitlines()

    def test_part_1(self):
        self.assertEqual(5, Dec11(instructions=self.data).part_1())

    def test_part_2(self):
        new_data = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out""".splitlines()
        self.assertEqual(2, Dec11(instructions=new_data).part_2())


if __name__ == '__main__':
    unittest.main()
