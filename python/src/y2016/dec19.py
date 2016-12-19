from math import log


def remaining_elf_dumb(no_elves):
    """
    Brute-force algorithm used so I could find a pattern.
    :param no_elves:
    :return:
    """
    start = 0
    elf_count = no_elves
    elves = [x for x in range(1, no_elves + 1)]
    while elf_count > 1:
        elves = [x for i, x in enumerate(elves[start:]) if i % 2 == 0]
        if elf_count % 2 == 1:
            elves = elves[1:]
        elf_count = len(elves)
    return elves[0]


def remaining_elf(no_elves):
    pow2 = 2 ** int(log(no_elves, 2))
    return (no_elves - pow2) * 2 + 1


def steal_across_dumb(no_elves):
    """
    Brute-force algorithm used so I could find a pattern.
    :param no_elves:
    :return:
    """
    elf_count = no_elves
    elves = [x for x in range(1, no_elves + 1)]
    while elf_count > 1:
        mid = elf_count // 2
        elves = elves[1:mid] + elves[mid + 1:] + elves[0:1]
        elf_count = len(elves)
    return elves[0]


def steal_across(no_elves):
    pow3 = 3 ** int(log(no_elves, 3))
    twice_pow3 = 2 * pow3
    if no_elves == pow3:
        return pow3
    elif no_elves > twice_pow3:
        return pow3 + 2 * (no_elves - twice_pow3)
    else:
        return no_elves - pow3


if __name__ == '__main__':
    # Find pattern for part A

    # for i in range(1, 101):
    #   dumb = remaining_elf_dumb(i)
    #    smart = remaining_elf(i)
    #   print(i, dumb, smart, dumb == smart)

    # Find pattern for part B

    # for i in range(1, 101):
    #    dumb = steal_across_dumb(i)
    #    smart = steal_across(i)
    #    print(i, dumb, smart, dumb == smart)

    print("The remaining elf when starting with 3014603 and stealing the next elf's present is", remaining_elf(3014603))
    print("The remaining elf when starting with 3014603 and stealing from the elf across is", steal_across(3014603))
