import re

__author__ = 'anna'


class Aunt(object):
    RE_AUNT = re.compile(r'Sue (\d+): (.*)')

    def __init__(self, line):
        self.possessions = dict()
        result = re.match(self.RE_AUNT, line)
        if result:
            self.number = int(result.group(1))
            for item in result.group(2).split(','):
                name, count = item.split(':')
                self.possessions[name.strip()] = int(count.strip())
        else:
            raise ValueError("Wrong format for aunt:", line)


def filter_factory(item, count, retroencabulator):

    def filter_possession(aunt):
        if item not in aunt.possessions:
            return True
        if retroencabulator:
            if item in ('cats', 'trees'):
                return aunt.possessions[item] > count
            elif item in ('pomeranians', 'goldfish'):
                return aunt.possessions[item] < count
        if aunt.possessions[item] == count:
            return True
        return False
    return filter_possession


def find_aunt(aunt_lines, ticker, retroencabulator):
    aunts = list()
    for line in aunt_lines:
        aunts.append(Aunt(line))
    for item, count in ticker.items():
        filter_item = filter_factory(item, count, retroencabulator)
        aunts = filter(filter_item, aunts)
    aunts = list(aunts)
    if len(aunts) > 1:
        raise ValueError("More than one aunt left")
    return aunts[0]


def main():
    with open('../../../data/2015/input.16.txt', 'r') as fh:
        aunts = fh.readlines()
        ticker = {'children': 3,
                  'cats': 7,
                  'samoyeds': 2,
                  'pomeranians': 3,
                  'akitas': 0,
                  'vizslas': 0,
                  'goldfish': 5,
                  'trees': 3,
                  'cars': 2,
                  'perfumes': 1}
        print("Ticker: ", ticker)
        aunt = find_aunt(aunts, ticker, False)
        print("Aunt number {no}, possessions: {things}".format(no=aunt.number, things=aunt.possessions))
        aunt = find_aunt(aunts, ticker, True)
        print("Aunt number {no}, possessions: {things}".format(no=aunt.number, things=aunt.possessions))

if __name__ == '__main__':
    main()