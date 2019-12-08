from python.src.common import Day


class Image(object):

    def __init__(self, width, height, pixels):
        self.no_layers = len(pixels) // (width * height)
        self.width = width
        self.height = height
        self.h_w = self.width * self.height
        self.layers = list()
        for start in range(0, len(pixels), self.h_w):
            self.layers.append(pixels[start:start + self.h_w])

    def render(self):
        result = [p for p in self.layers[self.no_layers - 1]]
        for l_no in range(self.no_layers - 1, -1, -1):
            for i in range(self.h_w):
                pixel = self.layers[l_no][i]
                if pixel < 2:
                    result[i] = pixel
        return result


class Dec08(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2019, 8, instructions, filename)
        self.image = Image(width=25, height=6, pixels=self.instructions)

    @staticmethod
    def parse_instructions(instructions):
        return [
            int(c) for c in instructions[0]
        ]

    def part_1(self):
        min_zeroes = self.image.h_w
        min_layer = None
        for i in range(self.image.no_layers):
            l = self.image.layers[i]
            zeroes = l.count(0)
            if zeroes < min_zeroes:
                min_zeroes = zeroes
                min_layer = i
        return self.image.layers[min_layer].count(1) * self.image.layers[min_layer].count(2)

    def part_2(self):
        image = self.image.render()
        image = ''.join('x' if c is 1 else ' ' for c in image)
        for start in range(0, len(image), self.image.width):
            print(image[start:start + self.image.width])


if __name__ == '__main__':
    d = Dec08()
    print("Part 1: ", d.part_1())
    print("Part 2")
    d.part_2()
