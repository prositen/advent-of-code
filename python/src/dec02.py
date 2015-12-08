__author__ = 'anna'


def wrap(l, w, h):
    lw = l * w
    lh = l * h
    wh = w * h
    slack = min(lw, lh, wh)
    return 2*lw + 2*lh + 2*wh + slack


def ribbon(l, w, h):
    lw = 2*l + 2*w
    lh = 2*l + 2*h
    wh = 2*w + 2*h
    bow = l * w * h
    return bow + min(lw, lh, wh)


if __name__ == '__main__':
    paper = 0
    ribbon_length = 0
    with open('../../data/input.2.txt','r') as fh:
        for line in fh.readlines():
            l, w, h = map(int, line.split('x'))
            paper += wrap(l, w, h)
            ribbon_length += ribbon(l, w, h)

    print("Total amount of paper to order:", paper)
    print("Total length of ribbon to order: ", ribbon_length)
