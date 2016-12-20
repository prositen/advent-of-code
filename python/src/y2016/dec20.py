class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def overlaps(self, other):
        overlaps = (self.end + 1 == other.start) or \
                   (self.start - 1 == other.end) or \
                   (self.start <= other.start <= self.end) or \
                   (self.start <= other.end <= self.end)
        return overlaps

    def update(self, other):
        self.start = min(self.start, other.start)
        self.end = max(self.end, other.end)

    def __repr__(self):
        return "<Range {0}-{1}>".format(self.start, self.end)

    def __len__(self):
        return self.end - self.start + 1

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


class Firewall:
    def __init__(self, lines):
        self.rules = []
        for rule in lines:
            start, end = map(int, rule.split('-', 2))
            self.rules.append(Range(start, end))
        self.allowed = []
        self._update_rules()
        self._update_allowed()

    def _update_rules(self):
        while True:
            self.rules.sort(key=lambda x: x.start)
            new_rules = []
            first = self.rules[0]
            for second in self.rules[1:]:
                if first.overlaps(second):
                    first.update(second)
                else:
                    new_rules.append(first)
                    first = second
            new_rules.append(first)
            new_rules.sort(key=lambda x: x.start)
            if len(new_rules) == len(self.rules):
                break
            self.rules = new_rules

    def lowest_not_blocked(self):
        return self.rules[0].end + 1

    def _update_allowed(self):
        start = self.rules[0].end
        for rule in self.rules[1:]:
            end = rule.start
            if start and end:
                self.allowed.append(Range(start + 1, end - 1))
            start = rule.end

    def number_of_allowed_ip_addresses(self):
        return sum(map(len, self.allowed))


if __name__ == '__main__':
    with open('../../../data/2016/input.20.txt', 'r') as fh:
        rules = fh.readlines()
    fw = Firewall(rules)
    print("The lowest not blocked IP is", fw.lowest_not_blocked())
    print("Number of allowed IP addresses is", fw.number_of_allowed_ip_addresses())
