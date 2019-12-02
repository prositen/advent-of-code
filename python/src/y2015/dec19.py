import re

__author__ = 'Anna'


class Rule(object):
    RE_RULE = re.compile(r'(\w+) => (.*)\n?')

    def __init__(self, rule):
        result = self.RE_RULE.match(rule)
        if result:
            self.source = result.group(1)
            self.target = result.group(2)
        else:
            raise ValueError(rule + " didn't match")

    def transform_any(self, text):
        found = text.find(self.source)
        transformed = list()
        while found > -1:
            new_text = text[:found] + text[found:].replace(self.source, self.target, 1)
            transformed.append(new_text)
            found = text.find(self.source, found + 1)
        return list(set(transformed))

    def __str__(self):
        return "{0} => {1}".format(self.source, self.target)


def sanitize(text):
    text = text.replace('Ar', ')')
    text = text.replace('Rn', '(')
    text = text.replace('Y', ',')
    return text


class FusionFission(object):
    RE_TOKEN = re.compile(r'((?:[A-Z][a-z]*)|(?:[\(\),]))')

    def __init__(self, rules_as_text, start_string):
        self.rules = [Rule(sanitize(rule)) for rule in rules_as_text]
        self.text = sanitize(start_string)
        self.text_tokens = self.RE_TOKEN.findall(self.text)

    def one_step(self):
        replacements = list()
        for r in self.rules:
            replacements.extend(r.transform_any(self.text))
        return list(set(replacements))

    def ugly_count(self):
        # https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju
        parentheses = self.text.count('(') + self.text.count(')')
        comma = self.text.count(',')
        length = len(self.text_tokens)
        return length - parentheses - 2 * comma - 1


def main():
    with open('../../../data/2015/input.19.txt') as fh:
        lines = fh.readlines()
        rules = lines[:-2]
        text = lines[-1].strip()
        r = FusionFission(rules, text)
        replacements = r.one_step()
        print("We can create {0} replacements".format(len(replacements)))
        print("It takes {0} steps to reach the medicine".format(r.ugly_count()))


if __name__ == '__main__':
    main()
