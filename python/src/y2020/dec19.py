from collections import deque

from python.src.common import Day, timer, Timer


class Dec19(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2020, 19, instructions, filename)
        self.rules = dict()
        rule_strings, self.messages = self.instructions
        self.parse_rules(rule_strings)

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_groups(instructions)

    def parse_rules(self, rules):
        for rule in rules:
            number, value = rule.split(':')
            number = number.strip()
            if '"' in value:
                options = value.strip()[1]
            else:
                options = list(
                    option.strip().split(' ')
                    for option in value.strip().split('|')
                )
            self.rules[number] = options

    def match_rule(self, message, rule_number):
        rule = self.rules[rule_number]
        if isinstance(rule, list):
            for sub_rule in rule:
                yield from self.match_sub_rules(message, sub_rule)
        elif message and message[0] == rule:
            yield message[1:]

    def match_sub_rules(self, message, sub_rules):
        if sub_rules:
            first, *remainder = sub_rules
            for to_match in self.match_rule(message, first):
                yield from self.match_sub_rules(to_match, remainder)
        else:
            yield message

    def match(self, message):
        return any(not m for m in self.match_rule(message, '0'))

    @timer(part=1)
    def part_1(self):
        return sum(self.match(m) for m in self.messages)

    @timer(part=2)
    def part_2(self):
        self.rules['8'] = [['42'], ['42', '8']]
        self.rules['11'] = [['42', '31'], ['42', '11', '31']]

        return sum(self.match(m) for m in self.messages)


if __name__ == '__main__':
    with Timer():
        Dec19().run_day()
