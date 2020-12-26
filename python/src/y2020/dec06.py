from python.src.common import Day, timer, Timer


class Dec06(Day, year=2020, day=6):

    @staticmethod
    def parse_instructions(instructions):
        return Day.parse_groups(instructions)

    def count_answers(self, everyone=False):
        total_sum = 0
        for group in self.instructions:
            answers = set(group[0])
            for row in group[1:]:
                if everyone:
                    answers = answers.intersection(row)
                else:
                    answers = answers.union(row)
            total_sum += len(answers)
        return total_sum

    @timer(part=1)
    def part_1(self):
        return self.count_answers(everyone=False)

    @timer(part=2)
    def part_2(self):
        return self.count_answers(everyone=True)


if __name__ == '__main__':
    with Timer('Custom Customs'):
        Dec06().run_day()
