__author__ = 'Anna'
from hashlib import md5

SECRET = 'uqwqemis'


def hash_password(secret, password_letters=8, zeroes=5):
    number = 0
    hashcode = ''
    z = '0' * zeroes
    password = ''
    for n in range(password_letters):
        while not hashcode.startswith(z):
            number += 1
            value = ("%s%d" % (secret, number)).encode('utf-8')
            hashcode = md5(value).hexdigest()
        password += hashcode[zeroes]
        hashcode = ''

    return password


def movie_password(secret, password_letters=8, zeroes=5):
    number = 0
    hashcode = ''
    z = '0' * zeroes
    password = ['_'] * password_letters
    while '_' in password:
        while not hashcode.startswith(z):
            number += 1
            value = ("%s%d" % (secret, number)).encode('utf-8')
            hashcode = md5(value).hexdigest()
        position = int(hashcode[zeroes], 16)
        character = hashcode[zeroes + 1]
        if position < password_letters and password[position] == '_':
            password[position] = character
            print(''.join(password))
        hashcode = ''

    return ''.join(password)


if __name__ == '__main__':
    print("Password:", hash_password(SECRET))
    print("Movie style password", movie_password(SECRET))
