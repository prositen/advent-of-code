import re

__author__ = 'anna'

RE_STRAIGHT = re.compile(r'abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz')
RE_TWO_PAIRS = re.compile(r'(\w)\1.*(\w)\2')
BAD_CHARS = ['i', 'o', 'l']
RE_BAD_CHARS = re.compile(r'[ilo]')


def password_valid(password):
    if re.search(RE_BAD_CHARS, password):
        return False
    if not re.search(RE_STRAIGHT, password):
        return False
    if not re.search(RE_TWO_PAIRS, password):
        return False
    return True


def increase_char(char):
    return chr(ord(char) + 1)


def increase(password):
    last_char = password[-1]
    if last_char == 'z':
        return "{0}a".format(increase(password[:-1]))
    else:
        next_char = increase_char(last_char)
        if next_char in BAD_CHARS:
            next_char = increase_char(next_char)
        return "{0}{1}".format(password[:-1], next_char)


def filter_bad(password):
    result = re.search(RE_BAD_CHARS, password)
    if result:
        pos = int(result.start())
        char = password[pos]
        rest = len(password) - pos - 1
        password = "{0}{1}{2}".format(password[:pos], increase_char(char), 'a' * rest)
    return password


def next_password(password):
    next_pwd = filter_bad(password)
    if next_pwd == password:
        next_pwd = increase(next_pwd)
    while not password_valid(next_pwd):
        next_pwd = increase(next_pwd)
    return next_pwd


if __name__ == '__main__':
    pw0 = 'hxbxwxba'
    pw1 = next_password(pw0)
    print("Next password after {0} is {1}".format(pw0, pw1))
    pw2 = next_password(pw1)
    print("After that, the next is {0}".format(pw2))
