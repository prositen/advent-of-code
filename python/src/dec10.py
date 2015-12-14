__author__ = 'Anna'


def look_and_say(sequence):
    output = []
    current = sequence[0]
    count = 1
    for char in sequence[1:]:
        if char == current:
            count += 1
        else:
            output.extend([str(count), current])
            count = 1
            current = char
    output.extend([str(count), current])
    return ''.join(output)


if __name__ == '__main__':
    seq = '1113222113'
    for x in range(0, 40):
        seq = look_and_say(seq)
    print(len(seq))
    for x in range(0, 10):
        seq = look_and_say(seq)
    print(len(seq))
