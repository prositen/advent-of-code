from collections import Counter
from functools import lru_cache, reduce
from itertools import product
from math import sqrt

MUL = int.__mul__


def extended_euclid(a: int, b: int) -> tuple[int, int]:
    """
    >>> extended_euclid(10, 6)
    (-1, 2)
    >>> extended_euclid(7, 5)
    (-2, 3)
    """
    if b == 0:
        return 1, 0
    (x, y) = extended_euclid(b, a % b)
    k = a // b
    return y, x - k * y


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
