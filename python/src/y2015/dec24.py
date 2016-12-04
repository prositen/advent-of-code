from functools import reduce
from itertools import permutations


def quantum_entanglement(packages):
    return reduce(lambda x, y: x*y, packages)


def smallest_group(packages, number_of_groups):
    weight = sum(packages) / number_of_groups
    package_count = len(packages)

    sorted_min = sorted(packages)
    sorted_max = packages[::-1]
    cumulative_min = [sum(sorted_min[:x]) for x in range(1, package_count)]
    cumulative_max = [sum(sorted_max[:x]) for x in range(1, package_count)]
    min_items_needed = 0
    max_items_needed = 0

    for index, num in enumerate(cumulative_max):
        if num >= weight:
            min_items_needed = index
            break
    for index, num in enumerate(cumulative_min):
        if num >= weight:
            max_items_needed = index
            break

    perms = set()
    for n in range(min_items_needed, max_items_needed):
        perms = set(filter(lambda x: sum(x) == weight, permutations(packages, n)))
        if len(perms):
            break

    groups = sorted(perms, key=lambda x: (len(x), quantum_entanglement(x)))
    return groups[0]


if __name__ == '__main__':
    with open('../../../data/2015/input.24.txt', 'r') as fh:
        packages = [int(p) for p in fh.readlines()]
        print("Part 1. This takes a couple of minutes")
        smallest = smallest_group(packages, 3)
        print(smallest, quantum_entanglement(smallest))
        # This is quick!
        print("Part 2")
        smallest = smallest_group(packages, 4)
        print(smallest, quantum_entanglement(smallest))
