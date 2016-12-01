from collections import defaultdict

__author__ = 'anna'


def fit_recursive(bins, eggnog, current_trail=None, collection=None, indent=0):
    if eggnog == 0:
        return True
    s = sum(bins)
    if s < eggnog:
        return False
    if not current_trail:
        current_trail = list()

    remaining_bins = list(filter(lambda k: k <= eggnog, bins))
    for pos, next_bin in enumerate(remaining_bins):
        trail = list(current_trail)
        trail.append(next_bin)
        current_eggnog = eggnog - next_bin
        if fit_recursive(remaining_bins[pos+1:], current_eggnog, trail, collection, indent+1):
            collection.append(trail)


def fit_eggnog(bins, eggnog):
    bins = sorted(bins, reverse=True)
    combinations = list()
    fit_recursive(bins, eggnog, collection=combinations)
    return combinations


def group_by_containers_needed(combinations):
    groups = defaultdict(list)
    for x in combinations:
        groups[len(x)].append(x)
    return groups


def fewest_containers(combinations):
    groups = group_by_containers_needed(combinations)
    size = min(groups.keys())
    return size, len(groups[size])


def main():
    with open('../../../data/2015/input.17.txt', 'r') as fh:
        bins = [int(line) for line in fh.readlines()]
        combinations = fit_eggnog(bins, 150)
        print("There are {no} combinations of bins to store 150 liters of eggnog".format(no=len(combinations)))
        size, number = fewest_containers(combinations)
        print("There are {number} ways of storing 150 liters of eggnog in {size} containers".format(number=number,
                                                                                                    size=size))

if __name__ == '__main__':
    main()
