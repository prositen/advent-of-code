from collections import Counter
from functools import lru_cache, reduce
from itertools import product
from math import sqrt

__author__ = 'Anna'

PUZZLE_INPUT = 36000000

MUL = int.__mul__


@lru_cache(maxsize=None)
def prime_factors(n):
    for f in range(2, int(sqrt(n) + 1)):
        d, m = divmod(n, f)
        if not m:
            return [f] + prime_factors(d)
    return [n]


def proper_divs(n):
    """Return the set of proper divisors of n."""
    pf = Counter(prime_factors(n))

    factors, occurrences = pf.keys(), pf.values()
    multiplicities = product(*(range(oc + 1) for oc in occurrences))
    divs = {reduce(MUL, (pf ** m for pf, m in zip(factors, multis)), 1)
            for multis in multiplicities}
    return divs or ({1} if n != 1 else set())


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
