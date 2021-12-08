from python.src.common import Day, timer, Timer


class Display(object):
    """
       AAA
      B   C
      B   C
       DDD
      E   F
      E   F
       GGG
    """

    def __init__(self, digits):
        len_lookup: dict[int, list] = {
            0: [],
            2: [1],
            3: [7],
            4: [4],
            5: [2, 3, 5],
            6: [0, 6, 9],
            7: [8]
        }
        self.digits = dict()
        self.options = dict()
        for d in digits:
            for c in len_lookup[len(d)]:
                self.options[c] = self.options.get(c, list()) + [d]

        self.unscramble_wires()

    def unscramble_wires(self):

        def join_segments(segments):
            return ''.join(sorted(s[ch] for ch in segments))

        s = dict()

        one = set(self.options[1][0])
        four = set(self.options[4][0])
        seven = set(self.options[7][0])
        eight = set(self.options[8][0])

        a = seven - one
        s['A'] = set(a).pop()
        cf = one
        bd = four - one
        eg = eight - four - seven
        for seg in self.options[0]:
            opt = set(seg)
            if opt.union(cf).union(eg) == opt:
                b = (opt - cf - eg - a)
                s['D'] = (bd - b).pop()
                s['B'] = b.pop()
                self.options[9].remove(seg)
                self.options[6].remove(seg)
                break
        for seg in self.options[9]:
            opt = set(seg)
            if opt.union(bd).union(cf) == opt:
                g = opt - bd - cf - a
                s['E'] = (eg - g).pop()
                s['G'] = g.pop()
                self.options[6].remove(seg)
                break
        six = set(self.options[6][0])
        c = eight - six
        s['C'] = set(c).pop()
        s['F'] = (cf - c).pop()

        self.digits = {
            join_segments('ABCEFG'): 0,
            join_segments('CF'): 1,
            join_segments('ACDEG'): 2,
            join_segments('ACDFG'): 3,
            join_segments('BCDF'): 4,
            join_segments('ABDFG'): 5,
            join_segments('ABDEFG'): 6,
            join_segments('ACF'): 7,
            join_segments('ABCDEFG'): 8,
            join_segments('ABCDFG'): 9
        }

    def read_display(self, display):
        output = 0
        for segment in display:
            output *= 10
            cur = self.digits[''.join(sorted(segment))]
            output += cur
        return output


class Dec08(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 8, instructions=instructions, filename=filename)

    @staticmethod
    def parse_instructions(instructions):
        return [
            ((part := line.split('|'))[0].strip().split(' '),
             part[1].strip().split(' '))
            for line in instructions
        ]

    @timer(part=1)
    def part_1(self):
        easy_digits = 0
        for (_, display) in self.instructions:
            easy_digits += sum(len(digit) in (2, 3, 4, 7) for digit in display)
        return easy_digits

    @timer(part=2)
    def part_2(self):
        output = 0
        for digits, display in self.instructions:
            d = Display(digits)
            output += d.read_display(display)
        return output


if __name__ == '__main__':
    with Timer('Seven Segment Search'):
        Dec08().run_day()
