import re

re_PASSPHRASE = re.compile(r'(\b\w+\b)(\s\w+\b)*\s(\1\b)')


def valid_passphrases(puzzle_input):
    return len(list(filter(is_valid, puzzle_input)))


def is_valid(param):
    return re_PASSPHRASE.search(param) is None


def valid_anagram_passphrases(puzzle_input):
    return len(list(filter(is_valid_anagram, puzzle_input)))


def is_valid_anagram(passphrase):
    words = passphrase.split()
    ordered_passphrase = " ".join(["".join(sorted(word)) for word in words])
    return re_PASSPHRASE.search(ordered_passphrase) is None

if __name__ == '__main__':
    with open('../../../data/2017/input.4.txt', 'r') as fh:
        puzzle_input = fh.readlines()
        print(len(puzzle_input))
        print("# of valid passphrases: {}".format(valid_passphrases(puzzle_input)))
        print("# of valid anagram passhprases: {}".format(valid_anagram_passphrases(puzzle_input)))

