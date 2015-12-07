import fileinput

__author__ = 'Anna'


VOWELS = 'aeiou'
BAD = ['ab', 'cd', 'pq', 'xy']


def naughty_or_nice(word):
    if any([word.contains(bad) for bad in BAD]):
        return False


if __name__ == '__main__':
    nice = 0
    for line in fileinput.input('../data/input.5.txt'):
        if naughty_or_nice(line):
            nice += 1

    print('Nice words: {nice}'.format(nice=nice))