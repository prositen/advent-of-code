__author__ = 'anna'


def char_decode_diff(text):
    mem_length = len(text)
    char_length = len(eval(text))
    return mem_length - char_length


def char_encode_diff(text):
    added_backslash = text.count('\\')
    added_quote = text.count('"')
    added = added_backslash + added_quote + 2
    return added

if __name__ == '__main__':
    with open('../../data/input.8.txt', 'r') as fh:
        total_decode_diff = 0
        total_encode_diff = 0
        for line in fh.readlines():
            text = line.strip()

            total_decode_diff += char_decode_diff(text)
            total_encode_diff += char_encode_diff(text)

    print("Diff is {diff} (decode) & {diff2} (encode)".format(diff=total_decode_diff, diff2=total_encode_diff))
