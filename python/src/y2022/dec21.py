from python.src.common import Day, timer, Timer


def solve_monkey_riddle(rules):
    prev_rules = dict()
    while prev_rules != rules:
        prev_rules = dict(rules)
        for name, job in list(rules.items()):
            match job:
                case (aa, op, bb):
                    a = rules.get(aa, aa)
                    b = rules.get(bb, bb)
                    if isinstance(a, int) and isinstance(b, int):
                        match op:
                            case '+':
                                rules[name] = a + b
                            case '-':
                                rules[name] = a - b
                            case '*':
                                rules[name] = a * b
                            case '/':
                                rules[name] = a // b
                            case '=':
                                rules[name] = a
                    elif isinstance(a, int):
                        rules[name] = (a, op, bb)
                    elif isinstance(b, int):
                        rules[name] = (aa, op, b)

    return rules


def invert_rules(rules):
    invert_op = {
        '*': '/',
        '/': '*',
        '+': '-',
        '-': '+',
        '=': '='
    }
    inverted = dict()
    for name, job in rules.items():
        match job:
            case (a, '-', str(b)):
                inverted[b] = (a, '-', name)
            case (a, op, str(b)):
                inverted[b] = (name, invert_op[op], a)
            case (str(a), op, b):
                inverted[a] = (name, invert_op[op], b)
    root = rules['root']
    if isinstance(root[0], int):
        root = root[0]
    else:
        root = root[2]
    inverted['root'] = root
    return solve_monkey_riddle(inverted)


class Dec21(Day, year=2022, day=21):

    @staticmethod
    def parse_instructions(instructions):
        result = dict()
        for line in instructions:
            name, job = line.split(': ')
            match job.split():
                case [a, op, b]:
                    result[name] = (a, op, b)
                case [n]:
                    result[name] = int(n)
        return result

    @timer(part=1)
    def part_1(self):
        return solve_monkey_riddle(dict(self.instructions))['root']

    @timer(part=2)
    def part_2(self):
        part_2 = dict(self.instructions)
        part_2['root'] = (part_2['root'][0], '=', part_2['root'][2])
        del part_2['humn']
        return invert_rules(solve_monkey_riddle(part_2))['humn']


if __name__ == '__main__':
    with Timer('Total'):
        Dec21().run_day()
