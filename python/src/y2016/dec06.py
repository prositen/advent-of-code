from collections import Counter


def repetition_code(data):
    return ''.join(Counter(x).most_common(1)[0][0] for x in zip(*data))


def modified_repetition_code(data):
    return ''.join(Counter(x).most_common()[::-1][0][0] for x in zip(*data))


if __name__ == '__main__':
    with open('../../../data/2016/input.6.txt', 'r') as fh:
        lines = fh.readlines()
        print(repetition_code(lines))
        print(modified_repetition_code(lines))