__author__ = 'Anna'
from hashlib import md5

SECRET = 'ckczppom'


def mining_hashes(secret, zeroes=5):
    """
    Yay bruteforce.
    :param secret:
    :param zeroes:
    :return: Lowest decimal number yielding a md5 hash starting with the specified number of zeroes
    """
    number = 0
    hashcode = ''
    z = '0' * zeroes
    while not hashcode.startswith(z):
        number += 1
        value = ("%s%d" % (secret, number)).encode('utf-8')
        hashcode = md5(value).hexdigest()

    return number


if __name__ == '__main__':
    print("Number with five leading zeroes:", mining_hashes(SECRET))
    print("Number with six leading zeroes:", mining_hashes(SECRET, 6))
