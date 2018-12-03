import unittest

from python.src.y2018 import dec03


class TestDec03(unittest.TestCase):

    def setUp(self):
        claims = [
            "#1 @ 1,3: 4x4",
            "#2 @ 3,1: 4x4",
            "#3 @ 5,5: 2x2"
        ]
        self.fabric = dec03.Fabric(claims)

    def test_overlapping_squares(self):
        self.assertEqual(4, self.fabric.overlapping_squares())

    def test_no_overlaps(self):
        self.assertEqual(3, self.fabric.no_overlaps())


class PrintFabric(dec03.Fabric):
    def print(self):
        """ Visualize the fabric with all the claims.

        Each square inch is marked with either:
            - the claim ID, if only one claim,
            - x if more than one claim
            - *claim_id* if this is the one non-overlapping claim.
        """
        id_width = len(str(max([c.id for c in self.claims]))) + 3
        n_o = self.no_overlaps()
        for y in range(1000):
            line = []
            for x in range(1000):
                claims = self.fabric.get((y, x))
                if not claims:
                    marker = '.'
                elif len(claims) == 1:
                    marker = next(iter(claims))
                    if marker == n_o:
                        marker = '*{}*'.format(marker)
                else:
                    marker = 'x'
                line.append('{marker:>{width}}'.format(marker=marker, width=id_width))
            print(''.join(line))
