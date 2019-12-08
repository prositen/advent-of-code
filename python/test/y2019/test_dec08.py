import unittest

from python.src.y2019 import dec08


class TestDec08(unittest.TestCase):
    def test_create_image(self):
        pixels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]

        image = dec08.Image(width=3, height=2, pixels=pixels)
        self.assertEqual(2, image.no_layers)
        self.assertEqual([1, 2, 3, 4, 5, 6], image.layers[0])

    def test_render_image(self):
        pixels = [0, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 2, 0, 0, 0, 0]
        image = dec08.Image(width=2, height=2, pixels=pixels)
        self.assertEqual([0, 1, 1, 0], image.render())


if __name__ == '__main__':
    unittest.main()
