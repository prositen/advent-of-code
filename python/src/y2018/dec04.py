import os
from collections import Counter

from python.src.y2018.common import DATA_DIR


def parse_notes(watch_notes):
    watch_notes = sorted(watch_notes)
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


def sleep_strategy_1(watch_notes):
    sleep_schedule = parse_notes(watch_notes)
    most_sleep_guard = Counter(x[0] for x in sleep_schedule).most_common(1)[0][0]
    minute = Counter(x[1] for x in sleep_schedule if x[0] == most_sleep_guard).most_common(1)[0][0]

    return most_sleep_guard * minute


def sleep_strategy_2(watch_notes):
    sleep_schedule = Counter(parse_notes(watch_notes))
    most_common = sleep_schedule.most_common(1)[0][0]
    return most_common[0] * most_common[1]


if __name__ == '__main__':
    with open(os.path.join(DATA_DIR, 'input.4.txt')) as fh:
        schedule = fh.readlines()
        print("Sleep strategy 1", sleep_strategy_1(schedule))
        print("Sleep strategy 2", sleep_strategy_2(schedule))
