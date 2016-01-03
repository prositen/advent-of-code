import re

__author__ = 'Anna'


class Rule(object):

    RE_RULE = re.compile(r'(\w+) => (\w+)')

    def __init__(self, rule):
        result = self.RE_RULE.match(rule)
        if result:
            self.source = result.group(1)
            self.target = result.group(2)

    def transform_start(self, text):
        if text.startswith(self.source):
            return self.target, text[len(self.source):]
        elif len(text) > 1:
            return text[0], text[1:]
        else:
            return text[0], None

    def transform_any(self, text):
        found = text.find(self.source)
        transformed = list()
        while found > -1:
            new_text = text[:found] + text[found:].replace(self.source, self.target, 1)
            transformed.append(new_text)
            found = text.find(self.source, found+1)
        return list(set(transformed))

    def __str__(self):
        return "{0} => {1}".format(self.source, self.target)


def replace_molecules(rules_as_text, start_string):
    rules = [Rule(rule) for rule in rules_as_text]
    replacements = list()
    for r in rules:
        replacements.extend(r.transform_any(start_string))
    return list(set(replacements))


def main():
    with open('../../data/input.19.txt') as fh:
        lines = fh.readlines()
        replacements = replace_molecules(lines[:-2], lines[-1])
        print("We can create {0} replacements".format(len(replacements)))

if __name__ == '__main__':
    main()