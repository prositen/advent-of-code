import math
from collections import deque

from python.src.common import Day, timer, Timer


class Rule(object):

    def __init__(self, rule: str):
        self.category = rule[0]
        self.op = rule[1]
        i = rule.index(':')
        self.rating = int(rule[2:i])
        self.target = rule[i + 1:]

    def __repr__(self):
        return f'({self.category}{self.op}{self.rating}:{self.target})'


class Part(object):

    def __init__(self, part: str):
        ratings = part[1:-1].split(',')
        self.ratings = {
            r[0]: int(r[2:]) for r in ratings
        }

    def __repr__(self):
        return (f'<Part x={self.ratings["x"]},'
                f'm={self.ratings["m"]},'
                f'a={self.ratings["a"]},'
                f's={self.ratings["s"]}>')


class Workflow(object):
    def __init__(self, workflow: str):
        i = workflow.index('{')
        self.name = workflow[:i]
        rules = workflow[i + 1:-1].split(',')
        self.rules = [Rule(rule) for rule in rules[:-1]]
        self.final_step = rules[-1]

    def run(self, part: Part):
        for rule in self.rules:
            rating = part.ratings[rule.category]
            match rule.op:
                case '<':
                    if rating < rule.rating:
                        return rule.target
                case '>':
                    if rating > rule.rating:
                        return rule.target
        return self.final_step


class System(object):

    def __init__(self, workflows, parts):
        workflows = [Workflow(wf) for wf in workflows]
        self.workflows = {wf.name: wf for wf in workflows}
        self.parts = [Part(p) for p in parts]

    def run(self):
        part_sum = 0
        for part in self.parts:
            next_step = 'in'
            while next_step not in {'A', 'R'}:
                wf = self.workflows[next_step]
                next_step = wf.run(part)
            if next_step == 'A':
                part_sum += sum(part.ratings.values())
        return part_sum

    def find_acceptance_criteria(self):
        to_visit = deque()
        to_visit.append(('in', {'x': range(1, 4001),
                                'm': range(1, 4001),
                                'a': range(1, 4001),
                                's': range(1, 4001)}
                         ))
        accepted = 0
        while to_visit:
            next_step, ratings = to_visit.popleft()
            if next_step == 'A':
                accepted += math.prod(len(v) for v in ratings.values())
            else:
                wf = self.workflows[next_step]
                for rule in wf.rules:
                    rating_range = ratings[rule.category]
                    rr = rule.rating
                    if rr in rating_range:
                        if rule.op == '<':
                            # rule: x<2000:label     x=range(1000,3000) -> split
                            next_range = range(rating_range.start, rr)
                            ratings[rule.category] = range(rr, rating_range.stop)
                        else:
                            # rule: x>2000:label     x=range(1000,3000) -> also split
                            next_range = range(rr + 1, rating_range.stop)
                            ratings[rule.category] = range(rating_range.start, rr + 1)
                    elif rr < rating_range.start:
                        if rule.op == '<':
                            # rule: x<2000:label    x=range(3000,4001) -> continue
                            continue
                        else:
                            # rule: x>2000:label    x=range(3000,4001) -> go to label
                            next_range = rating_range
                    else:  # rr > rating_range.stop
                        if rule.op == '<':
                            # rule: x<3000:label    x=range(1000,2000) -> go to label
                            next_range = rating_range
                        else:
                            # rule: x>3000:label    x=range(1000,2000) -> continue
                            continue
                    if rule.target != 'R':
                        to_visit.appendleft((
                            rule.target,
                            {
                                **ratings,
                                rule.category: next_range
                            }
                        ))

                if wf.final_step != 'R':
                    to_visit.appendleft((
                        wf.final_step,
                        ratings
                    ))

        return accepted


class Dec19(Day, year=2023, day=19):

    @staticmethod
    def parse_instructions(instructions):
        groups = Day.parse_groups(instructions)
        return groups[0], groups[1]

    @timer(part=1)
    def part_1(self):
        return System(*self.instructions).run()

    @timer(part=2)
    def part_2(self):
        return System(*self.instructions).find_acceptance_criteria()


if __name__ == '__main__':
    with Timer('Total'):
        Dec19().run_day()
