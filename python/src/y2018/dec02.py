import os
from collections import Counter

from python.src.y2018.common import DATA_DIR


def box_checksum(boxes):
    box_counters = [Counter(box) for box in boxes]
    twos = len([b for b in box_counters if 2 in b.values()])
    threes = len([b for b in box_counters if 3 in b.values()])
    return twos * threes


def common_letters(boxes):
    for i, this_box in enumerate(boxes[:-1]):
        for other_box in boxes[i+1:]:
            w = [a for a, b in zip(this_box, other_box) if a == b]
            if len(w) == len(this_box)-1:
                return ''.join(w)


if __name__ == '__main__':
    with open(os.path.join(DATA_DIR, 'input.2.txt')) as fh:
        main_boxes = fh.readlines()
        print("Box checksum:", box_checksum(main_boxes))
        print("Common letters:", common_letters(main_boxes))
