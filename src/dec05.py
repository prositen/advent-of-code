import fileinput
import re

__author__ = 'Anna'

BAD = re.compile('ab|cd|pq|xy')
VOWELS = re.compile('[aeiou].*[aeiou].*[aeiou]')
DOUBLE = re.compile('(.)\\1')
DOUBLE_PAIR = re.compile('(..).*\\1')
REPEATING_LETTER = re.compile('(.).\\1')


def bad_substring(word):
    return re.search(BAD, word)


def three_wovels(word):
    return re.search(VOWELS, word)


def double_letter(word):
    return re.search(DOUBLE, word)


def naughty_or_nice_1(word):
    if bad_substring(word):
        return False
    if not three_wovels(word):
        return False
    if not double_letter(word):
        return False
    return True


def double_pair(word):
    return re.search(DOUBLE_PAIR, word)


def repeating_letter(word):
    return re.search(REPEATING_LETTER, word)


def naughty_or_nice_2(word):
    return double_pair(word) and repeating_letter(word)


if __name__ == '__main__':
    nice_1 = 0
    nice_2 = 0
    for line in fileinput.input('../data/input.5.txt'):
        if naughty_or_nice_1(line):
            nice_1 += 1
        if naughty_or_nice_2(line):
            nice_2 += 1

    print('Nice words: 1: {nice}, 2: {nice2}'.format(nice=nice_1, nice2=nice_2))