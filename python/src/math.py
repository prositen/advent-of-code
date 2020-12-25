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
