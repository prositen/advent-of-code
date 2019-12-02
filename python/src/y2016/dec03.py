def valid_triangle(a, b, c):
    """
    In a valid triangle, the sum of any two sides must be larger than the remaining side
    """
    return (a + b > c) and (a + c > b) and (b + c > a)


def each_line_a_triangle(lines):
    """
    In your puzzle input, how many of the listed triangles are possible?
    """
    valid_triangles = len(list(filter(lambda x: valid_triangle(x[0], x[1], x[2]), lines)))
    print("Number of valid triangles", valid_triangles)


def convert_to_vertical(lines):
    # 1                         Transpose list => list of tuples
    # 2                                                 Convert to lists => list of lists
    # 3     Flatten
    cols = [item for sublist in zip(*lines) for item in list(sublist)]
    # zip magic. We want to reuse the same iterator to the above list three times,
    # in order to group items by 3
    icols = iter(cols)
    return list(zip(icols, icols, icols))


def vertical_triangles(lines):
    """
    In your puzzle input, and instead reading by columns,
    how many of the listed triangles are possible?
    """
    triples = convert_to_vertical(lines)
    valid_triangles = len(list(filter(lambda x: valid_triangle(x[0], x[1], x[2]), triples)))
    print("Number of valid triangles", valid_triangles)


if __name__ == '__main__':
    with open('../../../data/2016/input.3.txt', 'r') as fh:
        lines = [tuple(map(int, x.split())) for x in fh.readlines()]
        each_line_a_triangle(lines)
        vertical_triangles(lines)
