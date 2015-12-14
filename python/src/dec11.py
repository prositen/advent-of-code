import re

__author__ = 'anna'

RE_STRAIGHT = re.compile(r'abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz')
RE_TWO_PAIRS = re.compile(r'(\w)\1.*(\w)\2')


def password_valid(password):
    if any(char in password for char in ['i', 'o', 'l']):
        return False
    if not re.search(RE_STRAIGHT, password):
        return False
    if not re.search(RE_TWO_PAIRS, password):
        return False
    return True


def increase_char(char):
    return chr(ord(char)+1)


def increase(password):
    last_char = password[-1]
    if last_char == 'z':
        return "{0}a".format(increase(password[:-1]))
    else:
        next_char = increase_char(last_char)
        if next_char in ['i', 'o', 'l']:
            next_char = increase_char(next_char)
        return "{0}{1}".format(password[:-1], next_char)


def next_password(password):
    next_pwd = increase(password)
    while not password_valid(next_pwd):
        next_pwd = str(increase(next_pwd))
    return next_pwd


if __name__ == '__main__':
    print("Next password after {0} is {1}".format('hxbxwxba', next_password('hxbxwxba')))