from python.src.common import Timer, Day
import python.src.y2020  # noqa 401

if __name__ == '__main__':
    with Timer('--- Total --- '):
        for day, cls in Day.get_all_days(2020).items():
            cls().run_day()
