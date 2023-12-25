__author__ = 'Anna'

from python.src.math import proper_divs

PUZZLE_INPUT = 36000000


def problem_1(number):
    house = 0
    input_div_10 = number / 10
    while True:
        house += 1
        presents = sum(proper_divs(house))
        if presents >= input_div_10:
            return house, presents


def problem_2(number):
    house = 0
    input_div_11 = number / 11
    while True:
        house += 1
        divisors = proper_divs(house)
        presents = sum(d for d in divisors if house / d <= 50)
        if presents >= input_div_11:
            return house, presents


def main():
    number = 36000000

    house, presents = problem_1(number)
    print("House {0} got {1} presents".format(house, presents))
    house, presents = problem_2(number)
    print("House {0} got {1} presents".format(house, presents))


if __name__ == '__main__':
    main()
