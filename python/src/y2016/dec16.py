FLIP = str.maketrans("10", "01")


def dragon_curve(code):
    return code + '0' + code.translate(FLIP)[::-1]


def checksum(code):
    pairs = zip(code[::2], code[1::2])
    _checksum = [1 if a == b else 0 for a, b in pairs]
    if len(_checksum) % 2:
        return ''.join(str(x) for x in _checksum)
    else:
        return checksum(_checksum)


def checksum_of(code, length):
    while len(code) < length:
        code = dragon_curve(code)
    return checksum(code[:length])


if __name__ == '__main__':
    puzzle_input = '11110010111001001'
    print("Checksum of {0}, length 272 is {1}".format(puzzle_input,
                                                      checksum_of(puzzle_input, 272)))
    print("Checksum of {0}, length 35651584 is {1}".format(puzzle_input,
                                                           checksum_of(puzzle_input, 35651584)))
