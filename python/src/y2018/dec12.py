from python.src.common import Day


class Dec12(Day):

    def __init__(self, instructions=None, filename=None):
        super().__init__(2018, 12, instructions, filename)
        self.initial_state = self.instructions[0]
        self.rules = {rule_from: rule_to for rule_from, rule_to in self.instructions[1]}

    @staticmethod
    def parse_instructions(instructions):
        initial_state = instructions[0].split()[2]
        rules = []
        for rule in instructions[2:]:
            w = rule.split()
            rules.append((w[0], w[2]))
        return initial_state, rules

    def run2(self, state, generations, zero_pos=0):
        for _ in range(generations):
            state = '....' + state.strip('.') + '....'
            zero_pos += 4
            new_state = ['.'] * len(state)
            for i in range(2, len(state) - 2):
                pots = state[i - 2:i + 3]
                new_state[i] = self.rules.get(pots, '.')
            state = ''.join(new_state)
            zero_pos -= state.index('#')
            state = state.strip('.')

        score = 0
        for i, p in enumerate(state):
            if p == '#':
                score += i - zero_pos
        return score, zero_pos, state

    def part_1(self):
        return self.run2(state=self.initial_state, generations=20)[0]

    def part_2(self):
        state = self.initial_state
        prev_score = 0
        gens = 100
        zero_pos = 0
        last_diff = 0
        scores = list()
        for i in range(100):
            score, zero_pos, state = self.run2(state=state, generations=gens, zero_pos=zero_pos)
            scores.append((i * gens + gens, score))
            diff = score - prev_score
            prev_score = score
            if diff == last_diff:
                break
            last_diff = diff
        x1, y1 = scores[-2]
        x2, y2 = scores[-1]
        slope = (y2 - y1) / (x2 - x1)
        intercept = y1 - x1 * slope

        return int(50000000000 * slope + intercept)


if __name__ == '__main__':
    d = Dec12()
    print("Sum of pot# after 20 generations:", d.part_1())
    print("Sum of pot# after 50 000 000 000 generations:", d.part_2())
