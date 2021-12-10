from python.src.common import Day, timer, Timer


class NavLine(object):

    def __init__(self, line):
        self.line = line
        self.complete = ''
        self.error_code = 0
        self.parse()

    matches = {
        '{': '}',
        '(': ')',
        '[': ']',
        '<': '>'
    }

    syntax_score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    completion_score = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    def parse(self):
        brackets = list()
        for c in self.line:
            if c in '([{<':
                brackets.append(c)
            elif brackets:
                prev = brackets.pop()
                if self.matches[prev] != c:
                    self.error_code = self.syntax_score[c]
                    return
        self.complete = ''.join(self.matches[c]
                                for c in brackets[::-1])

    def score(self):
        score = 0
        for c in self.complete:
            score = (score * 5) + self.completion_score[c]
        return score


class Dec10(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2021, 10, instructions=instructions, filename=filename)

    @timer(part=1)
    def part_1(self):
        return sum(NavLine(line).error_code
                   for line in self.instructions)

    @timer(part=2)
    def part_2(self):
        scores = [
            score for score in
            (NavLine(line).score() for line in self.instructions)
            if score > 0
        ]
        scores.sort()
        return scores[len(scores) // 2]


if __name__ == '__main__':
    with Timer('Syntax Scoring'):
        Dec10().run_day()
