from collections import Counter
from python.src.common import Day


class Dec04(Day):
    def __init__(self, instructions=None):
        super().__init__(2018, 4, instructions)

    @staticmethod
    def parse_instructions(instructions):
        watch_notes = sorted(instructions)
        sleep_schedule = list()
        guard = None
        sleep_start = 0
        for note in watch_notes:
            minute = int(note[15:17])
            action = note[19:].strip()
            if action.startswith("Guard"):
                guard = int(action.split()[1][1:])
            elif action == 'falls asleep':
                sleep_start = minute
            else:
                for minute in range(sleep_start, minute):
                    sleep_schedule.append((guard, minute))
        return sleep_schedule

    def part_1(self):
        most_sleep_guard = Counter(x[0] for x in self.instructions).most_common(1)[0][0]
        minute = Counter(x[1]
                         for x in self.instructions
                         if x[0] == most_sleep_guard).most_common(1)[0][0]

        return most_sleep_guard * minute

    def part_2(self):
        sleep_schedule = Counter(self.instructions)
        most_common = sleep_schedule.most_common(1)[0][0]
        return most_common[0] * most_common[1]


if __name__ == '__main__':
    d = Dec04()
    print("Sleep strategy 1:", d.part_1())
    print("Sleep strategy 2:", d.part_2())
