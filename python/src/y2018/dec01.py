import os
from itertools import cycle

from python.src.y2018.common import DATA_DIR


def frequency_change(frequencies, start=0):
    numbers = list(map(int, frequencies))
    return sum([start] + numbers)


def first_repeating_frequency(frequencies):
    numbers = list(map(int, frequencies))
    found = {0}
    current = 0
    for n in cycle(numbers):
        current += n
        if current in found:
            return current
        found.add(current)


if __name__ == '__main__':
    with open(os.path.join(DATA_DIR, 'input.1.txt')) as fh:
        frequencies = fh.readlines()
        print("Frequency sum", frequency_change(frequencies))
        print("Captcha sum: ", first_repeating_frequency(frequencies))
