from python.src.common import Timer, Day
import python.src.y2021

if __name__ == '__main__':
    with Timer('--- Total --- '):
        for day, cls in Day.get_all_days(2021).items():
            print(f'Day {day}')
            cls().run_day()

