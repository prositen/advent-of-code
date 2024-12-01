__author__ = 'anna'


def wrap(length, width, height):
    lw = length * width
    lh = length * height
    wh = width * height
    slack = min(lw, lh, wh)
    return 2 * lw + 2 * lh + 2 * wh + slack


def ribbon(length, width, height):
    lw = 2 * length + 2 * width
    lh = 2 * length + 2 * height
    wh = 2 * width + 2 * height
    bow = length * width * height
    return bow + min(lw, lh, wh)


if __name__ == '__main__':
    paper = 0
    ribbon_length = 0
    with open('../../../data/2015/input.2.txt', 'r') as fh:
        for line in fh.readlines():
            l, w, h = map(int, line.split('x'))
            paper += wrap(l, w, h)
            ribbon_length += ribbon(l, w, h)

    print("Total amount of paper to order:", paper)
    print("Total length of ribbon to order: ", ribbon_length)
