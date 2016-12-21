import re


class Scrambler(object):
    re_SWAP_POSITION = re.compile(r'swap position (\d+) with position (\d+)')
    re_SWAP_LETTER = re.compile(r'swap letter (\w) with letter (\w)')
    re_ROTATE_LEFT = re.compile(r'rotate left (\d+) steps?')
    re_ROTATE_RIGHT = re.compile(r'rotate right (\d+) steps?')
    re_ROTATE_POSITION = re.compile(r'rotate based on position of letter (\w)')
    re_REVERSE = re.compile(r'reverse positions (\d+) through (\d+)')
    re_MOVE = re.compile(r'move position (\d+) to position (\d+)')

    def __init__(self, instructions):
        self.command_lookup = {
            self.re_SWAP_POSITION: self.swap_position,
            self.re_SWAP_LETTER: self.swap_letter,
            self.re_ROTATE_LEFT: self.rotate_left,
            self.re_ROTATE_RIGHT: self.rotate_right,
            self.re_ROTATE_POSITION: self.rotate_position,
            self.re_REVERSE: self.reverse,
            self.re_MOVE: self.move
        }
        self.instructions = [self.parse(instruction) for instruction in instructions]

    def run(self, password):
        for instruction, param in self.instructions:
            password = instruction(password, param)
        return password

    @staticmethod
    def swap_position(password, params):
        """ swap position X with position Y
        means that the letters at indexes X and Y (counting from 0) should be swapped. """
        pos_x = min(int(params[0]), int(params[1]))
        pos_y = max(int(params[0]), int(params[1]))
        return password[:pos_x] + password[pos_y] + password[pos_x + 1:pos_y] + password[pos_x] + password[pos_y + 1:]

    @staticmethod
    def swap_letter(password, params):
        """ swap letter X with letter Y
        means that the letters X and Y should be swapped (regardless of where they appear in the string)."""
        letter_x = params[0]
        letter_y = params[1]
        tr_table = str.maketrans("{}{}".format(letter_x, letter_y), "{}{}".format(letter_y, letter_x))
        return password.translate(tr_table)

    @staticmethod
    def rotate_left(password, params):
        """ rotate left X steps
        means that the whole string should be rotated; for example, one left rotation would turn dabc into abcd. """
        l = len(password)
        steps = int(params[0]) % l
        return password[steps:] + password[:steps]

    @staticmethod
    def rotate_right(password, params):
        """ rotate right X steps
        means that the whole string should be rotated; for example, one right rotation would turn abcd into dabc. """
        l = len(password)
        steps = int(params[0]) % l

        return password[l - steps:] + password[:l - steps]

    @staticmethod
    def rotate_position(password, params):
        """ rotate based on position of letter X
        means that the whole string should be rotated to the right based on the index of letter X (counting from 0)
        as determined before this instruction does any rotations. Once the index is determined, rotate the string
        to the right one time, plus a number of times equal to that index, plus one additional time if the index
        was at least 4. """
        letter_X = params[0]
        pos_X = password.find(letter_X) + 1
        if pos_X > 4:
            pos_X += 1
        return Scrambler.rotate_right(password, (pos_X,))

    @staticmethod
    def reverse(password, params):
        """ reverse positions X through Y
        means that the span of letters at indexes X through Y (including the letters at X and Y)
        should be reversed in order."""
        pos_x = min(int(params[0]), int(params[1]))
        pos_y = max(int(params[0]), int(params[1])) + 1

        x = "{}{}{}".format(password[:pos_x],
                            (password[pos_x:pos_y])[::-1],
                            password[pos_y:] if pos_y < len(password) else "")
        return x

    @staticmethod
    def move(password, params):
        """ move position X to position Y
        means that the letter which is at index X should be removed from the string, then inserted such
        that it ends up at index Y. """
        pos_x = int(params[0])
        pos_y = int(params[1])
        letter_x = password[pos_x]
        p1 = password[:pos_x] + password[pos_x + 1:]
        if pos_y > len(p1):
            return p1 + letter_x
        else:
            return "{}{}{}".format(p1[:pos_y], letter_x, p1[pos_y:])

    def parse(self, instruction):
        for regex, func in self.command_lookup.items():
            result = regex.match(instruction)
            if result:
                return func, result.groups()
        else:
            print("No match for", instruction)


class Unscrambler(Scrambler):
    @staticmethod
    def rotate_left(password, params):
        return Scrambler.rotate_right(password, params)

    @staticmethod
    def rotate_right(password, params):
        return Scrambler.rotate_left(password, params)

    @staticmethod
    def rotate_position(password, params):
        """ This only works if there's only one way of reverting the password. Luckily this is the case
        for my input. """
        for i in range(len(password)):
            try_password = Scrambler.rotate_right(password, (i, ))
            rotated_password = Scrambler.rotate_position(try_password, params)
            if password == rotated_password:
                return try_password

    @staticmethod
    def move(password, params):
        return Scrambler.move(password, (params[1], params[0]))


def scramble_password(password, instructions):
    return Scrambler(instructions).run(password)


def unscramble_password(password, instructions):
    return Unscrambler(instructions[::-1]).run(password)


if __name__ == '__main__':
    with open('../../../data/2016/input.21.txt', 'r') as fh:
        lines = fh.readlines()

    scrambler = Scrambler(lines)
    scrambled_password = scrambler.run('abcdefgh')
    print("Scrambled password", scrambled_password)

    backwards_instructions = lines[::-1]
    unscrambler = Unscrambler(backwards_instructions)
    print("Unscrambled password", unscrambler.run("fbgdceah"))
